import sys
import pytesseract
from PIL import Image, ImageDraw

def draw_bounding_boxes(image_path):
    # Open the image using PIL
    image = Image.open(image_path)

    # Use Tesseract to detect text and their bounding boxes
    d = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)

    # Draw bounding boxes on the image and print details
    draw = ImageDraw.Draw(image)
    box_count = 0
    for i in range(len(d['level'])):
        if d['text'][i].strip():  # Check if there is text in the box
            box_count += 1
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            draw.rectangle([x, y, x + w, y + h], outline='red')

            # Print bounding box coordinates and detected text
            #print(f"Box {box_count}: ({x}, {y}, {x + w}, {y + h}) - Text: '{d['text'][i]}")

    # Display or save the image with bounding boxes
    image.show()  # or image.save('output_image_with_boxes.jpg')
    
    return box_count

def main():
    # Check if an image path is provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script.py path_to_image")
        sys.exit(1)

    # Get the image path from the command-line argument
    image_path = sys.argv[1]

    # Draw bounding boxes and get the count
    box_count = draw_bounding_boxes(image_path)
    
    # Print total number of bounding boxes
    print(f"Total number of bounding boxes detected: {box_count}")

if __name__ == "__main__":
    main()
