# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QGridLayout,
        QPushButton, QLineEdit, QVBoxLayout, QApplication, QMessageBox)
from PyQt5.QtCore import QCoreApplication
from stack import stack

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.number = ""
        # self.numbers = stack()
        # self.operator = stack()
        self.operator = ""
        self.First = True
        self.intNumber = 0
        self.initUI()

    def initUI(self):
        # grid = QGridLayout()
        qvbox = QVBoxLayout()
        gridBar = QGridLayout()
        gridWidget = QWidget()

        self.numberEdit = QLineEdit()
        self.numberEdit.setReadOnly(True)

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
            if name == "Close":
                button.clicked.connect(QCoreApplication.instance().quit)
            else:
                button.clicked.connect(self.buttonClicked)
        qvbox.addWidget(self.numberEdit)
        gridWidget.setLayout(gridBar)
        qvbox.addWidget(gridWidget)

        self.setLayout(qvbox)

        self.move(300, 150)
        self.setWindowTitle("Calculator")
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.dealData(sender.text())

    def displayNumbers(self, data):
        self.numberEdit.end(False)
        self.numberEdit.clear()
        self.numberEdit.insert(data)

    def dealData(self, data):
        if '0' <= data <= '9':
            self.number += data
            self.displayNumbers(self.number)
        elif data in ['+', '-', '*', '/']:
            if self.number == "":
                return
            if self.First == True:
                self.intNumber = int(self.number)
                self.number = ""
                self.operator = data
                self.First = False
        elif data == '=':
            if self.First == False:
                res = 0
                if self.operator == '+':
                    res = self.intNumber + int(self.number)
                elif self.operator == '-':
                    res = self.intNumber - int(self.number)
                elif self.operator == '*':
                    res = self.intNumber * int(self.number)
                elif self.operator == '/':
                    if self.number == '0':
                        res = "Error"
                    else:
                        res = self.intNumber / int(self.number)
                self.First = True
                self.displayNumbers(str(res))
                self.number = ""
        elif data == "Cls":
            self.number = ""
            self.operator = ""
            self.First = True
            self.displayNumbers("0")


def temptest():
    s = stack()
    text = "123455"
    s.push(int(text))
    print(s.size())
    print(s.top())
    print(s.size())
    print(s.pop())
    print(s.size())

if __name__ == "__main__":
    # temptest()
    app = QApplication(sys.argv)
    ex = Calculator()
    sys.exit(app.exec_())

