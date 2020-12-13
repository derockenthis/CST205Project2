
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance

# Open an already existing image
imageObject = Image.open("sharper.jpg")
imageObject.show()

# Apply sharp filter
sharpened1 = imageObject.filter(ImageFilter.SHARPEN)
sharpened2 = sharpened1.filter(ImageFilter.SHARPEN)

# Show the sharpened images
sharpened2.show()
sharpened2.save("sharper2.jpg")
