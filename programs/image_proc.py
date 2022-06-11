import cv2
import numpy
print('Package imported')

# Read an Image
# img = cv2.imread('E:/Github/CMS SVIT/cmsapp/assets/developer/n3.jpeg')
# greyScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# scale_percent = 50 # percent of original size
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# dim = (width, height)
# greyScale = cv2.resize(greyScale,dim,interpolation=cv2.INTER_AREA)
# cv2.imshow('Just an image', greyScale);
# cv2.waitKey(0)


class ImgProc:
    def __init__(self, uri: str) -> None:
        super().__init__()
        self.img = cv2.imread(uri)

    def __str__(self) -> str:
        return 'Image Proc'

    def show_image(self) -> None:
        cv2.imshow('Just an image', self.img)
        cv2.waitKey(0)
        # print('Hello World')
