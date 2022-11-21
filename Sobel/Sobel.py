import math
import numpy
import cv2

def findCircle(img1, n):
    cv2.imshow(str(n)+' src',img1)
    cv2.imwrite(str(n)+' src.png',img1)
    fin_img = numpy.eye(h - 2, w - 2)
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            gx = (img1[i + 1][j - 1] + 2 * img1[i + 1][j] + img1[i + 1][j + 1]) - (
                        img1[i - 1][j - 1] + 2 * img1[i - 1][j] + img1[i - 1][j + 1])
            gy = (img1[i - 1][j + 1] + 2 * img1[i][j + 1] + img1[i + 1][j + 1]) - (
                        img1[i - 1][j - 1] + 2 * img1[i][j - 1] + img1[i + 1][j - 1])
            f = math.sqrt(gx ** 2 + gy ** 2)
            fin_img[i - 1][j - 1] = f
    name = "12" + str(n) + ".jpg"
    cv2.imshow(str(n)+' sobel ', fin_img)
    im = fin_img.copy()
    cv2.imshow(str(n)+' sobel ', im)
    edges = im.copy()
    cv2.imshow(str(n)+' edged ', edges)
    ret, thresh = cv2.threshold(edges, 127, 255, 0)
    cv2.imshow(str(n)+' thresh ', thresh)
    cv2.waitKey(0)
    return
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    name = "12" + str(n) + "_edges.jpg"
    cv2.imwrite(name, thresh)
    # cv2.imshow("i", img)
    n = len(contours)
    print(n)
    for i in range(n):
        x = []
        y = []
        if len(contours[i]) > 100:
            for j in range(len(contours[i])):
                x.append(numpy.split(contours[i][j][0], 2)[0])
                y.append(numpy.split(contours[i][j][0], 2)[1])
            imgt = cv2.imread("bokal.jpg")
            imgt = cv2.GaussianBlur(imgt, (21, 21), 0)
            cv2.drawContours(imgt, contours, i, (0, 255, 0), 1, cv2.LINE_AA, hierarchy, 1)
            cv2.imshow("i", imgt)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            sootnx = (max(x) - min(x)) / 2
            sootny = (max(y) - min(y)) / 2
            r = max(sootny, sootnx)
            area6 = 3 * math.sqrt(3) / 2 * r ** 2
            # area4 = (r * 2) ** 2
            area = cv2.contourArea(contours[i])
            perimeter = cv2.arcLength(contours[i], True)
            if perimeter != 0 and area != 0:
                print(area / area6)
                # sootn = area / perimeter
                if 1 <= area / area6 <= 1.4:
                    xc = max(x) - r
                    yc = max(y) - r
                    print(i, "Circle", "x =", xc, "y =", yc, "d =", r * 2)
                    return xc, yc, r * 2
                # elif 1 <= area4 / area <= 2:
                #print(i, "Square")

img = cv2.imread("bokal.jpg")
h, w, c = img.shape[:3]
img = cv2.GaussianBlur(img,(21,21),0)
img_hsl = cv2.cvtColor(img, cv2.COLOR_RGB2HLS)
im1= img_hsl[:,:,0]
im2= img_hsl[:,:,1]
im3= img_hsl[:,:,2]
# cv2.imshow("0", im1)
# cv2.imshow("1", im2)
# cv2.imshow("2", im3)
print("First channel")
findCircle(im1, 1)
#print("Second channel")
findCircle(im2, 2)
#print("Third channel")
findCircle(im2, 3)