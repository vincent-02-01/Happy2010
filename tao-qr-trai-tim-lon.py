"""QR lớn tạo phần đuôi trái tim, hai cung tròn tạo hai thùy phía trên."""
import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / '.qr-deps'))
from PIL import Image, ImageDraw
import qrcode

URL = sys.argv[1] if len(sys.argv) > 1 else 'https://for-u-virid.vercel.app/'
SIZE, MODULE = 1800, 26
RED = '#b3263e'
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=MODULE, border=1)
qr.add_data(URL)
qr.make(fit=True)
code = qr.make_image(fill_color=RED, back_color='white').convert('RGBA')
side = code.width
code = code.rotate(135, resample=Image.Resampling.NEAREST, expand=True, fillcolor=(0,0,0,0))
cx, cy = SIZE/2, 990
half = side / math.sqrt(2)
radius = side / 2
# Hai hình tròn có đường kính là hai cạnh trên của hình vuông xoay.
# Nửa phía trong được mã QR phủ lên, chỉ còn hai cung lồi ra ngoài.
mask = Image.new('L', (SIZE,SIZE))
md = ImageDraw.Draw(mask)
for sign in [-1,1]:
    x, y = cx + sign*half/2, cy-half/2
    md.ellipse((x-radius,y-radius,x+radius,y+radius),fill=255)
decor = Image.new('RGB',(SIZE,SIZE),'white')
draw = ImageDraw.Draw(decor)
rng = random.Random(20102026)
for row in range(-80,81):
    for col in range(-80,81):
        if rng.random() > .49: continue
        x = cx + (col-row)*MODULE/math.sqrt(2)
        y = cy + (col+row)*MODULE/math.sqrt(2)
        r = MODULE/math.sqrt(2)
        draw.polygon([(x,y-r),(x+r,y),(x,y+r),(x-r,y)],fill=RED)
image = Image.new('RGB',(SIZE,SIZE),'white')
image.paste(decor,(0,0),mask)
image.paste(code,(round(cx-code.width/2),round(cy-code.height/2)),code)
output=Path(__file__).with_name('qr-trai-tim-lon.png')
image.save(output,dpi=(300,300))
print(output)
print(URL)
