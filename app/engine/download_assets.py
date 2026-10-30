import concurrent.futures,hashlib,json,os,pathlib,subprocess,time,sys,shutil
APP=pathlib.Path(__file__).resolve().parents[1];STATE=pathlib.Path(os.environ['POSE_STATE_DIR']);CURL=os.environ.get('SystemRoot','C:/Windows')+'/System32/curl.exe'
def emit(stage,message,progress=0):print(json.dumps(dict(stage=stage,message=message,progress=progress),ensure_ascii=False),flush=True)
def valid(p,size,digest,kind):
 if not p.exists() or p.stat().st_size!=size:return False
 h=hashlib.sha256() if kind=='sha256' else hashlib.sha1()
 if kind=='git':h.update(('blob '+str(size)+'\0').encode())
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 return h.hexdigest()==digest
source=json.loads((APP/'data/model-source.json').read_text());tree=json.loads((APP/'data/model-tree.json').read_text());gallery=json.loads((APP/'data/source-tree.json').read_text());items=[]
for x in tree:
 if x['type']=='file' and (x['path'].startswith(('scheduler/','text_encoder/','tokenizer/','transformer/','vae/')) or x['path'] in ['model_index.json','LICENSE.md','README.md']):
  items.append(('https://huggingface.co/'+source['repository']+'/resolve/'+source['revision']+'/'+x['path'],'models/flux2-klein/'+x['path'],x['size'],x['lfs']['oid'] if x.get('lfs') else x['oid'],'sha256' if x.get('lfs') else 'git'))
for x in gallery['tree']:
 if x['type']=='blob' and (x['path'].startswith(('img/','thumbs/')) or x['path'] in ['data/pose-zh.json','data/meta-zh.json','LICENSE']):items.append(('https://raw.githubusercontent.com/anhao/ai-pose-gallery-zh/'+gallery['sha']+'/'+x['path'],'vendor/gallery/'+x['path'],x['size'],x['sha'],'git'))
def download(item):
 url,name,size,digest,kind=item;p=STATE/name;p.parent.mkdir(parents=True,exist_ok=True)
 if valid(p,size,digest,kind):return
 cache=os.environ.get('POSE_ASSET_CACHE')
 if cache and valid(pathlib.Path(cache)/name,size,digest,kind):
  if p.exists():p.unlink()
  try:os.link(pathlib.Path(cache)/name,p)
  except OSError:shutil.copyfile(pathlib.Path(cache)/name,p)
  return
 part=p.with_suffix(p.suffix+'.part')
 if part.exists() and part.stat().st_size>=size:
  if valid(part,size,digest,kind):part.replace(p);return
  part.unlink()
 for attempt in range(12):
  args=[CURL,'-fLsS','--connect-timeout','25','--max-time','600','--speed-limit','16384','--speed-time','60','-C','-','-o',str(part),url+'?download=true&retry='+str(int(time.time()))]
  result=subprocess.run(args,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE,creationflags=0x08000000)
  if result.returncode==0 and valid(part,size,digest,kind):part.replace(p);return
  if result.returncode in (0,33) and part.exists():part.unlink()
  time.sleep(2)
 raise RuntimeError('下载或校验失败：'+name+'。请检查网络后重试，已下载部分会保留。')
total=sum(i[2] for i in items)
try:
 with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
  tasks=[pool.submit(download,i) for i in items]
  while not all(t.done() for t in tasks):
   done=0
   for _,name,size,_,_ in items:
    p=STATE/name
    try:done+=min(size,(p if p.exists() else p.with_suffix(p.suffix+'.part')).stat().st_size)
    except FileNotFoundError:pass
   emit('assets',f'下载模型与图库 · {done/1e9:.1f} / {total/1e9:.1f} GB',done/total);time.sleep(2)
  for t in tasks:t.result()
 emit('assets','模型与全部图库哈希校验通过',1)
except Exception as e:emit('failed',str(e));sys.exit(1)
