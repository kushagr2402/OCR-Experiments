#from https://github.com/NielsRogge/Transformers-Tutorials/blob/master/Swin2SR/Perform_image_super_resolution_with_Swin2SR.ipynb
#use pip install 'transformers[torch]' from https://huggingface.co/docs/transformers/installation
#also from https://huggingface.co/docs/transformers/model_doc/swin2sr

import torch
import numpy as np
from PIL import Image
import sys
from transformers import AutoImageProcessor, Swin2SRForImageSuperResolution
import requests
import os
import io



def super_resolve_image(input_image_path):
    # Load the model and processor
    processor = AutoImageProcessor.from_pretrained("caidas/swin2SR-classical-sr-x2-64")
    model = Swin2SRForImageSuperResolution.from_pretrained("caidas/swin2SR-classical-sr-x2-64")

    # Load the image from the provided path
    #image = Image.open(input_image_path)
    with open(input_image_path, 'rb') as file:
        raw_data = file.read()
    image = Image.open(io.BytesIO(raw_data)).convert("RGB")
    #url = "https://huggingface.co/spaces/jjourney1125/swin2sr/resolve/main/samples/butterfly.jpg"
    #image = Image.open(requests.get(url, stream=True).raw)

    # Prepare the image for the model
    inputs = processor(image, return_tensors="pt")

    # Forward pass
    with torch.no_grad():
        outputs = model(**inputs)

    # Convert the output to an image format
    output = outputs.reconstruction.data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.moveaxis(output, source=0, destination=-1)
    output = (output * 255.0).round().astype(np.uint8)  # Convert from float32 to uint8

    # Save the output image
    output_image = Image.fromarray(output)
    base_name, ext = os.path.splitext(input_image_path)
    output_image_path = f"{base_name}sr{ext}"
    output_image.save(output_image_path)
    print(f"Saved super-resolved image as {output_image_path}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <image_path>")
        sys.exit(1)

    input_image_path = sys.argv[1]
    super_resolve_image(input_image_path)

if __name__ == "__main__":
    main()
