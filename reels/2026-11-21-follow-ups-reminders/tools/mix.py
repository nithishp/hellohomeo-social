import subprocess
A='assets/audio/'
VO=[(0.0,2.05,0.12),(2.41,5.15,2.9),(5.55,8.81,7.3),(9.14,12.71,11.6),(13.18,13.94,15.6),(14.22,15.79,16.5),(16.16,17.07,19.4),(17.30,18.28,22.2),(18.61,22.04,25.35)]
SFX=[('tick',t,0.35) for t in (0.1,0.3,0.5,7.65,8.4,9.05,10.05,19.9)]+[('tick',t,0.5) for t in (0.85,1.15)]+[('whoosh',t,0.45) for t in (6.8,11.25,15.2,18.75)]+[('whoosh',21.4,0.3)]+[('chime',10.1,0.4)]+[('pop',t,0.45) for t in (11.95,13.6,15.59,16.44,17.14)]
inp=['-i',A+'vo_take1.mp3','-i',A+'music_local.wav']+sum([['-i',A+f'sfx_{n}.wav'] for n in ('tick','whoosh','chime','pop')],[])
idx={'tick':2,'whoosh':3,'chime':4,'pop':5}
f=[]
for i,(a,b,at) in enumerate(VO):
    a2=max(0,a-0.03); b2=b+0.06; d=int(at*1000)
    f.append(f"[0:a]atrim={a2}:{b2},asetpts=PTS-STARTPTS,afade=t=in:d=0.02,afade=t=out:st={b2-a2-0.05:.3f}:d=0.05,aresample=48000,aformat=channel_layouts=stereo,adelay={d}|{d}[v{i}]")
f.append(''.join(f'[v{i}]' for i in range(len(VO)))+f"amix=inputs={len(VO)}:normalize=0,apad=whole_dur=30,atrim=0:30,asplit=2[vo][vosc]")
cnt={}
for j,(n,t,g) in enumerate(SFX):
    k=idx[n]; cnt[k]=cnt.get(k,0)+1
sp={k:[] for k in idx.values()}
for k,c in cnt.items(): f.append(f"[{k}:a]aresample=48000,aformat=channel_layouts=stereo,asplit={c}"+''.join(f'[x{k}_{i}]' for i in range(c)))
use={k:0 for k in idx.values()}; outs=[]
for j,(n,t,g) in enumerate(SFX):
    k=idx[n]; i=use[k]; use[k]+=1; d=int(t*1000)
    f.append(f"[x{k}_{i}]volume={g},adelay={d}|{d}[s{j}]"); outs.append(f'[s{j}]')
f.append(''.join(outs)+f"amix=inputs={len(outs)}:normalize=0,apad=whole_dur=30,atrim=0:30[sfx]")
f.append("[1:a]atrim=0:30,volume=0.55[mus]")
f.append("[mus][vosc]sidechaincompress=threshold=0.03:ratio=6:attack=20:release=350[duck]")
f.append("[duck][vo][sfx]amix=inputs=3:normalize=0:weights=1 1.25 0.8,afade=t=out:st=29.6:d=0.4[pre]")
f.append("[pre]loudnorm=I=-14:TP=-1.5:LRA=11[out]")
subprocess.run(['ffmpeg','-v','error','-y',*inp,'-filter_complex',';'.join(f),'-map','[out]','-ar','48000','-ac','2','-t','30',A+'mix.wav'],check=True)
r=subprocess.run(['ffmpeg','-i',A+'mix.wav','-af','ebur128=peak=true','-f','null','-'],capture_output=True,text=True).stderr
print('\n'.join(l for l in r.splitlines()[-14:] if any(k in l for k in ('I:','Peak','LRA:'))))
