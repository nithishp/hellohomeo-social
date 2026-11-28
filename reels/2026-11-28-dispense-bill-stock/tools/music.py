# Local instrumental bed: 106.7 BPM (8 bars from lift to resolve), D major, lift at 7.0 s, resolve at 25.0 s. No samples, no vocals.
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
SR=48000; DUR=30.6; BPM=320/3; B=60/BPM
N=int(SR*DUR); L=np.zeros(N); R=np.zeros(N)
rng=np.random.default_rng(11)
def midi(m): return 440*2**((m-69)/12)
def env(n,a,d,s,r,hold):
    t=np.arange(n)/SR; e=np.ones(n)*s
    e[t<a]=t[t<a]/a
    m=(t>=a)&(t<a+d); e[m]=1-(1-s)*(t[m]-a)/d
    m=t>=hold; e[m]=s*np.exp(-(t[m]-hold)/max(r,1e-3))
    return e
def add(sig,at,pan=0.0,g=1.0):
    i=int(at*SR); j=min(N,i+len(sig)); 
    if i>=N: return
    s=sig[:j-i]*g; L[i:j]+=s*(1-pan)/1.0; R[i:j]+=s*(1+pan)/1.0
def lp(x,f,o=2): return sosfilt(butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return sosfilt(butter(o,f,'high',fs=SR,output='sos'),x)
def pad(notes,dur,bright):
    n=int(SR*(dur+1.2)); t=np.arange(n)/SR; s=np.zeros(n)
    for m in notes:
        f=midi(m)
        for det in (-0.12,0.0,0.12):
            ff=f*2**(det/12)
            s+=np.sin(2*np.pi*ff*t)+0.35*np.sin(2*np.pi*2*ff*t)+0.15*np.sin(2*np.pi*3*ff*t)
    s=lp(s,900+1600*bright)*env(n,0.35,0.5,0.8,0.9,dur)
    return s/len(notes)/3
def pluck(m,dur=0.5):
    n=int(SR*dur); t=np.arange(n)/SR; f=midi(m)
    s=(np.sin(2*np.pi*f*t)+0.5*np.sin(2*np.pi*2*f*t)*np.exp(-t*12)+0.2*np.sin(2*np.pi*3*f*t)*np.exp(-t*20))*np.exp(-t*6)
    return lp(s,4000)*np.minimum(1,t/0.004)
def bell(m,dur=3.0):
    n=int(SR*dur); t=np.arange(n)/SR; f=midi(m); s=0
    for k,a,d in ((1,1,2.2),(2.76,0.4,4),(5.4,0.2,7),(2,0.3,3)): s=s+a*np.sin(2*np.pi*f*k*t)*np.exp(-t*d)
    return s*np.minimum(1,t/0.003)
def kick():
    n=int(SR*0.45); t=np.arange(n)/SR; f=48+90*np.exp(-t*28)
    return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*9)
def shaker():
    n=int(SR*0.09); t=np.arange(n)/SR
    return hp(rng.standard_normal(n),6000)*np.exp(-t*55)
def bass(m,dur):
    n=int(SR*dur); t=np.arange(n)/SR; f=midi(m)
    return lp(np.sin(2*np.pi*f*t)+0.3*np.sign(np.sin(2*np.pi*f*t)),500)*env(n,0.01,0.2,0.7,0.12,dur-0.1)
# D major: D  Bm  G  A (1 bar each, 4 beats)
CH=[[62,66,69,73],[59,62,66,69],[55,59,62,66],[57,61,64,69]]
ROOT=[38,35,43,45]
ARP=[[74,78,81,78],[71,74,78,74],[67,71,74,79],[69,73,76,81]]
LIFT=7.0; RES=25.0
# bars: align bar starts so a bar begins exactly at LIFT
bar=4*B; t0=LIFT-np.ceil(LIFT/bar)*bar
t=t0; k=0
while t<RES-1e-6:
    c=k%4; bright=0.2 if t<LIFT else 0.6
    if t+bar>0: add(pad(CH[c],bar,bright),max(t,0) if t>=0 else 0,g=0.5 if t<LIFT else 0.6)
    for i in range(8):  # 8th-note pluck arpeggio
        tt=t+i*B/2
        if 0<=tt<RES: add(pluck(ARP[c][i%4]+(12 if (t>=LIFT and i%4==3) else 0)),tt,pan=0.3*(-1)**i,g=0.16 if tt<LIFT else 0.2)
    if t>=LIFT-1e-6:
        add(bass(ROOT[c],bar*0.95),t,g=0.32)
        for i in range(4): add(kick(),t+i*B,g=0.55)
        for i in range(8): add(shaker(),t+i*B/2+B/4,pan=0.4,g=0.10)
    t+=bar; k+=1
# pre-lift riser 5.8-7.0
n=int(SR*1.2); tt=np.arange(n)/SR; rise=hp(rng.standard_normal(n),3000)*(tt/1.2)**2*0.12; add(rise,LIFT-1.2)
# resolve at 25: D major add9 pad + bell motif, then ring
add(pad([62,66,69,76],4.6,0.5),RES,g=0.7); add(bass(38,3.5),RES,g=0.3); add(kick(),RES,g=0.5)
for i,m in enumerate([81,78,74,76]): add(bell(m),RES+0.05+i*B,g=0.12,pan=0.2*(-1)**i)
mix=np.stack([L,R],1); mix=mix/np.max(np.abs(mix))*0.8
# fade end
f=int(SR*0.6); mix[-f:]*=np.linspace(1,0,f)[:,None]
sf.write('assets/audio/music_local.wav',mix,SR)
print('bar',bar,'t0',t0)
