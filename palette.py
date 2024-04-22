### Author: Erik Ring-Walters
### Github: erikringwalters
### Created: April 26, 2023
### Description: A color palette generator created to offer a wide selection of -
### - colors in a texture image, for game assets using low-poly UV editing.

from PIL import Image
from datetime import datetime

# user-adjusted parameters
SIZE=64
MAX=255
LEVELS=4

LEVEL_SIZE=SIZE/LEVELS

w=SIZE
m=MAX
l=LEVEL_SIZE

print("Creating " + str(SIZE) + "px sized palette...")

def normalized(x, min, max):
    return (x-min)/(max-min)*m

def savePng(img, size, levels):
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H:%M:%S")
    fn = "palette" + str(size)
    ## uncomment for more detailed filenames
    # fn = fn + "_" + str(levels) + "L"
    # fn = fn + "_" + date_time
    fn = fn + ".png"
    print("Saving: " + fn)
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

## comment to prevent saving image
savePng(img, SIZE, LEVELS)

## comment to prevent showing image
img.show()

print("Done.")