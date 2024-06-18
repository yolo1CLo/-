from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(605, 455)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(390, 140, 111, 31))
        self.c_DSB = QDoubleSpinBox(Form)
        self.c_DSB.setObjectName(u"c_DSB")
        self.c_DSB.setGeometry(QRect(400, 170, 62, 24))
        self.d_DSB = QDoubleSpinBox(Form)
        self.d_DSB.setObjectName(u"d_DSB")
        self.d_DSB.setGeometry(QRect(150, 170, 62, 24))
        self.w_DSB = QDoubleSpinBox(Form)
        self.w_DSB.setObjectName(u"w_DSB")
        self.w_DSB.setGeometry(QRect(150, 170, 62, 24))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 130, 131, 51))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 300, 80, 23))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 390, 80, 23))
        self.F_DSB = QDoubleSpinBox(Form)
        self.F_DSB.setObjectName(u"F_DSB")
        self.F_DSB.setGeometry(QRect(270, 170, 62, 24))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 140, 111, 31))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 50, 57, 15))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 100, 241, 16))
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"label")
        self.resultLabel.setGeometry(QRect(130, 20, 211, 500))
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Input for Grade", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for Force", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for Work", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Now we are looking for the Distance", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Here results will be showed", None))

    # retranslateUi

