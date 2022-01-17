import cv2
import time

image = cv2.imread("image0.jpg")
# print(type(image))
# print(image.shape)

# cv2.imshow("Yuv", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# cv2.imwrite("Yuv.png", image)



def takepic():
    video = cv2.VideoCapture(0)
    time.sleep(3)
    dummy,frame=video.read()
    print(dummy)
    cv2.imwrite("Yuv.png", frame)
    cv2.waitKey(0)
    video.release()
    cv2.destroyAllWindows()


takepic()