import cv2
import numpy as np
import matplotlib.pyplot as pyplot

image = cv2.imread("orange.jpg", 0)
lut = np.zeros(256, dtype=image.dtype)  # 创建空的查找表
hist = cv2.calcHist([image],  # 计算图像的直方图
					[0],  # 使用的通道
					None,  # 没有使用mask
					[256],  # it is a 1D histogram
					[0.0, 255.0])

minBinNo, maxBinNo = 0, 255

# 计算从左起第一个不为0的直方图柱的位置
print(hist)
for binNo, binValue in enumerate(hist):
	if binValue != 0:
		minBinNo = binNo
		break
# 计算从右起第一个不为0的直方图柱的位置
for binNo, binValue in enumerate(reversed(hist)):
	if binValue != 0:
		maxBinNo = 255 - binNo
		break

print(minBinNo, " ", maxBinNo)

# 生成查找表，方法来自参考文献1第四章第2节
for i, v in enumerate(lut):
	if i < minBinNo:
		lut[i] = 0
	elif i > maxBinNo:
		lut[i] = 255
	else:
		lut[i] = int(255.0 * (i - minBinNo) / (maxBinNo - minBinNo) + 0.5)

# 计算
print(lut)
# result = cv2.LUT(image, lut)
result = lut[image]

hist, bins = np.histogram(result.flatten(), 256, [0, 256])
bb = np.arange(0, 256, 1, int)
pyplot.axis([0, 256, 0, max(hist)])
pyplot.grid(True)
pyplot.bar(bb, hist)
pyplot.show()

hist, bins = np.histogram(image.flatten(), 256, [0, 256])
bb = np.arange(0, 256, 1, int)
pyplot.axis([0, 256, 0, max(hist)])
pyplot.grid(True)
pyplot.bar(bb, hist)
pyplot.show()

cv2.imshow("origin", image)
cv2.imshow("Result", result)
# cv2.imwrite("LutImage.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
