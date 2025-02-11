from rembg import remove
from PIL import Image

class PhotoTransform:
    def remove_background(self, img):
        # Remove background
        res_img = remove(img)

        # Get the bounding box of non-transparent pixels
        bbox = res_img.getbbox()

        # If bbox is found, crop the image
        if bbox:
            res_img = res_img.crop(bbox)

        return res_img

    def resize(self, image, width=None, height=None):
        """
        Resize an image while maintaining its aspect ratio.

        Parameters:
        - image: A PIL Image object.
        - width: The desired width in pixels. If None, the width will be calculated to maintain the aspect ratio based on the provided height.
        - height: The desired height in pixels. If None, the height will be calculated to maintain the aspect ratio based on the provided width.

        Returns:
        - A new PIL Image object with the specified dimensions.
        """
        # Get the original dimensions
        original_width, original_height = image.size

        # If both width and height are None, return the original image
        if width is None and height is None:
            return image

        # Calculate the new dimensions while maintaining the aspect ratio
        if width is None:
            # Calculate the width based on the desired height
            aspect_ratio = original_width / original_height
            width = int(height * aspect_ratio)
        elif height is None:
            # Calculate the height based on the desired width
            aspect_ratio = original_height / original_width
            height = int(width * aspect_ratio)

        # Resize the image with the computed dimensions
        resized_image = image.resize((width, height), Image.LANCZOS)

        return resized_image
