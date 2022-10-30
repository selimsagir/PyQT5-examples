import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        combobox = QComboBox()
        combobox.addItems(['One','Two', 'Three', 'Four'])

        # connect signals to the methods.
        combobox.activated.connect(self.activated)
        combobox.currentTextChanged.connect(self.text_changed)
        combobox.currentIndexChanged.connect(self.index_changed)
        
        label = QLabel("Sonuc", self)
        self.setCentralWidget(combobox)

    def activated(self, index):
        print("Activated index: ", index)

    def text_changed(self, s):
        print("Text changed: ", s)
    
    def index_changed(self, index):
        print("Index changed: ", index)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()