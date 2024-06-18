from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1077, 568)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(400, 70, 281, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(480, 120, 151, 16))
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton")
        self.pushButton_1.setGeometry(QRect(490, 160, 80, 23))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_3")
        self.pushButton_2.setGeometry(QRect(490, 190, 80, 23))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_4")
        self.pushButton_3.setGeometry(QRect(490, 230, 80, 23))
        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_2")
        self.pushButton_4.setGeometry(QRect(10, 540, 80, 23))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here you can calculate the gravitational force", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"What do you need? ", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"Mass", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Acceleration", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Force", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"<- Return ", None))
    # retranslateUi