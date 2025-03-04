from rembg import remove, new_session
import requests
from PIL import Image
import io
import os

U2NET_PATH = "C:/WorkFolder/ML/Posteriser/model/u2net/"

def crop_image(image: Image.Image) -> Image.Image:
    # Get the bounding box of non-transparent pixels
    bbox = image.getbbox()

    # If bbox is found, crop the image
    if bbox:
        image = image.crop(bbox)
    return image

class LocalPipeline():
    def __init__(self):
        os.environ['U2NET_HOME'] = U2NET_PATH
        model_name = "u2net"
        self.rembg_session = new_session(model_name)

    def __call__(self, img):
        # Remove background
        res_img = remove(img, session=self.rembg_session)

        return res_img
    
class RemoverPipeline():
    def __init__(self):
        from transparent_background import Remover
        self.remover = Remover()

    def __call__(self, img):
        return self.remover.process(img, threshold=0.6)
    
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
    
    def get_remover_pipeline():
        return BackgroundRemover(pipeline=RemoverPipeline())
    
    def remove_background(self, image) -> str:
        result_image = self.pipeline(image)
        cropped_image = crop_image(result_image)
        return cropped_image
    
    