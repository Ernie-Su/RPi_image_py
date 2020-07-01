import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i1', '--image1', required=True, help='first image')
ap.add_argument('-i2', '--image2', required=True, help='second image')
args = vars(ap.parse_args())

img1 = cv2.imread(args['image1'])
img2 = cv2.imread(args['image2'])

#feature = cv2.xfeatures2d.SIFT_create()
feature = cv2.xfeatures2d.SURF_create()
kp1, des1 = feature.detectAndCompute(img1, None)
kp2, des2 = feature.detectAndCompute(img2, None)

#use Brute Force algorithm to match every feature on two images
#k=2 in knnMatch() means every feature point on image1 will have two feature
#points on image2
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

#matches[] has two elements of distance of two feature points following  above
#choose the shorter distance for better answer and put it in good[]
#0.55 is a parameter for filter, lower is better
good = []
for m, n in matches:
    if m.distance < 0.55*n.distance:
        good.append(m)
print('Matching points :{}'.format(len(good)))

img3 = cv2.drawMatchesKnn(
        img1, kp1, img2, kp2, [good], outImg=None, 
        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS
)
img3 = cv2.resize(img3, (1024, 788))
cv2.imshow('image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()


