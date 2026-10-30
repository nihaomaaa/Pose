import pathlib,json,time,os,sys
from infer import load_pipeline,STATE,emit
import torch
key=sys.argv[1] if len(sys.argv)>1 else 'klein-4b'
start=time.time();pipe=load_pipeline(key)
emit('verifying','正在执行真实出图测试',.5)
image=pipe(prompt='A photograph of a green ceramic cup on a wooden desk, soft daylight.',width=256,height=320,num_inference_steps=4,guidance_scale=1.0,generator=torch.Generator('cpu').manual_seed(42)).images[0]
folder=STATE/'data';folder.mkdir(parents=True,exist_ok=True);image.save(folder/'setup-test.png')
(folder/('engine-9b-ready.json' if key=='klein-9b' else 'engine-custom-ready.json' if key=='custom' else 'engine-ready.json')).write_text(json.dumps(dict(ready=True,seconds=time.time()-start,device=torch.cuda.get_device_name() if torch.cuda.is_available() else 'CPU')),encoding='utf-8')
emit('completed','本地出图测试通过',1)
