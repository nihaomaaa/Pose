import json, os, pathlib, sys, time, traceback
os.environ['HF_HUB_OFFLINE']='1'
os.environ['TRANSFORMERS_OFFLINE']='1'
ROOT=pathlib.Path(__file__).resolve().parents[1]
STATE=pathlib.Path(os.environ.get('POSE_STATE_DIR',str(ROOT)))
os.environ['TORCHINDUCTOR_CACHE_DIR']=str(STATE/'runtime/torch-cache')
os.environ.setdefault('USERNAME','pose-local')
def emit(stage,message,progress=0): print(json.dumps(dict(stage=stage,message=message,progress=progress),ensure_ascii=False),flush=True)
def load_pipeline(model_key='klein-4b'):
 emit('loading','正在加载本地模型，首次加载需要一些时间',0.03)
 import torch
 from PIL import Image,ImageOps
 from diffusers import Flux2KleinPipeline,Flux2Transformer2DModel,BitsAndBytesConfig
 from transformers import Qwen3ForCausalLM,BitsAndBytesConfig as TBits
 profile=json.loads((STATE/'data/hardware-profile.json').read_text(encoding='utf-8')) if (STATE/'data/hardware-profile.json').exists() else {'profile':'cuda-nf4','precision':'bf16','device':0}
 cpu=profile['profile']=='cpu'
 if not cpu and not torch.cuda.is_available():raise RuntimeError('CUDA unavailable')
 if not cpu:torch.cuda.set_device(profile.get('device',0))
 dtype=torch.float32 if cpu else (torch.bfloat16 if profile.get('precision')=='bf16' else torch.float16)
 torch.set_num_threads(8)
 if model_key not in ('klein-4b','klein-9b','custom'):raise ValueError('Unknown model')
 model=str(STATE/('models/flux2-klein-9b' if model_key=='klein-9b' else 'models/custom' if model_key=='custom' else 'models/flux2-klein'))
 common=dict(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_compute_dtype=dtype)
 transformer=Flux2Transformer2DModel.from_pretrained(model,subfolder='transformer',quantization_config=BitsAndBytesConfig(**common) if profile['profile']=='cuda-nf4' else None,torch_dtype=dtype,local_files_only=True)
 # Move quantized denoiser to RAM before loading the larger text encoder on an 8 GB GPU.
 transformer.to('cpu');torch.cuda.empty_cache()
 emit('loading','正在准备人物与姿势理解模型',0.12)
 text=Qwen3ForCausalLM.from_pretrained(model,subfolder='text_encoder',quantization_config=TBits(**common) if profile['profile']=='cuda-nf4' else None,dtype=dtype,local_files_only=True)
 text.to('cpu');torch.cuda.empty_cache()
 pipe=Flux2KleinPipeline.from_pretrained(model,transformer=transformer,text_encoder=text,torch_dtype=dtype,local_files_only=True)
 if cpu:pipe.to('cpu')
 else:pipe.enable_model_cpu_offload(gpu_id=profile.get('device',0))
 pipe.vae.enable_tiling()
 pipe.set_progress_bar_config(disable=True)
 return pipe

def main():
 cfg=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
 import torch
 from PIL import Image,ImageOps
 started=time.time()
 pipe=load_pipeline(cfg.get('model','klein-4b'))
 Image.MAX_IMAGE_PIXELS=40000000
 def read(p,max_edge=1024):
  with Image.open(p) as im:
   im=ImageOps.exif_transpose(im).convert('RGB');im.thumbnail((max_edge,max_edge));return im.copy()
 from prompts import build_prompt
 paired=cfg.get('personCount')==2 or '双人' in cfg.get('system','')
 if paired:
  rules=json.loads((ROOT/'data/pose-rules.json').read_text(encoding='utf-8'))
  number=cfg.get('poseId','').split('_')[1] if cfg.get('poseId','').startswith('pair60_') else ''
  if number not in rules:raise ValueError('This pose is browse-only.')
  if not cfg.get('sourceB'):raise ValueError('The second person photo is required.')
 source=read(cfg['source'],768 if paired else 1024);ref=read(cfg['reference'],512 if paired else 768)
 images=[source,read(cfg['sourceB'],768),ref] if paired else [source,ref]
 captions=json.loads((ROOT/'data/pose-captions-en.json').read_text(encoding='utf-8'))
 prompt=build_prompt(cfg,captions)
 w,h={'small':(512,704),'medium':(640,864),'large':(768,1024)}[cfg.get('size','medium')]
 emit('encoding','正在理解人物外貌与姿势参考',0.22)
 def callback(pipe,step,timestep,kwargs):emit('sampling',f'正在绘制图片 · {step+1}/4',0.35+(step+1)*0.14);return kwargs
 out=pipe(image=images,prompt=prompt,width=w,height=h,num_inference_steps=4,guidance_scale=1.0,generator=torch.Generator('cpu').manual_seed(cfg['seed']),callback_on_step_end=callback).images[0]
 emit('saving','正在保存生成结果',0.96)
 from PIL.PngImagePlugin import PngInfo
 metadata=PngInfo();metadata.add_text('Software','Pose');metadata.add_text('Description','AI-generated image; not a photograph of a real event.');metadata.add_text('AI_generated','true')
 metadata.add_itxt('XML:com.adobe.xmp','<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"><rdf:Description xmlns:Iptc4xmpExt="http://iptc.org/std/Iptc4xmpExt/2008-02-29/" Iptc4xmpExt:DigitalSourceType="http://cv.iptc.org/newscodes/digitalsourcetype/trainedAlgorithmicMedia"/></rdf:RDF></x:xmpmeta>')
 target=pathlib.Path(cfg['output']);temp=target.with_suffix('.tmp');out.save(temp,format='PNG',pnginfo=metadata);temp.replace(target)
 if cfg.get('metrics'):
  pathlib.Path(cfg['metrics']).write_text(json.dumps(dict(ready=True,model=cfg.get('model','klein-4b'),device=torch.cuda.get_device_name() if torch.cuda.is_available() else 'CPU',peakVRAM=torch.cuda.max_memory_allocated() if torch.cuda.is_available() else 0,seconds=time.time()-started,testedAt=time.time())),encoding='utf-8')
if __name__=='__main__':
 try:main()
 except Exception:traceback.print_exc();sys.exit(1)
