from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 
from PyQt5.QtGui import QPalette, QBrush, QColor, QFont
from PyQt5.Qt import Qt


class Ui_Form(object):
    def setupUi(self, MyWindow):
        if not MyWindow.objectName():
            MyWindow.setObjectName(u"MyWindow")
        MyWindow.resize(1000, 1000)
        palette = QPalette()
        brush = QBrush(QColor(170, 170, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        brush2 = QBrush(QColor(240, 255, 247, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        MyWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Monospace")
        font.setPointSize(11)
        MyWindow.setFont(font)
        MyWindow.setAnimated(True)
        self.centralwidget = QWidget(MyWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(110, 240, 211, 61))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(550, 240, 141, 61))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 30, 671, 71))
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 140, 671, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 100, 381, 16))
        MyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MyWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 23))
        MyWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MyWindow)
        self.statusbar.setObjectName(u"statusbar")
        MyWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MyWindow)

        QMetaObject.connectSlotsByName(MyWindow)
    # setupUi

    def retranslateUi(self, MyWindow):
        MyWindow.setWindowTitle(QCoreApplication.translate("MyWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MyWindow", u"Scientific calculator", None))
        self.pushButton_2.setText(QCoreApplication.translate("MyWindow", u"Graphics", None))
        self.label_2.setText(QCoreApplication.translate("MyWindow", u"Hi dear users, this is a tool to calculate the unkown element in an physic formula ", None))
        self.label_3.setText(QCoreApplication.translate("MyWindow", u"Click on the button to be redirected on the page of your choice. ", None))
        self.label_4.setText(QCoreApplication.translate("MyWindow", u"and to make graphics based on your data. ", None))
    # retranslateUi

