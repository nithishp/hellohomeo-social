import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
SR=48000; rng=np.random.default_rng(3)
def tick():
    n=int(SR*0.06); t=np.arange(n)/SR
    return (0.6*np.sin(2*np.pi*2400*t)+0.4*np.sin(2*np.pi*3600*t))*np.exp(-t*90)
def whoosh(d=0.55):
    n=int(SR*d); t=np.arange(n)/SR; x=rng.standard_normal(n); out=np.zeros(n)
    for i in range(0,n,480):
        f=400+3000*np.sin(np.pi*i/n)**2
        seg=sosfilt(butter(2,[f*0.7,f*1.3],'band',fs=SR,output='sos'),x[max(0,i-2000):i+480])[-min(480,n-i):]
        out[i:i+len(seg)]=seg
    return out*np.sin(np.pi*t/d)**2*1.6
def chime():
    n=int(SR*1.6); t=np.arange(n)/SR; s=0
    for f,a,d in ((1318.5,1,3),(1975.5,0.6,4),(2637,0.3,6)): s=s+a*np.sin(2*np.pi*f*t)*np.exp(-t*d)
    s2=np.zeros(n); k=int(0.09*SR); s2[k:]=s[:-k]*0.8
    return (s+s2)*np.minimum(1,t/0.003)*0.4
def pop():  # message arrive
    n=int(SR*0.12); t=np.arange(n)/SR; f=700+500*np.exp(-t*40)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*30)
for name,s in (('tick',tick()),('whoosh',whoosh()),('chime',chime()),('pop',pop())):
    sf.write(f'assets/audio/sfx_{name}.wav',(s/np.max(np.abs(s))*0.7).astype(np.float32),SR)
print('ok')
