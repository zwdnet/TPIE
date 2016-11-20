# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout, QApplication)


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # grid = QGridLayout()
        qvbox = QVBoxLayout()
        gridBar = QGridLayout()
        gridWidget = QWidget()

        numberEdit = QLineEdit()

        names = ["Cls", "Bck", "", "Close",
                 "7", "8", "9", "/",
                 "4", "5", "6", "*",
                 "1", "2", "3", "-",
                 "0", ".", "=", "+"]

        position = [(i, j) for i in range(5) for j in range(4)]

        for position, name in zip(position, names):
            if name == "":
                continue
            button = QPushButton(name)
            gridBar.addWidget(button, *position)
        qvbox.addWidget(numberEdit)
        gridWidget.setLayout(gridBar)
        qvbox.addWidget(gridWidget)

        self.setLayout(qvbox)

        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())
