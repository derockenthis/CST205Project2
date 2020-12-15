# opens an image using pillow and sharpens the image twice. 
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# Open an already existing image
imageObject = Image.open("bird.jpg")
imageObject.show()

# Apply sharp filter
sharpened1 = imageObject.filter(ImageFilter.SHARPEN)
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN)

# Show the sharpened images
sharpened2.show()
sharpened2.save("test.jpg")
