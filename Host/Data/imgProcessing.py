import cv2

gray = cv2.imread('img/flower.jpg', 0)
cv2.imwrite('img/out.jpg', gray)

# cv2.imshow('cv2Window', gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()