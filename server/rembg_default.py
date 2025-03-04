from PIL import Image
from rembg import remove, new_session
import os

class BackgroundRemover:
    def __init__(self, u2net_path):
        os.environ['U2NET_HOME'] = u2net_path
        model_name = "u2net"
        self.rembg_session = new_session(model_name)

    def remove_background(self, img: Image.Image) -> Image.Image:
        # Remove background
        res_img = remove(img, session=self.rembg_session)

        return res_img