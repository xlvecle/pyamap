#coding: utf-8

class Amap:

	def __init__(self):
		self.zoomLevel = 10
		self.js = ""


	def setJsCode(self, js):
		self.js = js


	def setZoomLevel(self, zoomLevel):
		self.zoomLevel = zoomLevel

	def getPicture(self):
		print "hahaha"
		from template import html
		print "html"
		f = open("tmp.html", "w")
		html = html.replace("//for PyAmap//", self.js)
		html = html.replace("//ZOOM_LEVEL//", str(self.zoomLevel))
		f.write(html)
		f.close()
		import os
		os.system("cd " + os.getcwd())
		os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --disable-gpu --screenshot  file://" + os.getcwd() + "/tmp.html")		
		os.system("mv screenshot.png amap.png")


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
