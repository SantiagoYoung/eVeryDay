# -*- coding: utf-8 -*-
'''
生成随机验证码
'''
import string
strings = string.letters
ascii_letters = string.ascii_letters
import random
import Image, ImageDraw, ImageFilter, ImageFont

letter = ''
myImg = Image.new('RGB', (100, 50), 'white')
draw = ImageDraw.Draw(myImg)
font = ImageFont.truetype("/usr/share/fonts/truetype/AbyssinicaSIL-R.ttf", 20)
# for x in range(20):
#     for y in range(20):
#         draw.point((x*5,y*5), fill=(0,10,0))
        # draw.line((x,y) + (myImg.size[1],myImg.size[0]), fill=20)

for i in range(4):
    random_letter = random.choice(strings)
    print random_letter

    # letter += random_letter
    print draw.text((10+i*25 ,18), str(random_letter), fill='red', font=font)
myImg = myImg.filter(ImageFilter.MinFilter)
myImg.save('hello.jpg', 'JPEG')

















































































