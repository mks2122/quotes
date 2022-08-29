import random
rom PIL import Image,ImageDraw,ImageFont

obj=open('inspire.txt','rb')
handle=obj.read()

words=handle.splitlines()

quote =str(random.choice(words),'utf-8')
obj.close()



myf=ImageFont.truetype('arial',size=22)
image = Image.new(mode='RGB',size=(1920,1080),color='black')
t= ImageDraw.Draw(image)
t.text((0,0),quote,fill='white',align='center',font=myf)
image.show()


