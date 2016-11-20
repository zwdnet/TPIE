# -*- coding:utf-8 -*-
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
# w = QWidget()
# w.resize(250, 150)
# w.move(300, 300)
# w.setWindowTitle("Simple")
# w.show()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtGui import QIcon
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 300, 220)
#         self.setWindowTitle("Icon")
#         self.setWindowIcon(QIcon("举报.png"))
#         self.show()
#
# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
# from PyQt5.QtGui import QFont
#
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         QToolTip.setFont(QFont("SansSerif", 10))
#         self.setToolTip("This is a <b>QWidget</b> widget")
#
#         btn = QPushButton("Button", self)
#         btn.setToolTip("This is a <b>QPushButton</b> widget")
#         btn.resize(btn.sizeHint())
#         btn.move(50, 50)
#
#         self.setGeometry(300, 300, 300, 300)
#         self.setWindowTitle("Tooltips")
#         self.show()
#
# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
# from PyQt5.QtCore import QCoreApplication
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         qbtn = QPushButton("Quit", self)
#         qbtn.clicked.connect(QCoreApplication.instance().quit)
#         qbtn.resize(qbtn.sizeHint())
#         qbtn.move(50, 50)
#
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Quit button")
#         self.show()
#
# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
#
# class Example(QWidget):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle("Message Box")
#         self.show()
#
#     def closeEvent(self, event):
#         reply = QMessageBox.question(self, "Message",
#                                      "Are you suer to quit?", QMessageBox.Yes |
#                                      QMessageBox.No, QMessageBox.No)
#         if reply == QMessageBox.Yes:
#             event.accept()
#         else:
#             event.ignore()
#
# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
# from PyQt5.QtWidgets import QMainWindow, QAction, qApp
# from PyQt5.QtGui import QIcon
#
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.resize(250, 150)
#         self.center()
#         self.setWindowTitle("Center")
#         self.statusBar().showMessage("Ready")
#         exitAction = QAction(QIcon("举报.png"), "&Exit", self)
#         exitAction.setShortcut("Ctrl+Q")
#         exitAction.setStatusTip("Exit application")
#         exitAction.triggered.connect(qApp.quit)
#         self.statusBar()
#
#         menubar = self.menuBar()
#         fileMenu = menubar.addMenu("&File")
#         fileMenu.addAction(exitAction)
#
#         self.toobar = self.addToolBar('Exit')
#         self.toobar.addAction(exitAction)
#
#         self.show()
#
#     def center(self):
#         qr = self.frameGeometry()
#         cp = QDesktopWidget().availableGeometry().center()
#         qr.moveCenter(cp)
#         self.move(qr.topLeft())
#
# app = QApplication(sys.argv)
# ex = Example()
# sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton, QHBoxLayout, QVBoxLayout
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         # lbl1 = QLabel("zym", self)
#         # lbl1.move(15, 10)
#         #
#         # lbl2 = QLabel("zym2", self)
#         # lbl2.move(35, 40)
#         #
#         # lbl3 = QLabel("zym3", self)
#         # lbl3.move(55, 70)
#
#         okButton = QPushButton("OK")
#         cancelButton = QPushButton("Cancel")
#
#         hbox = QHBoxLayout()
#         hbox.addStretch(1)
#         hbox.addWidget(okButton)
#         hbox.addWidget(cancelButton)
#
#         vbox = QVBoxLayout()
#         vbox.addStretch(1)
#         vbox.addLayout(hbox)
#
#         self.setLayout(vbox)
#
#         self.setGeometry(300, 300, 300, 150)
#         self.setWindowTitle("Buttons")
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

# import sys
# from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)
#
# class Example(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         title = QLabel("Title")
#         author = QLabel("Author")
#         review = QLabel("Review")
#
#         titleEdit = QLineEdit()
#         authorEdit = QLineEdit()
#         reviewEdit = QTextEdit()
#
#         grid = QGridLayout()
#         grid.setSpacing(10)
#
#         grid.addWidget(title, 1, 0)
#         grid.addWidget(titleEdit, 1, 1)
#
#         grid.addWidget(author, 2, 0)
#         grid.addWidget(authorEdit, 2, 1)
#
#         grid.addWidget(review, 3, 0)
#         grid.addWidget(reviewEdit, 3, 1, 5, 1)
#
#         self.setLayout(grid)
#
#         self.setGeometry(300, 300, 350, 300)
#         self.setWindowTitle("Review")
#
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton, QLCDNumber, QSlider, QVBoxLayout, QApplication)


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        btn1 = QPushButton("Button1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)

        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("Signal & slot")
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.key_Escape:
            self.close()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " was pressed")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
