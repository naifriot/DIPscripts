import cv2
import math
def sobel(file):
	Cim = cv2.imread(file, 0)
	print Cim
	im = cv2.imread(file, 0)
	Vw=[[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]]
	Hw=[[-1, -2, -1],[0, 0, 0],[1, 2, 1]]
	#applying filter
	Gx = 0
	Gy = 0
	for i in range(len(Cim)):
		for j in range(len(Cim[0])):
			v = 0
			h = 0
			for x in range(len(Vw)):
				for y in range(len(Vw[0])):
					try:
						v += im[i+x-1][j+y-1]*Vw[x][y]
						h += im[i+x-1][j+y-1]*Hw[x][y]
					except:
						pass
			Gx= min(max(h,0),255)
			Gy= min(max(v,0), 255)
			Cim[i][j] = math.sqrt((Gx**2)+(Gy**2))
			print Cim[i][j]
	print Cim
	cv2.imwrite('aw.png', Cim)

def main():
	filepath = raw_input('filepath : ')
	sobel(filepath)
	
main()