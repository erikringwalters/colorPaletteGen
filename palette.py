from PIL import Image
from datetime import datetime

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

# minimum brightness
mb = w/2

# color value steps between pixels
d = m/(w-1)

# hue, saturation, brightness
h=s=b=0

# level factor
lf = (m+1)/LEVELS

# current level
cl = 1

img = Image.new(mode="HSV", size=(w, w), color=(h,s,b))

for i in range(w):
    for j in range(w):
        # if final column
        if(i == w-1):
            # gray values
            b = int(abs((d*j)-m))
            h=s=0
        # every other column
        else:
            # color values
            h = int((d*i))
            cl = int(j/l)+1
            s = int(cl*lf)-1
            bx = int((((j%l)+1)*m/l))
            b = int(normalized(bx, -mb, m))
            
        img.putpixel((i,j), (h,s,b))

savePng(img, SIZE, LEVELS)

img.show()