import cv2


def play():
    camera = cv2.VideoCapture(0)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    camera.set(cv2.CAP_PROP_BRIGHTNESS, 150)

    while True:
        success, img = camera.read()
        print(img.shape)
        imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        imgGreyBlur = cv2.GaussianBlur(imgGrey, (17, 17), 0)
        cannyImage = cv2.Canny(imgGrey, 75, 75)
        cv2.imshow('video', imgGrey)
        cv2.imshow('video blur', imgGreyBlur)
        cv2.imshow('video Canny', cannyImage)
        if cv2.waitKey(1) & 0xff == ord('q'):
            camera.release()
            break
