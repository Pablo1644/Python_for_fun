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
# drawing Circles
# r = 40
# for j in range(12):
#     r-=3
#     left_up_point = (center - r,center - r)
#     right_down_point=(center+r,center+r)
#     elipse_shape = (left_up_point,right_down_point)
#     draw_grad.ellipse(elipse_shape,fill=(200+int(4*j),50+j,10+j))

# img.show()

