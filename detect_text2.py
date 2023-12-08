import easyocr
import matplotlib.pyplot as plt
import sys
from PIL import Image, ImageDraw

def ocr_with_bounding_boxes(image_path):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Read the image
    image = Image.open(image_path)

    # Perform OCR
    results = reader.readtext(image_path)

    # Draw bounding boxes and print detected text and bounding box
    draw = ImageDraw.Draw(image)
    for (bbox, text, prob) in results:
        # bbox is a list of tuples (x, y) of the corners of the bounding box
        # Formatting bbox for ImageDraw.rectangle: [x1, y1, x2, y2]
        x1, y1 = bbox[0][0], bbox[0][1]  # Top-left corner
        x2, y2 = bbox[2][0], bbox[2][1]  # Bottom-right corner
        draw.rectangle([x1, y1, x2, y2], outline='red')
        print(f"Detected text: '{text}' with bounding box: {bbox}")

    # Display the image with bounding boxes
    plt.imshow(image)
    plt.title("Detected Text with Bounding Boxes")
    plt.show()

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    ocr_with_bounding_boxes(image_path)

if __name__ == "__main__":
    main()
