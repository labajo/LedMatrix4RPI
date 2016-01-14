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


def generate_image_from_text(text, r, g, b):
    font = ImageFont.truetype("./FreeSans.ttf", 15)
    print(text)
    width, ignore = font.getsize(text)
    print(width)

    im = Image.new("RGB", (width + 30, 16), "black")
    draw = ImageDraw.Draw(im)

    print("t=" + text + " " + str((r, g, b)))
    draw.text((0, -3), text, (r, g, b), font=font)
    im.save("test.ppm")
    os.system("../rpi-rgb-led-matrix/led-matrix -t 20 -D 1 -c 3 -r 16 test.ppm")



