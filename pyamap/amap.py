import sys  
import numpy as np 

reload(sys)  
sys.setdefaultencoding('utf8')

class Amap:

	def __init__(self, showHtml = True):
		self.showHtml = showHtml
		self.width = "100%"
		self.height = "600px"
		self.zoomLevel = 10
		self.js = ""
		self.html = ""
		self.prepareHtml()


	def setJsCode(self, js):
		self.js = js

	def appendJsCode(self, js):
		self.js += js


	def setZoomLevel(self, zoomLevel):
		self.zoomLevel = zoomLevel


	def prepareHtml(self):
		print "hahaha"
		from template import html
		print "html"
		f = open("tmp.html", "w")
		html = html.replace("//for PyAmap//", self.js)
		html = html.replace("//ZOOM_LEVEL//", str(self.zoomLevel))
		html = html.replace("map-height", self.height)
		html = html.replace("map-width", self.width)
		self.html = html
		f.write(html)
		f.close()

	def toImage(self, name="amap.png"):
		import os
		os.system("cd " + os.getcwd())
		os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --screenshot  file://" + os.getcwd() + "/tmp.html")		
		os.system("mv screenshot.png " + name)


	def getHtml(self):
		return self.html


	def _repr_html_(self):
		self.prepareHtml()
		if self.showHtml:
			return self.html
		else:
			return '<img src="amap.png" width="{}" height="{}">'.format(self.width, self.height)    


def main():
	amap = Amap()
	amap.setZoomLevel(15)
	amap.setJsCode("""
			addCircle(116.397428,39.90923);
			addPolygon([
            [116.368904, 39.913423],
            [116.382122, 39.901176],
            [116.387271, 39.912501],
            [116.388258, 39.904600]
 			])
		""")
	import time
	t1 = time.time()
	amap.getPicture()
	print(time.time() - t1)

if __name__ == '__main__':
	main()
