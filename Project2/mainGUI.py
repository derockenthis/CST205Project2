#Code created by Samuel Sherrill
#For CST205 project

#imports
import tempfile
import numpy as np
import cv2
from matplotlib import pyplot as plt
import sys
import easygui
from PIL import Image, ImageFilter, ImageEnhance
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide2.QtGui import QImage, QImageReader, QPixmap
import requests
import urllib.request

class mainWindow(QWidget):
	def __init__(self):
		super().__init__()
		
		self.activeImage=""
		self.previewImage=""
		self.n=400 #Set image display max size
		
		#Top Row Setup
		self.hedder=QLabel("Welcome to the Image Restoration App")
		
		#Button Row Setup
		self.selectButton=QPushButton("Click to select an image.")
		self.selectButton.clicked.connect(self.imageSelect)
		self.option1=QPushButton("Black and White to Color")
		self.option1.clicked.connect(self.bandwToColorFilter)
		self.option2=QPushButton("Denoise Image")
		self.option2.clicked.connect(self.denoiseFilter)
		self.option3=QPushButton("Sharpen Image")
		self.option3.clicked.connect(self.sharpenFilter)
		self.option4=QPushButton("Resize Image")
		self.option4.clicked.connect(self.resizeFilter)
		self.resizePercent=QLineEdit(self)
		self.saveImage=QPushButton("Save Image")
		self.saveImage.clicked.connect(self.imageSave)
		self.saveLabel=QLabel("Save name ->")
		self.saveName=QLineEdit(self)
		
		self.optionsRow=QHBoxLayout()
		self.optionsRow.addWidget(self.selectButton)
		self.optionsRow.addWidget(self.option1)
		self.optionsRow.addWidget(self.option2)
		self.optionsRow.addWidget(self.option3)
		self.optionsRow.addWidget(self.option4)
		self.optionsRow.addWidget(self.resizePercent)
		self.optionsRow.addWidget(self.saveLabel)
		self.optionsRow.addWidget(self.saveName)
		self.optionsRow.addWidget(self.saveImage)
		
		#Image Display Setup
		self.activeImageDisplay=QLabel()
		self.previewImageDisplay=QLabel()
		
		
		self.imageDisplayRow=QHBoxLayout()
		self.imageDisplayRow.addWidget(self.activeImageDisplay)
		self.imageDisplayRow.addWidget(self.previewImageDisplay)
		
		#Main Layout Setup
		self.mainLayout=QVBoxLayout()
		self.mainLayout.addWidget(self.hedder)
		self.mainLayout.addLayout(self.optionsRow)
		self.mainLayout.addLayout(self.imageDisplayRow)
		
		self.setLayout(self.mainLayout)
		
	def imageSelect(self): #function for selecting image
		self.activeImage=easygui.fileopenbox()
		pixmap=QPixmap(self.activeImage)
		self.previewImage=""
		self.previewImageDisplay.clear()
		if str(pixmap.size())=="PySide2.QtCore.QSize(0, 0)": #checks if image is valid
			self.activeImage=""
			self.activeImageDisplay.clear()
			self.hedder.setText("Warning: Invalid image.")
			self.repaint()
		else: #if image is valid, sets and displays image
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.activeImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Image selected. Now, apply a filter.")
			self.previewImageDisplay.clear()
			self.repaint()

	def bandwToColorFilter(self): #code to run bandwToColor, save and display
		if self.previewImage!="": #checks if preview exists. If it does, it will be edited instead of original.
			self.previewImage=bandwToColor(self.previewImage)
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		elif self.activeImage!="": #checks if image is ready
			self.previewImage=bandwToColor(self.activeImage)
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		else: #if image is not ready, displays warning
			self.hedder.setText("Warning: No image selected. Select an image before apllying filters.")
			self.repaint()

	def denoiseFilter(self): #code to run denoise, save and display
		if self.previewImage!="": #checks if preview exists. If it does, it will be edited instead of original.
			self.previewImage=denoise(self.previewImage)
			imPath=self.previewImage
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		elif self.activeImage!="": #checks if image is ready
			self.previewImage=denoise(self.activeImage)
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		else: #if image is not ready, displays warning
			self.hedder.setText("Warning: No image selected. Select an image before apllying filters.")
			self.repaint()

	def sharpenFilter(self): #code to run sharpen, save and display
		if self.previewImage!="": #checks if preview exists. If it does, it will be edited instead of original.
			self.previewImage=sharpen(self.previewImage)
			imPath=self.previewImage
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		elif self.activeImage!="": #checks if image is ready
			self.previewImage=sharpen(self.activeImage)
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		else: #if image is not ready, displays warning
			self.hedder.setText("Warning: No image selected. Select an image before apllying filters.")
			self.repaint()
			
	def resizeFilter(self): #code to run resize, save and "display"
		if self.resizePercent.displayText().isnumeric()==False:
			self.hedder.setText("Warning: You must imput an integer for the resize. Greater than 100 increases size, less than 100 decreases size.")
			self.repaint()
		elif int(self.resizePercent.displayText())<0.0:
			self.hedder.setText("Warning: Resize must be number greater than 0.")
			self.repaint()
		elif self.previewImage!="": #checks if preview exists. If it does, it will be edited instead of original.
			self.previewImage=resize(self.previewImage,int(self.resizePercent.displayText()))
			imPath=self.previewImage
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Warning: Resize may not be visible in app. Now, apply additional filters or save.")
			self.repaint()
		elif self.activeImage!="": #checks if image is ready
			self.previewImage=resize(self.activeImage,int(self.resizePercent.displayText()))
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Warning: Resize may not be visible in app. Now, apply additional filters or save.")
			self.repaint()
		else: #if image is not ready, displays warning
			self.hedder.setText("Warning: No image selected. Select an image before apllying filters.")
			self.repaint()
	
	def imageSave(self): #code to save image
		if self.previewImage=="": #checks if image is ready
			self.hedder.setText("Warning: No image to save. Upload an image to edit or apply a filter.")
			self.repaint()
		elif self.saveName.displayText()=="": #checks if name is valid
			self.hedder.setText("Warning: No name for image. Add a name before hitting save.")
			self.repaint()
		else:
			im=Image.open(self.previewImage)
			if "." in self.saveName.displayText(): #checks if save name as extension
				fileName=self.saveName.displayText()
			else: #if not, defaults to extension of original image
				extension=findExtension(self.activeImage)
				fileName=self.saveName.displayText()+extension
			im.save(fileName)
			self.hedder.setText("Image saved! Remember to change the save name before saving more images.")
			
def findExtension(fil): #function to return file extension from a file name
	if "." in fil:
		revFil=fil[::-1]
		ext=""
		for char in revFil:
			if char==".":
				ext=char+ext
				break
			else:
				ext=char+ext
		return ext
	else:
		return ".jpg"

#These functions are the filters for the app
def bandwToColor(filepath): #Function to download color version of black and white input from API
	r = requests.post(
		"https://api.deepai.org/api/colorizer",
		files={
			'image': open(filepath, 'rb'),
		},
		headers={'api-key': 'b8c5d118-0549-4884-b765-79798f16fa00'}
	)

	return urllib.request.urlretrieve(r.json()['output_url'])[0]

def denoise(filepath): #Function to save denoised version of imput
	img = cv2.imread(filepath)

	dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)
	newpath=tempfile.mkstemp(suffix=findExtension(filepath))[1]
	cv2.imwrite(newpath, dst)
	return newpath

def resize(filepath,scale_percent): #Function to save denoised version of imput
	img = cv2.imread(filepath)

	# percent of original size
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)
	dim = (width, height)
	# resize image
	resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
	newpath=tempfile.mkstemp(suffix=findExtension(filepath))[1]
	cv2.imwrite(newpath, resized)
	return newpath

def sharpen(filepath): #Function to save sharpened version of imput
	# Open an already existing image
	imageObject = Image.open(filepath)
	# Apply sharp filter
	sharpened = imageObject.filter(ImageFilter.SHARPEN)
	
	newpath=tempfile.mkstemp(suffix=findExtension(filepath))[1]
	sharpened.save(newpath)
	return newpath


app=QApplication([])
imageRestoreWindow=mainWindow()
imageRestoreWindow.show()
app.exec_()
