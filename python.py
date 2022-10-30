
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel

class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.ozellikEkle()
        self.ekOzellikEkle()
        self.buton.clicked.connect(self.tiklandi)

    def ozellikEkle(self):
        self.resize(500,500)
        self.move(700,100)
        self.setWindowTitle("Basit Pencere")

    def ekOzellikEkle(self):
        self.input = QLineEdit("Bir şey Yaz",self)
        self.input.setGeometry(10, 10, 200, 25)

        self.buton = QPushButton("ekrana bas", self)
        self.buton.setGeometry(10, 50, 200, 75)

        self.label = QLabel("Sonuc", self)
        self.label.setGeometry(110, 110, 220, 75)

    def tiklandi(self):
        self.label.setText(self.input.text())

app = QApplication(sys.argv)
pencere = Pencere()
pencere.show()
sys.exit(app.exec_()) 
