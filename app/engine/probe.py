import ctypes,json
result=[]
try:
 cuda=ctypes.WinDLL('nvcuda.dll');cuda.cuInit(0);n=ctypes.c_int();cuda.cuDeviceGetCount(ctypes.byref(n))
 for i in range(n.value):
  name=ctypes.create_string_buffer(256);cuda.cuDeviceGetName(name,256,i);size=ctypes.c_size_t();cuda.cuDeviceTotalMem_v2(ctypes.byref(size),i);major=ctypes.c_int();minor=ctypes.c_int();cuda.cuDeviceComputeCapability(ctypes.byref(major),ctypes.byref(minor),i)
  result.append(dict(index=i,name=name.value.decode(),vram=size.value,major=major.value,minor=minor.value))
except Exception:pass
print(json.dumps(result))
