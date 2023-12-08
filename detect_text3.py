import sys
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
from paddleocr import PaddleOCR
import cv2
from paddleocr import draw_ocr
import numpy as np


def ocr_with_paddleocr(image_path):
    # Initialize PaddleOCR
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Perform OCR on the image
    result = ocr.ocr(image_path, cls=True)
    from PIL import Image
    result = result[0]
    image = Image.open(image_path).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path='./doc/fonts/simfang.ttf')
    im_show = Image.fromarray(im_show)
    im_show.save('result.jpg')

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    ocr_with_paddleocr(image_path)

if __name__ == "__main__":
    main()
