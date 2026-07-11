from PIL import Image, ImageDraw, ImageFont
for size in (192,512):
    im=Image.new('RGB',(size,size),'#07070b')
    d=ImageDraw.Draw(im)
    try: f=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Black.ttf',int(size*.42))
    except: f=ImageFont.load_default()
    d.rounded_rectangle([size*.06,size*.06,size*.94,size*.94],radius=size*.18,outline='#ff5c47',width=max(3,size//48))
    bb=d.textbbox((0,0),'PN',font=f)
    d.text(((size-bb[2]+bb[0])/2-bb[0],(size-bb[3]+bb[1])/2-bb[1]),'PN',font=f,fill='#f2efe6')
    im.save(f'assets/icon-{size}.png')
print('icons done')
