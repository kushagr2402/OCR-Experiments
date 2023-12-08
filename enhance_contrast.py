import sys
import os
from PIL import Image, ImageEnhance

def enhance_contrast(image_path, output_path, contrast_factor):
    """
    Enhances the contrast of an image and saves it to the output directory.

    :param image_path: Path to the image file.
    :param output_path: Path to save the enhanced image.
    :param contrast_factor: Factor by which the contrast will be increased.
    """
    try:
        # Open the image
        img = Image.open(image_path)

        # Enhance the contrast
        enhancer = ImageEnhance.Contrast(img)
        enhanced_img = enhancer.enhance(contrast_factor)

        # Save the enhanced image
        enhanced_img.save(output_path)

    except Exception as e:
        print(f"Could not process {image_path}: {e}")

def main():
    # Check if the input and output directory paths are provided as command line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py input_folder_path output_folder_path")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    contrast_factor = 2  # Adjust the contrast factor as needed

    # Ensure output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each image in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            # Construct the output file path
            output_file_name = "enhanced_" + file_name
            output_file_path = os.path.join(output_folder, output_file_name)

            # Enhance the image's contrast, ignoring images that cannot be read
            enhance_contrast(file_path, output_file_path, contrast_factor)

if __name__ == "__main__":
    main()
