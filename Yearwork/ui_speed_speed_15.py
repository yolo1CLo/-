from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 50, 211, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 270, 80, 23))
        self.d_DSB = QDoubleSpinBox(Form)
        self.d_DSB.setObjectName(u"d_DSB")
        self.d_DSB.setGeometry(QRect(90, 150, 62, 24))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 100, 111, 31))
        self.t_DSB = QDoubleSpinBox(Form)
        self.t_DSB.setObjectName(u"t_DSB")
        self.t_DSB.setGeometry(QRect(240, 150, 62, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(160, 200, 80, 23))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 100, 101, 31))
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"label")
        self.resultLabel.setGeometry(QRect(130, 20, 211, 500))
        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Now we are looking for the speed", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"<- Return", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Input for distance", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Input for time", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Here results will be showed", None))

    # retranslateUi

