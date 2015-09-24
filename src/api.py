from  PIL  import Image
'''
Calculate a image color flag value and

return the processed image
'''
def Calculate(image):
	# image = image.rotate(180)
	mean = Calculate_Color(image)
	mask_image = Image.new("RGBA",image.size,mean)
	base_image = Image.open("../resource/test1.png").resize(image.size)
	'''
		merge image 
	'''
	result = Image.blend(base_image,image,0.4)
	return result
	
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
	print (r_mean,g_mean,b_mean)
	return (r_mean,g_mean,b_mean)
