import cv2

# Capture from the camera
cam = cv2.VideoCapture(0)
cv2.namedWindow("Capture")

while True:
    ret, frame = cam.read()
    if not ret:
        print("Failed to grab frame")
        break
    cv2.imshow("Capture", frame)
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        break
    elif k%256 == 32:
        # SPACE pressed, capture image
        img_name = "./Image.png"
        cv2.imwrite(img_name, frame)
        break

# Release the camera 
cam.release()
cv2.destroyAllWindows()