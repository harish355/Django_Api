import cv2

img = cv2.imread('../Image.png')

# Failing at unclear or low pixels images
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
faces = faceCascade.detectMultiScale(
        img,
        scaleFactor=1.3,
        minNeighbors=3,
        minSize=(30, 30)
)

cv2.waitKey(0)
cv2.destroyAllWindows()
