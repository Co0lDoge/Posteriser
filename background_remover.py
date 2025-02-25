from rembg import remove
from PIL import Image

class BackgroundRemover:
    def remove_background(img):
        # Remove background
        res_img = remove(img)

        # Get the bounding box of non-transparent pixels
        bbox = res_img.getbbox()

        # If bbox is found, crop the image
        if bbox:
            res_img = res_img.crop(bbox)

        return res_img
