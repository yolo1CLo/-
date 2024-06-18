from PyQt5.QtWidgets import QDoubleSpinBox, QFrame, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget, QMessageBox, QMenuBar, QStatusBar
from PyQt5.QtCore import QRect,QCoreApplication,QMetaObject 

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(636, 300)
        self.a_DSB = QDoubleSpinBox(Form)
        self.a_DSB.setObjectName(u"doubleSpinBox_3")
        self.a_DSB.setGeometry(QRect(260, 210, 62, 24))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 160, 131, 51))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 90, 241, 16))
        self.m_DSB = QDoubleSpinBox(Form)
        self.m_DSB.setObjectName(u"a_DSB")
        self.m_DSB.setGeometry(QRect(130, 210, 62, 24))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 170, 101, 31))
        self.reslabel = QLabel(Form)
        self.resultLabel = QLabel(Form)
        self.resultLabel.setObjectName(u"label")
        self.resultLabel.setGeometry(QRect(130, 20, 211, 500))

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Mass", None))
        self.label.setText(QCoreApplication.translate("Form", u"Now we are looking for the Force", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Acceleration", None))
        self.resultLabel.setText(QCoreApplication.translate("Form", u"Here results will be showed", None))

    # retranslateUi

