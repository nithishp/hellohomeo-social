import sys,subprocess,glob
from PIL import Image
W='/work/reel/2026-W46-scribe-case-sheet'
stdir=sys.argv[1]; out=sys.argv[2]
def base(t):
    if 2.0<=t<5.6: c,o='A',0.3+(t-2.0)
    elif 20.3<=t<23.2: c,o='B2',1.9+(t-20.3)
    else: return Image.new('RGBA',(1080,1920),(7,12,31,255))
    f=f'/tmp/b_{c}_{o:.2f}.png'
    subprocess.run(['ffmpeg','-v','error','-y','-ss',str(o),'-i',f'{W}/assets/clips/{c}.mp4','-frames:v','1','-vf','scale=1080:1920',f],check=True)
    return Image.open(f).convert('RGBA')
fs=sorted(glob.glob(stdir+'/t*.png'),key=lambda s:float(s.split('/t')[-1][:-4]))
th=[]
for f in fs:
    t=float(f.split('/t')[-1][:-4]); b=base(t); b.alpha_composite(Image.open(f).convert('RGBA')); b=b.convert('RGB'); b.save(f.replace('/t','/c_t')); th.append(b.resize((270,480)))
cols=6; rows=(len(th)+cols-1)//cols
sheet=Image.new('RGB',(cols*270,rows*480),(20,20,20))
for i,im in enumerate(th): sheet.paste(im,((i%cols)*270,(i//cols)*480))
sheet.save(out)
