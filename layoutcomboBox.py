from PyQt5.QtWidgets import QComboBox, QMainWindow, QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.combobox()
       # label.currentTextChanged.connect(self.current_text_changed)


    def combobox(self):
        combo1 = QComboBox(self)
        combo1.addItem('1')
        combo1.addItem('2')
        combo1.addItem('3')
        combo1.addItem('4')

        label = QLabel("Sonuc", self)

        layout = QVBoxLayout()
        layout.addWidget(combo1)
        layout.addWidget(label)
        
        combo1.currentTextChanged.connect(self.current_text_changed)
        
        container = QWidget()
        container.setLayout(layout) 
        self.setCentralWidget(container)

    def current_text_changed(self):
        self.label.setText(self.input.text())

    def on_combobox_changed(self, value):
        print("combobox changed", value)
        # do your code



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()