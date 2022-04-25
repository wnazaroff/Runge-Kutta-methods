import sys
from check import *
from PyQt6 import QtCore, QtGui, QtWidgets


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Вешаем на кнопку функцию RungeKutta
        self.ui.pushButton.clicked.connect(self.RungeKutta)
        # Вешаем на кнопку функцию очистки
        self.ui.pushButton_2.clicked.connect(self.clean)

    # Описываем функцию 
    def RungeKutta(self):
        # Очищаем второе текстовое поле
        self.ui.textEdit_2.setText("")
        # В переменную a получаем текст из x поля ввода
        x = (float(self.ui.textEdit.toPlainText()))
        # В переменную a получаем текст из y поля ввода
        y = (float(self.ui.textEdit_3.toPlainText()))
        # В переменную n получаем текст из n поля ввода
        n = int(self.ui.textEdit_4.toPlainText())
        # В переменную n получаем текст из xn поля ввода
        xn = int(self.ui.textEdit_5.toPlainText())
        # В переменную n получаем текст из функции поля ввода
        fff = str(self.ui.textEdit_6.toPlainText())

        
        # Делаем из текстового поля функцию
        def f(x, y):
            return eval(fff)

        # rezultat=str(float(a)*float(b))
        rezultat = ""
        h = (xn - x) / n
        k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
        dy = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        rezultat = rezultat + "x=" + str("%.3f" % x) + "   y=" + str("%.6f" % y) + "    k1=" + str(
            "%.6f" % k1) + "   k2=" + str("%.6f" % k2) + "  k3=" + str("%.6f" % k3) + "  k4= " + str(
            "%.6f" % k4) + "  dy= " + str("%.6f" % dy) + '\n'
        y = y + dy
        for i in range(1, n + 1):
            x = x + h
            k1 = f(x, y)
            k2 = f(x + h / 2, y + h * k1 / 2)
            k3 = f(x + h / 2, y + h * k2 / 2)
            k4 = f(x + h, y + h * k3)
            dy = h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

            rezultat = rezultat + "x=" + str("%.3f" % x) + "   y=" + str("%.6f" % y) + "    k1=" + str(
                "%.6f" % k1) + "   k2=" + str("%.6f" % k2) + "  k3=" + str("%.6f" % k3) + "  k4= " + str(
                "%.6f" % k4) + "  dy= " + str("%.6f" % dy) + '\n' 
            y = y + dy
        # Выводим в правое поле переменную результат 
        self.ui.textEdit_2.setText(rezultat)
    def clean(self):
        self.ui.textEdit_2.setText('rezultat')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec())
