import sys
import os
import math
import random
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.ticker import MaxNLocator

import ui_quad_screen_2, ui_newt_mass_7, ui_work_screen_4, ui_calc_screen_1, ui_kine_screen_6, \
    ui_speed_screen_5, ui_newt_home_3, ui_newt_acceleration_8, ui_newt_force_9, ui_work_D_10, \
    ui_work_W_12, ui_work_F_11, ui_speed_distance_13, ui_speed_time_14, ui_speed_speed_15, \
    ui_kin_E_18, ui_kin_m_16, ui_kin_s_17, ui_main_screen_0

from ui_calc_screen_1 import Ui_Form as Ui_MainWindow
from ui_main_screen_0 import Ui_Form as Ui_MyWindow
from ui_quad_screen_2 import Ui_Form as Ui_Form_Quadratic
from ui_newt_mass_7 import Ui_Form as Ui_Form_NewtMass
from ui_work_screen_4 import Ui_Form as Ui_Form_Work
from ui_speed_screen_5 import Ui_Form as Ui_Form_Speed
from ui_newt_home_3 import Ui_Form as Ui_Form_NewtHome
from ui_newt_acceleration_8 import Ui_Form as Ui_Form_NewtAcceleration
from ui_newt_force_9 import Ui_Form as Ui_Form_NewtForce
from ui_work_D_10 import Ui_Form as Ui_Form_WorkD
from ui_work_W_12 import Ui_Form as Ui_Form_WorkW
from ui_work_F_11 import Ui_Form as Ui_Form_WorkF
from ui_speed_distance_13 import Ui_Form as Ui_Form_SpeedDistance
from ui_speed_time_14 import Ui_Form as Ui_Form_SpeedTime
from ui_speed_speed_15 import Ui_Form as Ui_Form_SpeedSpeed
from ui_kin_E_18 import Ui_Form as Ui_Form_KineticEnergy
from ui_kin_m_16 import Ui_Form as Ui_Form_KineticMass
from ui_kin_s_17 import Ui_Form as Ui_Form_KineticSpeed
class Calc(QMainWindow):
    def __init__(self, stackWidget):
        super(Calc, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        # Connect all your buttons here
        self.ui.pushButton_2.clicked.connect(self.Return)
        self.ui.pushButton_1.clicked.connect(self.gotoQuadratic)
        self.ui.pushButton_3.clicked.connect(self.gotoNewt)
        self.ui.pushButton_4.clicked.connect(self.gotoWork)
        self.ui.pushButton_5.clicked.connect(self.gotoSpeed)
        self.ui.pushButton.clicked.connect(self.gotoKine)

    # Implement all your navigation methods
    def gotoNewt(self):
        self.stackWidget.setCurrentIndex(3)

    def gotoWork(self):
        self.stackWidget.setCurrentIndex(4)

    def gotoQuadratic(self):
        self.stackWidget.setCurrentIndex(2)

    def gotoSpeed(self):
        self.stackWidget.setCurrentIndex(5)

    def gotoKine(self):
        self.stackWidget.setCurrentIndex(6)

    def Return(self):
        self.stackWidget.setCurrentIndex(0)

class Quadratic(QMainWindow):
    def __init__(self, stackWidget):
        super(Quadratic, self).__init__()
        self.ui = ui_quad_screen_2.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.a = self.ui.a_DSB.value()
        self.b = self.ui.b_DSB.value()
        self.c = self.ui.c_DSB.value()

        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.resultLabel.setText('Here the result will be displayed')

        self.ui.a_DSB.valueChanged.connect(self.calcQuad)
        self.ui.b_DSB.valueChanged.connect(self.calcQuad)
        self.ui.c_DSB.valueChanged.connect(self.calcQuad)

    def Return(self):
        self.stackWidget.setCurrentIndex(1)

    def calcQuad(self):
        self.a = self.ui.a_DSB.value()
        self.b = self.ui.b_DSB.value()
        self.c = self.ui.c_DSB.value()
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if self.a != 0:
            if discriminant < 0:
                self.ui.resultLabel.setText("The Discriminant is inferior to zero.")
            elif discriminant == 0:
                x = (-self.b) / (2 * self.a)
                self.ui.resultLabel.setText(f"x: {x}")
            else:
                x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
                x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
                self.ui.resultLabel.setText(f"x1: {x1:.4f} and x2: {x2:.4f}")
        else:
            self.ui.resultLabel.setText("Can't divide by 0")

class Newton_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Newton_homepage, self).__init__()
        self.ui = ui_newt_home_3.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton_4.clicked.connect(self.Return)
        self.ui.pushButton_1.clicked.connect(self.gotoNewt_mass)
        self.ui.pushButton_2.clicked.connect(self.gotoNewt_acceleration)
        self.ui.pushButton_3.clicked.connect(self.gotoNewt_force)

    def gotoNewt_mass(self):
        self.stackWidget.setCurrentIndex(7)

    def gotoNewt_acceleration(self):
        self.stackWidget.setCurrentIndex(8)

    def gotoNewt_force(self):
        self.stackWidget.setCurrentIndex(9)

    def Return(self):
        self.stackWidget.setCurrentIndex(3)

class Newt_mass(QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_mass, self).__init__()
        self.ui = ui_newt_mass_7.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.resultLabel.setText('Here the result will be displayed')
        self.a = self.ui.a_DSB.value()
        self.F = self.ui.f_DSB.value()
        self.ui.a_DSB.valueChanged.connect(self.calcNewton)
        self.ui.f_DSB.valueChanged.connect(self.calcNewton)

    def calcNewton(self):
        self.a = self.ui.a_DSB.value()
        self.F = self.ui.f_DSB.value()
        try:
            self.m = self.F / self.a
            self.ui.resultLabel.setText(f"The mass is equal to {self.m:.2f} kg.")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Newt_acceleration(QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_acceleration, self).__init__()
        self.ui = ui_newt_acceleration_8.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.m = self.ui.m_DSB.value()
        self.F = self.ui.f_DSB.value()
        self.ui.m_DSB.valueChanged.connect(self.calcNewton)
        self.ui.f_DSB.valueChanged.connect(self.calcNewton)

    def calcNewton(self):
        self.m = self.ui.m_DSB.value()
        self.F = self.ui.f_DSB.value()
        try:
            a = self.F / self.m
            self.ui.resultLabel.setText(f"The acceleration is equal to {a:.2f}.")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Newt_force(QMainWindow):
    def __init__(self, stackWidget):
        super(Newt_force, self).__init__()
        self.ui = ui_newt_force_9.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.m = self.ui.m_DSB.value()
        self.a = self.ui.a_DSB.value()
        self.ui.m_DSB.valueChanged.connect(self.calcNewton)
        self.ui.a_DSB.valueChanged.connect(self.calcNewton)

    def calcNewton(self):
        self.m = self.ui.m_DSB.value()
        self.a = self.ui.a_DSB.value()
        try:
            self.F = self.m * self.a
            self.ui.resultLabel.setText(f"The value of the Force is {self.F:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Work_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Work_homepage, self).__init__()
        self.ui = ui_work_screen_4.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.pushButton_2.clicked.connect(self.gotoWo_D)
        self.ui.pushButton_3.clicked.connect(self.gotoWo_F)
        self.ui.pushButton_4.clicked.connect(self.gotoWo_W)

    def gotoWo_D(self):
        self.stackWidget.setCurrentIndex(10)

    def gotoWo_F(self):
        self.stackWidget.setCurrentIndex(11)

    def gotoWo_W(self):
        self.stackWidget.setCurrentIndex(12)

    def Return(self):
        self.stackWidget.setCurrentIndex(1)

class Work_D(QMainWindow):
    def __init__(self, stackWidget):
        super(Work_D, self).__init__()
        self.ui = ui_work_D_10.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.w = self.ui.w_DSB.value()
        self.ui.F_DSB.valueChanged.connect(self.calcWork)
        self.ui.c_DSB.valueChanged.connect(self.calcWork)
        self.ui.d_DSB.valueChanged.connect(self.calcWork)
        self.ui.w_DSB.valueChanged.connect(self.calcWork)

    def calcWork(self):
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.w = self.ui.w_DSB.value()

        try:
            self.W = self.F * (self.c * self.d * self.w)
            self.ui.resultLabel.setText(f"The work is equal to {self.W:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Work_F(QMainWindow):
    def __init__(self, stackWidget):
        super(Work_F, self).__init__()
        self.ui = ui_work_F_11.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.w = self.ui.W_DSB.value()
        self.ui.c_DSB.valueChanged.connect(self.calcWork)
        self.ui.d_DSB.valueChanged.connect(self.calcWork)
        self.ui.W_DSB.valueChanged.connect(self.calcWork)

    def calcWork(self):
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.w = self.ui.W_DSB.value()

        try:
            self.F = (self.ui.c * self.d * self.w)
            self.ui.resultLabel.setText(f"The work is equal to {self.F:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Work_W(QMainWindow):
    def __init__(self, stackWidget):
        super(Work_W, self).__init__()
        self.ui = ui_work_W_12.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()
        self.ui.F_DSB.valueChanged.connect(self.calcWork)
        self.ui.c_DSB.valueChanged.connect(self.calcWork)
        self.ui.d_DSB.valueChanged.connect(self.calcWork)

    def calcWork(self):
        self.F = self.ui.F_DSB.value()
        self.c = self.ui.c_DSB.value()
        self.d = self.ui.d_DSB.value()

        try:
            self.w = self.F / (self.c * self.d)
            self.ui.resultLabel.setText(f"The work is equal to {self.w:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Speed_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_homepage, self).__init__()
        self.ui = ui_speed_screen_5.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.pushButton_2.clicked.connect(self.gotoSpeedDistance)
        self.ui.pushButton_3.clicked.connect(self.gotoSpeedTime)
        self.ui.pushButton_4.clicked.connect(self.gotoSpeedSpeed)

    def gotoSpeedDistance(self):
        self.stackWidget.setCurrentIndex(13)

    def gotoSpeedTime(self):
        self.stackWidget.setCurrentIndex(14)

    def gotoSpeedSpeed(self):
        self.stackWidget.setCurrentIndex(15)

    def Return(self):
        self.stackWidget.setCurrentIndex(1)


class Speed_Distance(QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_Distance, self).__init__()
        self.ui = ui_speed_distance_13.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.t_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.s_DSB.valueChanged.connect(self.calcSpeed)

    def calcSpeed(self):
        t = self.ui.t_DSB.value()
        s = self.ui.s_DSB.value()
        try:
            self.d = self.s * self.t
            self.ui.resultLabel.setText(f"The distance is equal to {self.d:.2f} m/s")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")


class Speed_Time(QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_Time, self).__init__()
        self.ui = ui_speed_time_14.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.d_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.s_DSB.valueChanged.connect(self.calcSpeed)

    def calcSpeed(self):
        d = self.ui.d_DSB.value()
        s = self.ui.s_DSB.value()
        try:
            speed = d / s
            self.ui.resultLabel.setText(f"The speed is equal to {speed:.2f} m/s")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")


class Speed_Speed(QMainWindow):
    def __init__(self, stackWidget):
        super(Speed_Speed, self).__init__()
        self.ui = ui_speed_speed_15.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.d_DSB.valueChanged.connect(self.calcSpeed)
        self.ui.t_DSB.valueChanged.connect(self.calcSpeed)

    def calcSpeed(self):
        d = self.ui.d_DSB.value()
        t = self.ui.t_DSB.value()
        try:
            speed = d / t
            self.ui.resultLabel.setText(f"The speed is equal to {speed:.2f} m/s")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")


class Kinetic_homepage(QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic_homepage, self).__init__()
        self.ui = ui_kine_screen_6.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget

        self.ui.pushButton.clicked.connect(self.Return)
        self.ui.pushButton_2.clicked.connect(self.gotoKinMass)
        self.ui.pushButton_3.clicked.connect(self.gotoKinSpeed)
        self.ui.pushButton_4.clicked.connect(self.gotoKinEnergy)

    def gotoKinMass(self):
        self.stackWidget.setCurrentIndex(16)

    def gotoKinSpeed(self):
        self.stackWidget.setCurrentIndex(17)

    def gotoKinEnergy(self):
        self.stackWidget.setCurrentIndex(18)

    def Return(self):
        self.stackWidget.setCurrentIndex(1)


class Kinetic_mass(QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic_mass, self).__init__()
        self.ui = ui_kin_m_16.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.resultLabel.setText('Here the result will be displayed')
        self.ui.s_DSB.valueChanged.connect(self.calcKinetic)
        self.ui.e_DSB.valueChanged.connect(self.calcKinetic)

    def calcKinetic(self):
        self.s = self.ui.s_DSB.value()
        self.e = self.ui.e_DSB.value()
        try:
            m = (self.e * 2)/self.v ** 2
            self.ui.resultLabel.setText(f"The mass is equal to {m:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")


class Kinetic_speed(QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic_speed, self).__init__()
        self.ui = ui_kin_s_17.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.resultLabel.setText('Here the result will be displayed')
        self.ui.e_DSB.valueChanged.connect(self.calcKinetic)
        self.ui.m_DSB.valueChanged.connect(self.calcKinetic)

    def calcKinetic(self):
        self.K = self.ui.e_DSB.value()
        self.m = self.ui.m_DSB.value()
        try:
            self.v = math.sqrt((2 * self.e) / self.m)
            self.ui.resultLabel.setText(f"The speed is equal to {self.v:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")


class Kinetic_energy(QMainWindow):
    def __init__(self, stackWidget):
        super(Kinetic_energy, self).__init__()
        self.ui = ui_kin_E_18.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.resultLabel.setText('Here the result will be displayed')
        self.ui.S_DSB.valueChanged.connect(self.calcKinetic)
        self.ui.m_DSB.valueChanged.connect(self.calcKinetic)

    def calcKinetic(self):
        self.S = self.ui.S_DSB.value()
        self.m = self.ui.m_DSB.value()
        try:
            self.K = (self.m * (self.S ** 2)) / 2
            self.ui.resultLabel.setText(f"The kinetic energy is equal to {self.K:.2f}")
        except ZeroDivisionError:
            self.ui.resultLabel.setText("Can't divide by Zero")

class Ui_Form_GraphGenerator(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.plotWidget = QtWidgets.QWidget(Form)
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout.addWidget(self.plotWidget)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.verticalLayout.addWidget(self.canvas)
        self.plotBtn = QtWidgets.QPushButton(Form)
        self.plotBtn.setObjectName("plotBtn")
        self.verticalLayout.addWidget(self.plotBtn)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Graph Generator"))
        self.plotBtn.setText(_translate("Form", "Plot Graph"))

class GraphGenerator(QMainWindow):
    def __init__(self, stackWidget):
        super(GraphGenerator, self).__init__()
        self.ui = Ui_Form_GraphGenerator()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.plotBtn.clicked.connect(self.plotGraph)

    def plotGraph(self):
        x = list(range(1, 11))
        y = [random.randint(1, 100) for _ in x]

        self.ui.figure.clear()
        ax = self.ui.figure.add_subplot(111)
        ax.plot(x, y, marker='o', linestyle='-', color='b', label='Data')
        ax.set_title('Random Data Plot')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.xaxis.set_major_locator(MaxNLocator(integer=True))
        ax.legend()
        ax.grid(True)
        self.ui.canvas.draw()

class MyWindow(QMainWindow):
    def __init__(self, stackWidget):
        super(MyWindow, self).__init__()
        self.ui = ui_main_screen_0.Ui_Form()
        self.ui.setupUi(self)
        self.stackWidget = stackWidget
        self.ui.pushButton_2.clicked.connect(self.gotoGraphGenerator)
        self.ui.pushButton.clicked.connect (self.gotoCalc)

    def gotoCalc (self):
        self.stackWidget.setCurrentIndex (1)

    def gotoGraphGenerator(self):
        self.stackWidget.setCurrentIndex(19)  

def main():
    app = QApplication(sys.argv)
    stackWidget = QtWidgets.QStackedWidget()

    main_window = MyWindow(stackWidget)
    calc_window = Calc(stackWidget)
    graph_window = GraphGenerator(stackWidget)
    quadr_window = Quadratic(stackWidget)
    newt_window = Newton_homepage(stackWidget)
    work_window = Work_homepage(stackWidget)
    speed_window = Speed_homepage(stackWidget)
    kine_window = Kinetic_homepage(stackWidget)
    newt__window_m = Newt_mass(stackWidget)
    newt__window_a = Newt_acceleration(stackWidget)
    newt__window_F = Newt_force(stackWidget)
    work_window_d = Work_D(stackWidget)
    work_window_w = Work_W(stackWidget)
    work_window_f = Work_F(stackWidget)
    speed_window_d = Speed_Distance(stackWidget)
    speed_window_t = Speed_Time(stackWidget)
    speed_window_s = Speed_Speed(stackWidget)
    kine_window_m = Kinetic_mass(stackWidget)
    kine_window_s = Kinetic_speed(stackWidget)
    kine_window_k = Kinetic_energy(stackWidget)
    
    stackWidget.addWidget(main_window)
    stackWidget.addWidget(calc_window)
    stackWidget.addWidget(quadr_window)
    stackWidget.addWidget (newt_window)
    stackWidget.addWidget(work_window)
    stackWidget.addWidget(speed_window)
    stackWidget.addWidget(kine_window)
    stackWidget.addWidget(newt__window_m)
    stackWidget.addWidget (newt__window_a)
    stackWidget.addWidget (newt__window_F)
    stackWidget.addWidget (work_window_d)
    stackWidget.addWidget (work_window_f)
    stackWidget.addWidget (work_window_w)
    stackWidget.addWidget (speed_window_d)
    stackWidget.addWidget (speed_window_t)
    stackWidget.addWidget (speed_window_s)
    stackWidget.addWidget (kine_window_m)
    stackWidget.addWidget (kine_window_s)
    stackWidget.addWidget (kine_window_k)
    stackWidget.addWidget (graph_window)
    
    stackWidget.setCurrentIndex(0)
    stackWidget.show()
    
    sys.exit(app.exec_())

main()