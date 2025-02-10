from PIL import Image

def generate_image_gradient(width=900, height=900, start_color=(0, 0, 255), end_color=(0, 0, 0)):
    """
    Generate a gradient image transitioning from start_color to end_color.

    Parameters:
    - width: The width of the image in pixels. Default is 900.
    - height: The height of the image in pixels. Default is 900.
    - start_color: The starting color of the gradient in RGB format. Default is blue (0, 0, 255).
    - end_color: The ending color of the gradient in RGB format. Default is black (0, 0, 0).

    Returns:
    - A Pillow Image object representing the gradient.
    """
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
