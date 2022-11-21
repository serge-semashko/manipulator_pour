import math
import numpy
import cv2

img = cv2.imread("2.jpg")
h, w, c = img.shape[:3]
img_bw = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
fin_img = numpy.eye(h - 2, w - 2)
for i in range(1, h - 1):
    for j in range(1, w - 1):
        gx = (img_bw[i + 1][j - 1] + 2 * img_bw[i + 1][j] + img_bw[i + 1][j + 1]) - (img_bw[i - 1][j - 1] + 2 * img_bw[i - 1][j] + img_bw[i - 1][j + 1])
        gy = (img_bw[i - 1][j + 1] + 2 * img_bw[i][j + 1] + img_bw[i + 1][j + 1]) - (img_bw[i - 1][j - 1] + 2 * img_bw[i][j - 1] + img_bw[i + 1][j - 1])
        f = math.sqrt(gx ** 2 + gy ** 2)
        fin_img[i - 1][j - 1] = f

cv2.imwrite("12.jpg", fin_img)

im = cv2.imread('12.jpg')
edges = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(edges, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.imwrite("12_edges.jpg", thresh)
n = len(contours)
print(n)
x = []
y = []
for i in range(n):
    if len(contours[i]) > 100:
        for j in range(len(contours[i])):
            x.append(numpy.split(contours[i][j][0], 2)[0])
            y.append(numpy.split(contours[i][j][0], 2)[1])
        cv2.drawContours(thresh, contours, i, (0, 255, 255), 1, cv2.LINE_AA, hierarchy, 1)
        cv2.imshow("i", thresh)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        sootnx = (max(x) - min(x)) / 4
        sootny = (max(y) - min(y)) / 4
        area = cv2.contourArea(contours[i])
        perimeter = cv2.arcLength(contours[i], True)
        if perimeter != 0:
            sootn = area / perimeter
            if abs(sootn - sootnx) < 5 and abs(sootn - sootny) < 5:
                print(i, "Circle")