from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(591, 416)

        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(100, 130, 361, 81))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.a_DSB = QDoubleSpinBox(self.frame)
        self.a_DSB.setObjectName(u"a_DSB")
        self.a_DSB.setGeometry(QRect(10, 30, 62, 24))
        self.a_DSB.setMinimum(-99.989999999999995)
        self.a_DSB.setSingleStep(0.500000000000000)
        self.a_DSB.setValue(1)

        self.b_DSB = QDoubleSpinBox(self.frame)
        self.b_DSB.setObjectName(u"b_DSB")
        self.b_DSB.setGeometry(QRect(130, 30, 62, 24))
        self.b_DSB.setMinimum(-99.989999999999995)
        self.b_DSB.setSingleStep(0.500000000000000)
        self.b_DSB.setValue(1)

        self.c_DSB = QDoubleSpinBox(self.frame)
        self.c_DSB.setObjectName(u"c_DSB")
        self.c_DSB.setGeometry(QRect(260, 30, 62, 24))
        self.c_DSB.setMinimum(-99.989999999999995)
        self.c_DSB.setSingleStep(0.500000000000000)
        self.c_DSB.setValue(1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 61, 16))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 10, 61, 16))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 10, 61, 16))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 361, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 80, 171, 16))

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 370, 80, 23))

        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"label")
        self.resultLabel.setGeometry(QRect(130, 20, 211,500))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Value of a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Value of b", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Value of c", None))
        self.label.setText(QCoreApplication.translate("Form", u"Here we will calculate the answers of a quadratic formula,", None))
        self.label_2.setText(QCoreApplication.translate("Form", u" in this form: ax\u00b2+bx+c = 0", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Here results will be showed", None))

    # retranslateUi

