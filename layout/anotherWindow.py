from tkinter import Button
from turtle import isvisible
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys

from random import randint

class anotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d " % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window1 = anotherWindow()
        self.window2 = anotherWindow()

        l = QVBoxLayout()
        widget = QWidget()
        self.w = None
        button = QPushButton("Push for Window 1")
        button2 = QPushButton("Push for Window 2")
        button.clicked.connect(self.toggle_window1)
        button2.clicked.connect(self.toggle_window2)

        l.addWidget(button)
        l.addWidget(button2)
        widget.setLayout(l)
        self.setCentralWidget(widget)


    def show_new_window(self, checked):
        if self.w is None:
            self.w = anotherWindow()
        self.w.show()
    
    def toggle_window1(self, checked):
        if self.window2.isVisible():
            self.window2.hide()
            self.window1.show()
        else:
            self.window1.show()

    def toggle_window2(self, checked):
        if self.window1.isVisible():
            self.window1.hide()
            self.window2.show()
        else:
            self.window2.show()

app = QApplication(sys.argv)
w=MainWindow()
w.show()
app.exec_()
