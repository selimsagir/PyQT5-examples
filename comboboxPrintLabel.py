import sys
from PyQt5.QtWidgets import (QApplication, 
                            QWidget,QLabel,
                            QVBoxLayout,
                            QComboBox,
                            QSpinBox)


class ComboExample(QWidget):
    def __init__(self):
        super().__init__()


        self.topLabel = QLabel("Select a Combo", self)

        combo_box = QComboBox(self)
        combo_box.addItems(['1', '2', '3'])

        self.bottom_label = QLabel('Result',self)
        self.spin = QSpinBox(self)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.topLabel)
        v_layout.addWidget(combo_box)
        v_layout.addWidget(self.bottom_label)
        v_layout.addWidget(self.spin)

        combo_box.activated[str].connect(self.change_label)
        combo_box.currentTextChanged[str].connect(self.on_select)
        #combo_box.currentIndexChanged.connect(self.on_select)

        self.setLayout(v_layout)
        self.setWindowTitle('Use of comboBox')



    def on_select(self,txt):
        txt = int(txt)
        self.spin.setValue((txt))
    def change_label(self,txt):
        #txt =+ 1
        #txt= str(txt)
        self.bottom_label.setText(txt)


app = QApplication(sys.argv)
combo_box = ComboExample()
combo_box.show()
app.exec_()
