# pillow,openvc libaraies
import cv2
from matplotlib import pyplot as plt
from PIL import Image
import pytesseract

#im_file = "data/page_01.jpg"
#im = Image.open(im_file)
#im.save("temp/page_01.jpg")


image_file = "data/page_01.jpg"
img = cv2.imread(image_file)

#https://stackoverflow.com/questions/28816046/
#displaying-different-images-with-actual-size-in-matplotlib-subplot
def display(im_path):
    dpi = 80
    im_data = plt.imread(im_path)

    height, width  = im_data.shape[:2]
    
    # What size does the figure need to be in inches to fit the image?
    figsize = width / float(dpi), height / float(dpi)

    # Create a figure of the right size with one axes that takes up the full figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_axes([0, 0, 1, 1])

    # Hide spines, ticks, etc.
    ax.axis('off')

    # Display the image.
    ax.imshow(im_data, cmap='gray')

    plt.show()
display(image_file)