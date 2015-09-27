import urllib 
import urllib2 
from PIL import Image
import StringIO 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def delay(time):
	for i in range(time):
		for j in range(1000):
			for k in range(500):
				a=100*100

class BingSpider():
	url=["http://cn.bing.com/images/search?pq=%u52a8%u6f2b&sc=8-2&sp=6&sk=IM5&q=%E5%8A%A8%E6%BC%AB%E4%BA%BA%E7%89%A9&qft=+filterui:color2-FGcls_RED&FORM=R5IR8"]
	driver = webdriver.Firefox()
	load_page_length = 1
	def crawl(self):
		self.driver.get(self.url[0])
		self.loadmore(self.load_page_length)
		self.getimage()
		
	def loadmore(self,time):
		for j in range(time):
			next_page = self.driver.find_elements_by_xpath("//a[@id='fbpgbt']")
			for i in range(12):
				next_page[0].send_keys(Keys.PAGE_DOWN)
				delay(20)
			more_page = self.driver.find_elements_by_xpath("//div[@class='mm_seemore']/a[@class='btn_seemore']")
			more_page[0].click()

	def getimage(self):
		images = self.driver.find_elements_by_xpath("//div[@class='imgres']/div/a/img")
		print len(images)
		for img in images[:4]:
			url = img.get_attribute('src')
			print url
			image_data =urllib2.urlopen(url).read()
			img_file = Image.open(StringIO.StringIO(image_data))
			img_file.show()


import urllib 
import urllib2 
def main():
	bSpider = BingSpider()
	bSpider.crawl()
	pass

if __name__ == '__main__':
	main()