from PIL import Image, ImageChops

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    # Returns the absolute value of the pixel-by-pixel difference between the two images.
    # pixel value of diff (image object): if no difference, the value is 0, otherwise the abs(difference).
    # https://pillow.readthedocs.io/en/3.0.x/reference/ImageChops.html
    diff = ImageChops.difference(a, b)
    diff = diff.convert('L')
    
    # Maps the diff (image) to 0 or 255. If a pixel of diff is 0 (no difference), then the result of it is 0, otherwise is 255.
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.point
    diff = diff.point(point_table)
    
    # 1-channel image to 3-channels image
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.convert
    new = diff.convert('RGB')
    
    # Pastes another image b into this image new according to the mask.
    # Where pixel value of the mask is 255, pixel value of new is replaced by value of b. 
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.paste
    new.paste(b, mask=diff)
    return new

a = Image.open('Spot_the_difference1.png')
b = Image.open('Spot_the_difference2.png')
c = black_or_b(a, b)
c.save('result.png')
