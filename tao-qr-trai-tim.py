"""Tạo QR trái tim: python tao-qr-trai-tim.py [URL]. Cần pillow, qrcode."""
import math
import random
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / '.qr-deps'))
from PIL import Image, ImageDraw
import qrcode

URL = sys.argv[1] if len(sys.argv) > 1 else 'https://for-u-virid.vercel.app/'
SIZE = 1600
RED = '#b3263e'
image = Image.new('RGB', (SIZE, SIZE), 'white')
mask = Image.new('L', image.size)
points = []
for i in range(1000):
    t = i * math.tau / 1000
    points.append((800 + 43 * 16 * math.sin(t)**3,
                   720 - 43 * (13*math.cos(t)-5*math.cos(2*t)-2*math.cos(3*t)-math.cos(4*t))))
ImageDraw.Draw(mask).polygon(points, fill=255)
# Các ô trang trí cùng góc 45 độ với mã thật, nằm trong hình trái tim.
decor = Image.new('RGB', image.size, 'white')
draw = ImageDraw.Draw(decor)
rng = random.Random(20102026)
module = 16
root2 = math.sqrt(2)
for row in range(-80, 81):
    for col in range(-80, 81):
        if rng.random() > .51:
            continue
        x = 800 + (col-row)*module/root2
        y = 770 + (col+row)*module/root2
        r = module/root2
        draw.polygon([(x,y-r),(x+r,y),(x,y+r),(x-r,y)], fill=RED)
image.paste(decor, (0,0), mask)
# Giữ nguyên toàn bộ dữ liệu QR và quiet zone 4 ô, chỉ xoay cả mã.
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=module, border=4)
qr.add_data(URL)
qr.make(fit=True)
code = qr.make_image(fill_color=RED, back_color='white').convert('RGBA')
code = code.rotate(135, resample=Image.Resampling.NEAREST, expand=True, fillcolor=(0,0,0,0))
image.paste(code, ((SIZE-code.width)//2, 770-code.height//2), code)
output = Path(__file__).with_name('qr-trai-tim.png')
image.save(output, dpi=(300,300))
print(output)
print(URL)
