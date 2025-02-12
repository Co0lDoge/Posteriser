from PIL import Image

class ImageGenerator:
    def generate_image_gradient(width=900, height=900, start_color=(0, 0, 255), end_color=(0, 0, 0)):
        # Create a new image with the specified dimensions
        img = Image.new('RGB', (width, height))

        # Generate the gradient
        for y in range(height):
            # Calculate the interpolation factor (0.0 at the top, 1.0 at the bottom)
            factor = y / (height - 1)
            # Interpolate between the start and end colors
            color = tuple(
                int(start_color[i] * (1 - factor) + end_color[i] * factor)
                for i in range(3)
            )
            # Set the color for the current row
            for x in range(width):
                img.putpixel((x, y), color)

        return img
