from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(430, 300)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 80, 101, 31))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 280, 80, 23))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 80, 101, 31))
        self.s_DSB = QDoubleSpinBox(Form)
        self.s_DSB.setObjectName(u"s_DSB")
        self.s_DSB.setGeometry(QRect(120, 130, 62, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 220, 80, 23))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 211, 16))
        self.e_DSB = QDoubleSpinBox(Form)
        self.e_DSB.setObjectName(u"e_DSB")
        self.e_DSB.setGeometry(QRect(280, 130, 62, 24))
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"label")
        self.resultLabel.setGeometry(QRect(130, 20, 211, 500))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Input for Energy", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for speed", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label.setText(QCoreApplication.translate("Form", u"Now we are looking for the mass", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Here results will be showed", None))

    # retranslateUi

