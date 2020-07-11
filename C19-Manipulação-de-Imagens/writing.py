from PIL import Image, ImageDraw, ImageFont
import os

image = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(image)
draw.text((20, 150), 'Hello World!', fill='purple')
fonts_folder = '/usr/share/fonts/truetype/dejavu'
arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'DejaVuSans-Bold.ttf'), 32)
draw.text((100, 150), 'Lorem Ipsum', fill='gray', font=arial_font)
image.save('text.png')

