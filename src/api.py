from  PIL  import Image
import os
import random
'''
Calculate a image color flag value and

return the processed image
'''
color_map =	{

}

test_matrix=[
	(9,6),(10,6),
	(9,7),(10,7),(11,7),
	(8,8),(9,8),(10,8),(11,8),(12,8),
	(7,9),(8,9),(9,9),(10,9),(11,9),(12,9),
	(7,10),(8,10),(9,10),(10,10),(11,10),(12,10),
	(7,11),(8,11),(9,11),(10,11),(11,11),(12,11),
	(7,12),(8,12),(9,12),(10,12),(11,12),(12,12),
	(7,13),(8,13),(9,13),(10,13),(11,13),(12,13),(13,13),
	(7,14),(8,14),(9,14),(10,14),(11,14),(12,14),(13,14),
	(7,15),(8,15),(9,15),(10,15),(11,15),(12,15),(13,15),
	(7,16),(8,16),(9,16),(10,16),(11,16),(12,16),(13,16)
]
test_matrix2=[
	(4,3),(5,3),(6,3),(7,3),
	(4,4),(5,4),(6,4),(7,4),
	(8,5),(9,5),(10,5),(11,5),(12,5),
	(7,6),(8,6),(9,6),(10,6),(11,6),(12,6),
	(7,7),(78,7),(9,7),(10,7),(11,7),(12,7),
	(7,11),(8,11),(9,11),(10,11),(11,11),(12,11),
	(7,12),(8,12),(9,12),(10,12),(11,12),(12,12),
	(7,13),(8,13),(9,13),(10,13),(11,13),(12,13),(13,13),
	(7,14),(8,14),(9,14),(10,14),(11,14),(12,14),(13,14),
	(7,15),(8,15),(9,15),(10,15),(11,15),(12,15),(13,15),
	(7,16),(8,16),(9,16),(10,16),(11,16),(12,16),(13,16)
]



def Calculate(image,coord):
	# image = image.rotate(180)
	# mean = Calculate_Color(image)
	color =  get_dominant_color(image)
	print color
	base_image = MatchImage(image)
	'''
		Cheating!merge image with original image
	'''

	if coord in test_matrix2:
		result = Image.blend(base_image,image,0.95)
	else :
		result = Image.blend(base_image,image,0.75)
	return result

'''
match a image which like most
'''

def Rgb2Hsv(rgb):
	h=0
	v=max(rgb)
	s=float((v-min(rgb)))/v
	if rgb[0]>rgb[1] and rgb[0]>rgb[2]:
		h = float((rgb[1]-rgb[2]))/(v-min(rgb))*60		
	elif rgb[1]>rgb[0] and rgb[1]>rgb[2]:
		h = 120 + float((rgb[2]-rgb[0]))/(v-min(rgb))*60
	elif rgb[2]>rgb[0] and rgb[2]>rgb[1]:
		h = 240 + float((rgb[0]-rgb[1]))/(v-min(rgb))*60	
	if h<0:
		h+=360
	return (h,s,v)

def Hus2Color(hsv):
	'''
		is black?
	'''
	if hsv[2]<=45:
		return 'black'
	'''
		is gray or white
	'''
	elif hsv[1]<=45:
		if hsv[2]<=220:
			return 'gray'
		elif 220<hsv[2]:
			return 'white'

	'''
		is red green bule ....?>_<
	'''
	elif 45<hsv[1]:
		if 0<hsv[0]<=15 or 345<hsv[0]<=360:
			return 'red'
		elif 15<hsv[0]<=45:
			return 'orange'
		elif 45<hsv[0]<=75:
			return 'yellow'
		elif 75<hsv[0]<=105:
			return 'green'
		elif 105<hsv[0]<=135:
			return 'green'
		elif 135<hsv[0]<=165:
			return 'teal'
		elif 165<hsv[0]<=195:
			return 'teal'
		elif 195<hsv[0]<=225:
			return 'bule'
		elif 225<hsv[0]<=255:
			return 'bule'
		elif 255<hsv[0]<=285:
			return 'purple'
		elif 285<hsv[0]<=315:
			return 'purple'
		elif 315<hsv[0]<=345:
			return 'pink'

def Sv2Color(s,v):
	pass

def Get_Rgb_max(rgb):
	if rgb[0]>rgb[1] and rgb[0]>rgb[2]:
		return 'r'
	elif rgb[1]>rgb[0] and rgb[1]>rgb[2]:
		return 'g'
	elif rgb[0]>rgb[1] and rgb[2]>rgb[1]:
		return 'b'

def MatchImage(image):
	'''
		now is just a test
	'''
	return getRandomImage('../resource/img.bing.com/lufei').resize(image.size)
	 

def Calculate_Color(image):
	r_mean=0
	g_mean=0
	b_mean=0
	x,y = image.size
	for i in range(x):
		for j in range(y):
			rgb = image.getpixel((i,j))
			r_mean+=int(rgb[0])
			g_mean+=int(rgb[0])
			b_mean+=int(rgb[0])
	r_mean/=x*y
	g_mean/=x*y
	b_mean/=x*y
	return (r_mean,g_mean,b_mean)

def getRandomImage(dir_url):
	colors =  os.listdir(dir_url)
	colors_number = random.randrange(len(colors))
	pic_dri = os.path.join(dir_url,colors[colors_number])
	imgs_dri = os.listdir(pic_dri)
	imgs_number = random.randrange(len(imgs_dri))
	img_dri = os.path.join(pic_dri,imgs_dri[imgs_number])
	print img_dri
	return Image.open(img_dri).convert("RGBA")


import colorsys
def get_dominant_color(image):

    image = image.convert('RGBA')
    image.thumbnail((200, 200))
    max_score = None
    dominant_color = None
    for count, (r, g, b, a) in image.getcolors(image.size[0] * image.size[1]):
        #tiao guo hei se
        if a == 0:
            continue
        saturation = colorsys.rgb_to_hsv(r / 255.0, g / 255.0, b / 255.0)[1]
        # y = min(abs(r * 2104 + g * 4130 + b * 802 + 4096 + 131072) >> 13, 235)
        # y = (y - 16.0) / (235 - 16)
        # #hu lue gao liang se
        # if y > 0.9:
        #     continue
        score = (saturation + 0.1) * count
        if score > max_score:
            max_score = score
            dominant_color = (r, g, b)
    return dominant_color


# getRandomImage('../resource/img.bing.com/lufei')
print Rgb2Hsv((255,0,11))