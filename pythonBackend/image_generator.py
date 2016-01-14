'''
(c) Copyright 2013 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''


import os
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

text = (("Raspberry Pi ", (255, 0, 0)), ("and ", (0, 255, 0)), ("Adafruit", (0, 0, 255)))


font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf", 16)
all_text = ""
for text_color_pair in text:
    t = text_color_pair[0]
    all_text = all_text + t

print(all_text)
width, ignore = font.getsize(all_text)
print(width)


im = Image.new("RGB", (width + 30, 16), "black")
draw = ImageDraw.Draw(im)

x = 0
for text_color_pair in text:
    t = text_color_pair[0]
    c = text_color_pair[1]
    print("t=" + t + " " + str(c) + " " + str(x))
    draw.text((x, 0), t, c, font=font)
    x = x + font.getsize(t)[0]

im.save("test.ppm")

# os.system("./led-matrix 1 test.ppm")
