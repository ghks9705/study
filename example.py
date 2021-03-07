import cv2

img_color = cv2.imread('Billiard.jpg', cv2.IMREAD_COLOR)

cv2.imshow('Color',img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()