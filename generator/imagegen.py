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
    
    from PIL import Image

    def generate_transparent_gradient(width=900, height=900, start_color=(0, 0, 255), end_color=(0, 0, 100), exponent=2):
        # Create an image with an RGBA mode (supports transparency)
        img = Image.new('RGBA', (width, height))

        for y in range(height):
            # Linear factor from 0.0 to 1.0
            t = y / (height - 1)
            # Apply non-linearity: with exponent > 1, the increase is slower at first and steeper at the end
            factor = t ** exponent
            
            # Interpolate between fully transparent and the target color
            color = (
                int(start_color[0] * (1 - factor) + end_color[0] * factor),
                int(start_color[1] * (1 - factor) + end_color[1] * factor),
                int(start_color[2] * (1 - factor) + end_color[2] * factor),
                int(255 * factor)  # Alpha value (0 at the top, 255 at the bottom)
            )
            
            for x in range(width):
                img.putpixel((x, y), color)

        return img
