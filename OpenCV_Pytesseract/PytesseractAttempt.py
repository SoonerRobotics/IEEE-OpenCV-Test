import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"


def main():
    # list of letters we are looking for
    letters = ['A', 'B', 'C', 'D', 'E', 'F']
    original = cv2.imread('A_Testing_270.png', 0)
    # binary thresh it at value 100. It is now a black and white image
    # ret, original = cv2.threshold(original, 100, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(original, config='--psm 10')
    while text not in letters:
        # if it does not recognize the letter it will rotate the image
        original = rotate(original)
        text = pytesseract.image_to_string(original, config='--psm 10')

    print(text)


def rotate(image):
    # get the image height, width
    (h, w) = image.shape[:2]

    # calculate the center of the image
    center = (w/2, h/2)

    scale = 1.0

    # perform the counter clockwise rotation holding at the center
    m = cv2.getRotationMatrix2D(center, 90, scale)
    rotated90 = cv2.warpAffine(image, m, (w, h))

    return rotated90


if __name__ == "__main__":
    main()


