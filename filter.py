import cv2

def applyfilter(file, f):
	im = cv2.imread(file)
	Cim = cv2.imread(file)
	divider = 1
	if f=='directional':
		Cf=[[-1, 0, 1],[-1, 0, 1],[-1, 0, 1]]
	elif f=='mean':
		Cf=[[1, 1, 1],[1, 1, 1],[1, 1, 1]]
		divider = 9
	elif f=='highpass':
		Cf=[[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]]
		divider = 9
	elif f=='laplacian':
		Cf=[[0, -1, 0],[-1, 4, -1],[0, -1, 0]]
	#applying filter
	for i in range(len(Cim)):
		for j in range(len(Cim[0])):
			r = 0
			g = 0 
			b = 0
			for x in range(len(Cf)):
				for y in range(len(Cf[0])):
					try:
						r += im[i+x-1][j+y-1][0]*Cf[x][y]
						g += im[i+x-1][j+y-1][1]*Cf[x][y]
						b += im[i+x-1][j+y-1][2]*Cf[x][y]
					except:
						pass
			Cim[i][j][0]= min(max(r/divider,0),255)
			Cim[i][j][1]= min(max(g/divider,0),255)
			Cim[i][j][2]= min(max(b/divider,0),255)
	cv2.imwrite(file[:-4] + f + ".png", Cim)

def main():
	filepath = raw_input('filepath : ')
	applyfilter(filepath, 'directional')
	applyfilter(filepath, 'mean')
	applyfilter(filepath, 'highpass')
	applyfilter(filepath, 'laplacian')
main()