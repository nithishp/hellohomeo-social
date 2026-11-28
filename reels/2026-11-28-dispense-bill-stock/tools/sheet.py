import sys,glob,os
from PIL import Image, ImageDraw
d=sys.argv[1]; out=sys.argv[2]; cols=int(sys.argv[3]) if len(sys.argv)>3 else 4
fs=sorted(glob.glob(d+'/*.png'), key=lambda p: float(os.path.basename(p)[1:-4]) if os.path.basename(p)[0]=='t' else 0)
w,h=360,640; rows=(len(fs)+cols-1)//cols
S=Image.new('RGB',(cols*w+(cols+1)*10,rows*(h+40)+10),(30,30,30)); D=ImageDraw.Draw(S)
for i,f in enumerate(fs):
    im=Image.open(f).convert('RGBA'); bg=Image.new('RGBA',im.size,(7,12,31,255)); bg.alpha_composite(im)
    x=10+(i%cols)*(w+10); y=10+(i//cols)*(h+40); S.paste(bg.convert('RGB').resize((w,h)),(x,y)); D.text((x,y+h+5),os.path.basename(f),fill=(255,255,255))
S.save(out)
