#Code created by Samuel Sherrill
#For CST205 project

#imports
import sys
import easygui
from PIL import Image
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton
from PySide2.QtGui import QImage, QImageReader, QPixmap

class mainWindow(QWidget):
	def __init__(self):
		super().__init__()
		
		self.activeImage=""
		
		#Button Row Setup
		self.selectButton=QPushButton("Click to select an image.")
		self.selectButton.clicked.connect(self.imageSelect)
		self.option1=QPushButton("Placeholder.")
		self.option1.clicked.connect(self.filter1)
		#Add connect here
		self.option2=QPushButton("Placeholder.")
		#Add connect here
		self.option3=QPushButton("Placeholder.")
		#Add connect here
		self.option4=QPushButton("Placeholder.")
		#Add connect here
		
		self.optionsRow=QHBoxLayout()
		self.optionsRow.addWidget(self.selectButton)
		self.optionsRow.addWidget(self.option1)
		self.optionsRow.addWidget(self.option2)
		self.optionsRow.addWidget(self.option3)
		self.optionsRow.addWidget(self.option4)
		
		#Image Display Setup
		self.activeImageDisplay=QLabel()
		self.previewImageDisplay=QLabel()
		
		
		self.imageDisplayRow=QHBoxLayout()
		self.imageDisplayRow.addWidget(self.activeImageDisplay)
		self.imageDisplayRow.addWidget(self.previewImageDisplay)
		
		#Main Layout Setup
		self.mainLayout=QVBoxLayout()
		self.mainLayout.addLayout(self.optionsRow)
		self.mainLayout.addLayout(self.imageDisplayRow)
		
		self.setLayout(self.mainLayout)
		
	def imageSelect(self): #function for selecting image
		self.activeImage=easygui.fileopenbox()
		pixmap=QPixmap(self.activeImage)
		n=400
		pixmap=pixmap.scaled(n,n,Qt.KeepAspectRatio)
		self.activeImageDisplay.setPixmap(pixmap)
		self.previewImageDisplay.clear()
		self.repaint()

	def filter1(self):
		imPath=self.activeImage
		pixmap=QPixmap(imPath)
		n=400
		pixmap=pixmap.scaled(n,n,Qt.KeepAspectRatio)
		self.previewImageDisplay.setPixmap(pixmap)
		self.repaint()

app=QApplication([])
imageRestoreWindow=mainWindow()
imageRestoreWindow.show()
app.exec_()
