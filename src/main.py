from api import *
'''
Goble define
'''
Pixel_Byte_Define = 20


def Combines(original_im):
	original_x,original_y = original_im.size
	'''
	new a Image object and initialize
	'''
	small_x = int(original_x/Pixel_Byte_Define)
	small_y = int(original_y/Pixel_Byte_Define)
	wall_img = Image.new("RGB",
						 (
						  small_x*Pixel_Byte_Define,
						  small_y*Pixel_Byte_Define
						  ),
						 "#ffffff")
	for p_x in range(Pixel_Byte_Define):
		for p_y in range(Pixel_Byte_Define):
			current_coord = (
								p_x*small_x,
								p_y*small_y
							 )
			'''
			crop current area
			'''
			small_img = original_im.crop(
										 (
											  current_coord[0],
											  current_coord[1],
											  current_coord[0]+small_x,
											  current_coord[1]+small_y
										  )
										)
			'''
			get a image after Calculate
			'''
			small_img = Calculate(small_img)

			'''
			paste the ok image to current area
			'''
			wall_img.paste(small_img,current_coord)
	return wall_img


def main():
	im = Image.open('../resource/test3.jpg').convert("RGBA")
	im = Combines(im)
	im.show()
	pass


def test():
	im = Image.open('../resource/test2.png')
	# im = im.array(im)
if __name__ == '__main__':
	main()
	# test()
