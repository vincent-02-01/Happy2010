"""In thiệp 20/10 có mã QR thật + viền trái tim đỏ.

Cài thư viện: pip install pillow qrcode[pil]
Chạy: python tao-qr.py "https://ten-trang-web-cua-ban.netlify.app"
"""
import math
import os
import random
import sys
from PIL import Image, ImageDraw, ImageFont
import qrcode

WIDTH, HEIGHT = 1400, 1800
BG = (255, 253, 252)
RED = (200, 51, 72)
INK = (64, 55, 59)


def font(size, bold=False):
    candidates = [
        'C:/Windows/Fonts/seguisb.ttf' if bold else 'C:/Windows/Fonts/segoeui.ttf',
        'C:/Windows/Fonts/arialbd.ttf' if bold else 'C:/Windows/Fonts/arial.ttf',
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf' if bold else '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    ]
    for path in candidates:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def centered(draw, y, value, font_obj, color):
    bbox = draw.textbbox((0, 0), value, font=font_obj)
    draw.text(((WIDTH-(bbox[2]-bbox[0]))/2, y), value, font=font_obj, fill=color)


def heart_point(theta, scale=27, center=(700, 945)):
    x = 16*math.sin(theta)**3
    y = -(13*math.cos(theta)-5*math.cos(2*theta)-2*math.cos(3*theta)-math.cos(4*theta))
    return (center[0]+x*scale, center[1]+y*scale)


def make_card(url, output='thiep-qr-20-10.png'):
    if not url.startswith(('http://', 'https://')):
        raise ValueError('Đường dẫn cần bắt đầu bằng https:// hoặc http://')
    image = Image.new('RGB', (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(image)
    centered(draw, 145, 'Mừng ngày Phụ nữ Việt Nam', font(51, True), INK)
    centered(draw, 215, '20 tháng 10', font(47), INK)

    random.seed(20261020)
    # Vẽ outline trái tim bằng những ký hiệu nhỏ, không che vùng quét mã.
    for i in range(430):
        theta = (i+random.random()*.5)*2*math.pi/430
        x,y = heart_point(theta,scale=31)
        x += random.uniform(-14,14)
        y += random.uniform(-12,12)
        r = random.randint(3,11)
        color = RED if random.random()<.6 else (225, 88, 109)
        if random.random()<.32:
            draw.rectangle((x-r,y-r,x+r,y+r), fill=color)
        else:
            draw.ellipse((x-r,y-r,x+r,y+r),fill=color)

    for _ in range(750):
        theta=random.random()*math.tau
        # Decorative scatter around heart boundary only.
        x,y=heart_point(theta,scale=random.uniform(25,32))
        r=random.randrange(2,6)
        draw.rectangle((x-r,y-r,x+r,y+r), fill=(240, 135, 154))

    # QR code tối trên nền trắng, giữ viền trắng (quiet zone) để quét đáng tin cậy.
    qr=qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=12,border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr_img=qr.make_image(fill_color='#b32f4e',back_color='white').convert('RGB')
    qr_size=510
    qr_img=qr_img.resize((qr_size,qr_size), Image.Resampling.NEAREST)
    image.paste(qr_img,((WIDTH-qr_size)//2,945-qr_size//2))
    draw=ImageDraw.Draw(image)
    centered(draw, 1480, 'Quét mã để mở điều bất ngờ', font(31), INK)
    centered(draw, 1560, '20.10.2026', font(46,True),RED)
    image.save(output)
    print(f'Đã tạo: {os.path.abspath(output)}')
    print(f'Địa chỉ gắn với QR: {url}')


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv)>1 else input('Dán đường dẫn trang web 20/10 đã công khai: ').strip()
    make_card(url)
