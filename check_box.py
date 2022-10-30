import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("+ Check Box +")

        check_box = QCheckBox()
        check_box.setCheckState(Qt.Checked)

        check_box.stateChanged.connect(self.show_state)

        self.setCentralWidget(check_box)

    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()