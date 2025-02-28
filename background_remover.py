from rembg import remove
import requests
from PIL import Image
import io

class LocalPipeline():
    def __init__(self):
        pass

    def __call__(self, img):
        # Remove background
        res_img = remove(img)

        # Get the bounding box of non-transparent pixels
        bbox = res_img.getbbox()

        # If bbox is found, crop the image
        if bbox:
            res_img = res_img.crop(bbox)

        return res_img
    
class RemotePipeline():
    def __init__(self, url):
        self.url = url

    def remove_background(self, image: Image.Image):
        # Convert the image to a byte stream
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format="PNG")
        img_byte_arr.seek(0)  # Go to the start of the byte stream

        # Send the image as part of the POST request
        files = {"image": ("image.png", img_byte_arr, "image/png")}
        response = requests.post(f"{self.url}/rembg", files=files)

        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")

        result_image = Image.open(io.BytesIO(response.content))  # Convert the binary data to an image
        return result_image

    def __call__(self, img: Image.Image):
        return self.remove_background(img)


class BackgroundRemover:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def get_local_pipeline():
        return BackgroundRemover(pipeline=LocalPipeline())
    
    def get_remote_pipeline(url):
        return BackgroundRemover(pipeline=RemotePipeline(url))
    
    def remove_background(self, image) -> str:
        return self.pipeline(image)
    
    