import os 
import cv2

# read images
image_path = os.path.join("Computer Vision","io","bird.jpg")

img = cv2.imread(image_path)

cv2.imwrite(os.path.join("Computer Vision","io","bird_out.jpg"),img)


cv2.imshow("image",img)
cv2.waitKey(0)