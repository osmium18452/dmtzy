import cv2
import numpy as np
import matplotlib.pyplot as pyplot
from histogram import calHistogram

image = cv2.imread("./orange.jpg", 0)
# print(image.shape)

lut = np.zeros(256, dtype=image.dtype)  # 创建空的查找表

hist, bins = np.histogram(image.flatten(), 256, [0, 256])
bb=np.arange(0,256,1,int)
pyplot.axis([0,256,0,max(hist)])
pyplot.grid(True)
pyplot.bar(bb,hist)
pyplot.show()
# print(type(bins))
cdf = hist.cumsum()  # 计算累积直方图
cdf_m = np.ma.masked_equal(cdf, 0)  # 除去直方图中的0值
print(cdf_m)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())  # 等同于前面介绍的lut[i] = int(255.0 *p[i])公式
cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # 将掩模处理掉的元素补为0
print(cdf)
# 计算
result2 = cdf[image]
result = cv2.LUT(image, cdf)

hist, bins = np.histogram(result.flatten(), 256, [0, 256])
bb=np.arange(0,256,1,int)
pyplot.axis([0,256,0,max(hist)])
pyplot.grid(True)
pyplot.bar(bb,hist)
pyplot.show()

hist, bins = np.histogram(result2.flatten(), 256, [0, 256])
bb=np.arange(0,256,1,int)
pyplot.axis([0,256,0,max(hist)])
pyplot.grid(True)
pyplot.bar(bb,hist)
pyplot.show()

cv2.imshow("OpenCVLUT", result)
# cv2.waitKey(0)
cv2.imshow("NumPyLUT", result2)
cv2.waitKey(0)
# cv2.destroyAllWindows()