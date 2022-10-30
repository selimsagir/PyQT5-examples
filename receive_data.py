import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")

        button = QPushButton("Press here...")
        button.setCheckable(True)
        button.clicked.connect(self.button_clicked)
        button.clicked.connect(self.button_toggled)

        self.setCentralWidget(button)

    def button_clicked(self):
        print("Clicked")
    def button_toggled(self, checked):
        print("Clicked?", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()