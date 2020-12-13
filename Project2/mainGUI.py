#Code created by Samuel Sherrill
#For CST205 project

#imports
import sys
import easygui
from PIL import Image
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit
from PySide2.QtGui import QImage, QImageReader, QPixmap

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
		self.option1=QPushButton("Sample Filter.")
		self.option1.clicked.connect(self.sampleFilter)
		#Add connect here
		self.option2=QPushButton("Placeholder.")
		#Add connect here
		self.option3=QPushButton("Placeholder.")
		#Add connect here
		self.option4=QPushButton("Placeholder.")
		#Add connect here
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

	def sampleFilter(self): #code to be replaced with filter
		if self.previewImage!="": #checks if preview exists. If it does, it will be edited instead of original.
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
			self.repaint()
		elif self.activeImage!="": #checks if image is ready
			self.previewImage=self.activeImage
			imPath=self.previewImage
			pixmap=QPixmap(imPath)
			pixmap=pixmap.scaled(self.n,self.n,Qt.KeepAspectRatio)
			self.previewImageDisplay.setPixmap(pixmap)
			self.hedder.setText("Filter applied. Now, apply additional filters or save.")
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
		return ""

app=QApplication([])
imageRestoreWindow=mainWindow()
imageRestoreWindow.show()
app.exec_()
