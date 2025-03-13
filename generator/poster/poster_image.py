from PIL import Image
from PIL.Image import Image as ImageType

def resize_image(image: ImageType, size: tuple[int, int]):
        # Get the original dimensions
        original_width, original_height = image.size

        width, height = size

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