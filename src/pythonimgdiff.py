from PIL import Image, ImageChops

if_debug = 1  # change to 0 to stop generating debug info.

point_table = ([0] + ([255] * 255))

def black_or_b(a, b):
    # Returns an image (RGB) with the absolute value of the pixel-by-pixel difference between the two images.
    # pixel value of diff (image object): if no difference, the value is 0, otherwise the abs(difference).
    # https://pillow.readthedocs.io/en/3.0.x/reference/ImageChops.html
    diff = ImageChops.difference(a, b)
    if if_debug == 1:
        print('result1.png ', *diff.getdata())
        diff.save('result1.png')
    
    # Convert image to greyscale (“L”) - 1 channel  
    # e.g. (12, 55, 1, 0) -> (a number), that is L = R * 299/1000 + G * 587/1000 + B * 114/1000
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.convert
    diff = diff.convert('L')
    if if_debug == 1:
        print('result2.png ', *diff.getdata())
        diff.save('result2.png')
    
    # Maps the diff (image) to 0 or 255. If a pixel of diff is 0 (no difference), then mapping result is 0, otherwise is 255.
    # e.g. (None 0) -> (255);  (0) -> (0)
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.point
    diff = diff.point(point_table)
    if if_debug == 1:
        print('result3.png ', *diff.getdata())
        diff.save('result3.png')
    
    # 1-channel image to 3-channels image, e.g. (255) -> (255, 255, 255)
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.convert
    new = diff.convert('RGB')
    if if_debug == 1:
        print('result4.png ', *new.getdata())
        diff.save('result4.png')
    
    # Pastes another image b into this image new according to the mask.
    # Where pixel value of the mask is 255, pixel value of new is replaced by value of b. 
    # e.g. (255, 255, 255) -> "(1, 23, 4) from b";  (0, 0, 0) -> "(0, 0, 0) from new"
    # https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.Image.paste
    new.paste(b, mask=diff)
    if if_debug == 1:
        print('result5.png ', *new.getdata())
        diff.save('result5.png')
    return new

a = Image.open('Spot_the_difference1.png')
b = Image.open('Spot_the_difference2.png')
c = black_or_b(a, b)
c.save('result.png')
