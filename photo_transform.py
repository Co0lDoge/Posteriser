from rembg import remove

def remove_background(img):
    # Remove background
    res_img = remove(img)

    # Convert to RGBA (to ensure transparency is preserved)
    res_img = res_img.convert("RGBA")

    # Get the bounding box of non-transparent pixels
    bbox = res_img.getbbox()

    # If bbox is found, crop the image
    if bbox:
        res_img = res_img.crop(bbox)

    return res_img

