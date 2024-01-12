import random
from PIL import Image, ImageDraw
w, h = 400, 400
center = 200

colors = (random.randint(20,60),random.randint(50,100)+4,random.randint(50,100)+19)

canvas =[(0,0),(w,h)]

img = Image.new('RGB',(w,h))
#Canvas
gradient_bg = ImageDraw.Draw(img)
gradient_bg.rectangle(canvas,fill=colors)

# drawing rectangles
for i in range(6,126,6):
    canv_temp =[(i,i),(w-i,h-i)]
    draw_grad = ImageDraw.Draw(img)
    draw_grad.rectangle(canv_temp,fill=(colors[0]+int(i/2),colors[1]+int(i/2),colors[2])) # changed from 181,172, 0
img.show()
img.save('bg.jpg')

