from PIL import Image
from datetime import datetime
import math

SIZE=256
MAX=255
LEVELS=4
LEVEL_SIZE=SIZE/LEVELS

w=SIZE
m=MAX
l=LEVEL_SIZE



def savePng(img, size, levels):
    now= datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    f = "palette" + str(size) + "W_" + str(levels) + "L_" + date_time + ".png"
    img.convert('RGB').save(f)


#divide max by size for step to next value
d = m/(w-1)

#hue, saturation, brightness
h=s=b=m

img = Image.new(mode="HSV", size=(w, w), color=(h,s,b))

#level factor
lf = (m+1)/LEVELS

#hue factor
hf = 1

#brightness factor
bf = 1

#current level
cl = 1

for i in range(w):
    for j in range(w):
        if(i == w-1):
            #gray values
            b = int(abs((d*j)-m))
            h=s=0
        else:
            # if(i==w-1):
            #     hf=i*d*0.1 
            #     bf=i*d*0.005
            # else: 
            #     hf=1
            #     bf=1
            h = int((d*i)*hf)
            cl = int(j/l)+1
            s = int(cl*lf)-1

            b = int((((j%l)+1)*m/l)*bf)
            
        img.putpixel((i,j), (h,s,b))

# savePng(img, SIZE, LEVELS)

img.show()


