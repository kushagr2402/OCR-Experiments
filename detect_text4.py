import cv2
import easyocr
import argparse
from textfusenet import TextFuseNetDetector

def detect_and_extract_text(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Initialize TextFuseNet detector
    textfusenet_detector = TextFuseNetDetector()

    # Detect text regions
    text_regions = textfusenet_detector.detect(image)

    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    extracted_texts = []

    # Process each detected text region
    for region in text_regions:
        # Extract text region from the image
        x, y, w, h = region
        text_region = image[y:y+h, x:x+w]

        # Use EasyOCR to recognize text
        result = reader.readtext(text_region)

        # Extract text from the result
        text = " ".join([r[1] for r in result])
        extracted_texts.append(text)

    return extracted_texts

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Text Detection and Extraction")
    parser.add_argument("image_path", help="Path to the image file")
    args = parser.parse_args()

    # Perform text detection and extraction
    texts = detect_and_extract_text(args.image_path)
    print(texts)

if __name__ == "__main__":
    main()
