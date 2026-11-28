# No voiceover this week: music bed + SFX, loudness -14 LUFS, peaks <= -1.5 dBTP
import subprocess
A='assets/audio/'
SFX=[('tick',t,0.4) for t in (0.05,0.3,13.4,13.65,15.9,16.1,16.3,16.5,17.2)]+[('tick',t,0.55) for t in (0.9,8.6,9.3)]+\
    [('whoosh',t,0.45) for t in (2.1,6.85,11.35,15.3,18.85)]+[('whoosh',21.5,0.3)]+[('pop',t,0.5) for t in (9.5,12.5)]+[('chime',17.8,0.4),('chime',25.0,0.45)]
idx={'tick':1,'whoosh':2,'chime':3,'pop':4}
inp=['-i',A+'music_local.wav']+sum([['-i',A+f'sfx_{n}.wav'] for n in ('tick','whoosh','chime','pop')],[])
f=[]; cnt={}
for n,t,g in SFX: cnt[idx[n]]=cnt.get(idx[n],0)+1
for k,c in cnt.items(): f.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,asplit={c}"+''.join(f'[x{k}_{i}]' for i in range(c)))
use={k:0 for k in idx.values()}; outs=[]
for j,(n,t,g) in enumerate(SFX):
    k=idx[n]; i=use[k]; use[k]+=1; d=int(t*1000)
    f.append(f"[x{k}_{i}]volume={g},adelay={d}|{d}[s{j}]"); outs.append(f'[s{j}]')
f.append(''.join(outs)+f"amix=inputs={len(outs)}:normalize=0,apad=whole_dur=30,atrim=0:30[sfx]")
f.append("[0:a]atrim=0:30,volume=0.7[mus]")
f.append("[mus][sfx]amix=inputs=2:normalize=0:weights=1 0.9,afade=t=out:st=29.5:d=0.5[pre]")
f.append("[pre]loudnorm=I=-14:TP=-1.5:LRA=11,volume=-1dB[out]")
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(f),'-map','[out]','-ar','48000','-ac','2','-t','30',A+'mix.wav'],check=True)
r=subprocess.run(['ffmpeg','-i',A+'mix.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
print('\n'.join(l for l in r.splitlines()[-14:] if any(k in l for k in ('I:','Peak','LRA:'))))
