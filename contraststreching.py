import cv2
import math
import numpy as np
from matplotlib import pyplot as plt
def stats(image):
	sum = 0
	sumquad = 0
	max = 0
	min = 255
	len = 0
	for a in image:
		for i in a:
			sum += i
			sumquad += i**2
			if i>max:
				max = i
			if i<min:
				min = i
			len+=1
	sd = math.sqrt((sumquad*len-(sum)**2)/(len*(len-1)))
	average = sum/len
	print "a. rara-rata pixel  : " + str(average)
	print "b. max nilai pixel : " + str(max)
	print "   min nilai pixel : " + str(min)
	print "c. standar deviasi : " + str(sd)

def histogram(image):
	hist = np.zeros(256)
	#hitung array histogram
	for a in image:
		for i in a:
			hist[i] += 1
	#print hist
	#hist = cv2.calcHist([image], [0], None, [256], [0,256])
	#plot histogram
	#plt.plot(hist)
	#plt.xlim([0,256])
	#plt.show()
	return hist

def histEq(image):
	h = histogram(image)
	#count probs
	c = 0
	for i in range(len(h)):
		h[i] = h[i]/(len(image)*len(image[0]))
		c += h[i]
		h[i] = int(c*255)
	#count cumulative

	for i in range(len(image)):
		for j in range(len(image[0])):
			image[i][j] = h[image[i][j]]
	cv2.imshow('hasil', image)

def main():
	filepath = "lena_low.png"
	im = cv2.imread(filepath, 0)
	imasli = im
	#show image asli & statistik
	cv2.imshow('asli', imasli)
	print "Statistik pixel sebelum :"
	stats(imasli)
	histogram(imasli)
	histEq(imasli)
	equ = cv2.equalizeHist(imasli)
	cv2.imshow('hasilequ', equ)
	#contrast strech
	#tentukan s1, s2, r1, r2
	#pengaturan parameter r1,s1,r2,s2
	s1 = 0
	r1 = 1
	s2 = 255
	r2 = 252

	for i in range(len(im)):
		for x in range(len(im[i])):
			r = im[i][x]
			if r<=r1:
				im[i][x] = s1/r1*r
			elif r>=r2:
				im[i][x] = (((255-s2)/(255-r2))*(r-r2))+s2
			else :
				im[i][x] = (((s2-s1)/(r2-r1))*(r-r1))+s1

	#statistik
	print "Statistik pixel sesudah :"
	stats(im)

	#display image
	cv2.imshow('hasil',im)

	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()