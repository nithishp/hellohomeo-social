import subprocess
src='vo_take1.mp3'
# (start,end) in source, placement in reel (at 1.08x)
segs=[(0.0,1.68,2.05),(1.98,3.86,3.62),(4.22,5.47,5.75),(5.84,9.04,6.92),(9.40,12.69,10.02),(12.88,14.86,13.10),(15.22,19.35,14.95),(19.56,22.29,19.30),(22.60,23.44,23.40),(23.72,27.20,24.32),(27.50,28.90,27.66)]
inputs=[];fil=[]
for i,(a,b,at) in enumerate(segs):
    fil.append(f"[0:a]atrim={a}:{b},asetpts=PTS-STARTPTS,atempo=1.08,afade=t=in:d=0.02,afade=t=out:st={(b-a)/1.08-0.04:.3f}:d=0.04,adelay={int(at*1000)}|{int(at*1000)}[s{i}]")
fil.append(''.join(f'[s{i}]' for i in range(len(segs)))+f"amix=inputs={len(segs)}:normalize=0,apad=whole_dur=30,atrim=0:30[out]")
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-filter_complex',';'.join(fil),'-map','[out]','-ar','48000','-ac','2','vo_placed.wav'],check=True)
for i,(a,b,at) in enumerate(segs): print(i, f"{at:.2f}-{at+(b-a)/1.08:.2f}")
