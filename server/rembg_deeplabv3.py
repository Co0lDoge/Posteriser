import torch
from torchvision import models, transforms
from PIL import Image
import numpy as np

class BackgroundRemoverDeeplab:
    def __init__(self, model_path: str):
        torch.hub.set_dir(model_path)
        self.model = models.segmentation.deeplabv3_resnet101(pretrained=True)
        self.model.eval()  # Set the model to evaluation mode

    def remove_background(self, img: Image.Image) -> Image.Image:
        # Define the image transformation pipeline
        preprocess = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        # Load and preprocess the image
        img_tensor = preprocess(img).unsqueeze(0)  # Add batch dimension

        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model = self.model.to(device)
        img_tensor = img_tensor.to(device)

        # Make predictions
        with torch.no_grad():
            output = self.model(img_tensor)['out'][0]  # Get the output from the model
            output_predictions = output.argmax(0)  # Get the predicted class for each pixel

        # Convert to numpy array for plotting
        output_predictions = output_predictions.cpu().numpy()

        # Create a binary mask for the "person" class (class index 15)
        human_mask = (output_predictions == 15).astype(np.uint8)

        # Convert the original image to a numpy array
        img_np = np.array(img)

        # Extract the human region using the mask
        # Multiply the mask with the original image to keep only the human area
        extracted_human = img_np * np.expand_dims(human_mask, axis=-1)  # Apply the mask to each channel

        # Create an RGBA image where the alpha channel is the human mask (transparent background)
        rgba_image = np.dstack((extracted_human, human_mask * 255))  # Add alpha channel with 255 where mask is

        # Convert the image to a Pillow Image
        pil_image = Image.fromarray(rgba_image, 'RGBA')

        # Return the image with the human extracted and the background transparent
        return pil_image