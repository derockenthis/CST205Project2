Photo Restoration Application

Coded in Python

External Packages:
numpy
cv2
matplotlib
easygui
pillow
PySide2
requests
urllib.requests

Usage:
To use this application, run the application, then select an image from your computer. You can then apply any of the following filters to it:

Black and White to Color: This filter converts a black and white image to a color image. Requires internet access to use, as it uses an API.
Denoise Image: Reduces noise to image. Can be used multiple times. Overuse may result in blur.
Sharpen Image: Sharpens the edges of shapes in an image. Can be used multiple times.
Resize Image: Changes size of image based on number put in box by the percent of that number.
For example, a resize to 130 increases the size by 30%, to 130% the size of the original, while a resize of 70 decreases the size to 70% of the original.

Once all the desired edits have been applied to an image, the image can be saved via the "save image" once a name is typed.
The destination of the save is the same as the folder the python file is in. If there is no extension in the name, the extension of the original image is used.

Credits:
Code created by Russel De Vera, Derek In, Gaberial Reyes Tejeda, Samuel Sherrill
Black and White to Color filter accessed via https://deepai.org/machine-learning-model/colorizer