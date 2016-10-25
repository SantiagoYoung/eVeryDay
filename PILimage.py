from PIL import Image, ImageDraw, ImageFont

# first edit
# image = Image.open('car.jpg')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype('Arvo-Regular.ttf', 40)
# draw.text((image.size[0]-20,20), 'hello world',font=font, fill='red')
# image.save()
# image.show()

#second eidt
def show_edit():

	try:
		image = Image.open('car.jpg')
		xsize, ysize = image.size
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('Arvo-Regular.ttf',40)
		draw.text((xsize-20,ysize-200), 'hello world', font=font, fill='red')
		image.save()
		image.show()
	except IOError as e:
		print e
		return False

if __name__ == '__main__':
	show_edit()


'''
# function edition
from PIL import Image,ImageFont,ImageDraw

def draw_badge_number(filePath,badgeNumber=10,fill=(255,0,0),x=0.85,y=0.1,fontPath=None,fontOption=None):

    try:
        image = Image.open(filePath)
        pic = ImageDraw.Draw(image)
        x_size,y_size = image.size
        pic.text([x*x_size,y*y_size],str(badgeNumber),fill=fill,font=fontPath)
        image.save("new_%s"%(filePath))
        input()
        return True        
    except Exception as e:
        print (e)
        return False

if __name__ == '__main__':

'''
# first edit
# image = Image.open('car.jpg')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype('Arvo-Regular.ttf', 40)
# draw.text((image.size[0]-20,20), 'hello world',font=font, fill='red')
# image.save()
# image.show()


'''
#second eidt
def show_edit():

	try:
		image = Image.open('car.jpg')
		xsize, ysize = image.size
		draw = ImageDraw.Draw(image)
		font = ImageFont.truetype('Arvo-Regular.ttf',40)
		draw.text((xsize-20,ysize-200), 'hello world', font=font, fill='red')
		image.save()
		image.show()
	except IOError as e:
		print e
		return False

if __name__ == '__main__':
	show_edit()

'''



# function edition
'''

from PIL import Image,ImageFont,ImageDraw

def draw_badge_number(filePath,*,badgeNumber=10,fill=(255,0,0),x=0.85,y=0.1,fontPath=None,fontOption=None):
    try:
        image = Image.open(filePath)
        pic = ImageDraw.Draw(image)
        x_size,y_size = image.size
        pic.text([x*x_size,y*y_size],str(badgeNumber),fill=fill,font=fontPath)
        image.save("new_%s"%(filePath))
        input()
        return True        
    except Exception as e:
        print (e)
        return False

if __name__ == '__main__':
    draw_badge_number("app.png",badgeNumber=15)


'''