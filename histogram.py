import cv2
import matplotlib.pyplot as pyplot


def calHistogram(img):
	if len(img.shape) != 2:
		print("wrong image size")
		return None
	histogram = {}
	for i in range(img.shape[0]):
		for j in range(img.shape[1]):
			if histogram.get(img[i][j]) is None:
				histogram[img[i][j]] = 0
			histogram[img[i][j]] += 1
	# print(max(histogram.values()))
	m=max(histogram.values())
	for key in histogram:
		# histogram[key] /= m
		histogram[key] /= img.shape[1]*img.shape[0]
	return histogram


def drawHistoGram(histogram):
	pyplot.figure()
	pyplot.axis([0,256, 0,max(histogram.values())])
	# pyplot.axis([0, 256, 0, 1])
	pyplot.grid(True)
	keys = histogram.keys()
	values = histogram.values()
	pyplot.bar(tuple(keys), tuple(values))
	pyplot.show()


img = cv2.imread("./gry.jpg", 0)
cv2.imshow("img",img)
cv2.waitKey(0)
histogram = calHistogram(img)
drawHistoGram(histogram)
