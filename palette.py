from PIL import Image
from datetime import datetime
import os
import math

SIZE=64
MAX=255
LEVELS=4
LEVEL_SIZE=SIZE/LEVELS

w=SIZE
m=MAX
l=LEVEL_SIZE

def normalized(x, min, max):
    return (x-min)/(max-min)*m

def savePng(img, size, levels):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H,%M,%S")
    fn = "palette" + str(size) + "W_" + str(levels) + "L_" + date_time + ".png"

    img.convert('RGB').save(fn)


#divide max by size for step to next value
d = m/(w-1)

#hue, saturation, brightness
h=s=b=m

img = Image.new(mode="HSV", size=(w, w), color=(h,s,b))

#level factor
lf = (m+1)/LEVELS

#minimum brightness
mb = w/2

#current level
cl = 1

for i in range(w):
    for j in range(w):
        if(i == w-1):
            #gray values
            b = int(abs((d*j)-m))
            h=s=0
        else:
            h = int((d*i))
            cl = int(j/l)+1
            s = int(cl*lf)-1
            b = int((((j%l)+1)*m/l))
            b = int(normalized(b, -mb, m))
            
        img.putpixel((i,j), (h,s,b))

savePng(img, SIZE, LEVELS)

img.show()


