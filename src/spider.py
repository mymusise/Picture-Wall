import urllib 
import urllib2 
from PIL import Image
import StringIO 
import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import image_url

def delay(time):
	for i in range(time):
		for j in range(1000):
			for k in range(500):
				a=100*100

def getRandomName(name_length):
	return string.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], name_length)).replace(' ','')

class BingSpider():
	urls=[
			image_url.cartoon['purple'],
			image_url.cartoon['pink'],
			image_url.cartoon['brown'],
			image_url.cartoon['black'],
			image_url.cartoon['white'],
			image_url.cartoon['grey']
		]
	driver = webdriver.Firefox()
	load_page_length = 2
	def crawl(self):
		for url in self.urls:
			self.driver.get(url)
			self.loadmore(self.load_page_length)
			self.getimage()
		
	def loadmore(self,time):
		for j in range(time):
			next_page = self.driver.find_elements_by_xpath("//a[@id='fbpgbt']")
			for i in range(15):
				next_page[0].send_keys(Keys.PAGE_DOWN)
				delay(20)
			more_page = self.driver.find_elements_by_xpath("//div[@class='mm_seemore']/a[@class='btn_seemore']")
			# more_page[0].click()

	def getimage(self):
		images = self.driver.find_elements_by_xpath("//div[@class='imgres']/div/a/img")
		print len(images)
		for img in images:
			url = img.get_attribute('src')
			print url
			try:
				image_data =urllib2.urlopen(url).read()
				img_file = Image.open(StringIO.StringIO(image_data))
				url = self.driver.current_url
				color = url[url.find("FGcls_")+6:url.find("&",url.find("FGcls_"))].lower()
				img_file.save('../resource/img.bing.com/cartoon/'+color+'/'+getRandomName(15)+'.jpg')
			except:
				pass


import urllib 
import urllib2 
def main():
	bSpider = BingSpider()
	bSpider.crawl()
	pass

if __name__ == '__main__':
	main()