

# from wand.image import Image

# f = "NOLAN.pdf"
# with (Image(filename=f, resolution=120)) as source:
#    for i, image in enumerate(source.sequence):
#        newfilename = f.removesuffix(".pdf") + str(i + 1) + '.jpeg'
#        Image(image).save(filename=newfilename)

import os
from wand.image import Image
import pytesseract
from PIL import Image as PILImage


def save_pdf_pages_as_jpeg(pdf_filename):
    # Create a folder to save the images
    folder_name = pdf_filename.removesuffix(".pdf")
    # Create folder if it doesn't exist
    os.makedirs(folder_name, exist_ok=True)

    with Image(filename=pdf_filename, resolution=120) as source:
        for i, image in enumerate(source.sequence):
            new_filename = f"{folder_name}/page_{i + 1}.jpeg"
            Image(image).save(filename=new_filename)

            # Perform OCR on the generated JPEG image
            ocr_result = pytesseract.image_to_string(
                PILImage.open(new_filename))

            # Print the OCR result
            print(f"Text extracted from {new_filename}:")
            print(ocr_result)
            print("-----------------------------------------")


pdf_filename = "NOLAN.pdf"
save_pdf_pages_as_jpeg(pdf_filename)
