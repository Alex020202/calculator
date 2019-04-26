from PySide2 import QtCore, QtGui, QtWidgets
import sys
from calculator import Ui_MainWindow
import math
# Create application
app = QtWidgets.QApplication(sys.argv)

# Create form and init Calc
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Hook Logic

def ButPress(key):
    ui.textEdit.insert(key)


ui.Button_1.clicked.connect(lambda:ButPress("1"))
ui.Button_2.clicked.connect(lambda:ButPress("2"))
ui.Button_3.clicked.connect(lambda:ButPress("3"))
ui.Button_4.clicked.connect(lambda:ButPress("4"))
ui.Button_5.clicked.connect(lambda:ButPress("5"))
ui.Button_6.clicked.connect(lambda:ButPress("6"))
ui.Button_7.clicked.connect(lambda:ButPress("7"))
ui.Button_8.clicked.connect(lambda:ButPress("8"))
ui.Button_9.clicked.connect(lambda:ButPress("9"))
ui.Button_10.clicked.connect(lambda:ButPress("0"))


def calc():
    global x, y, oper
    if oper == "+":
        result = x + y
    elif oper == "-":
        result = x - y
    elif oper == "*":
        result = x * y
    elif oper == "/":
        result = x / y
    elif oper == "^":
        result = x ** y
    elif oper == "!":
        result = math.factorial(x)
    elif oper == "div":
        result = x // y
    elif oper == "mod":
        result = x % y
    ui.textEdit.insert(str(result))
    print(result)
ui.Button_12.clicked.connect(lambda:operation("+"))
ui.Button_13.clicked.connect(lambda:operation("-"))
ui.Button_14.clicked.connect(lambda:operation("/"))
ui.Button_15.clicked.connect(lambda:operation("*"))
ui.Button_11.clicked.connect(lambda:operation("="))
ui.Button_18.clicked.connect(lambda:operation("^"))
ui.Button_19.clicked.connect(lambda:operation("!"))
ui.Button_20.clicked.connect(lambda:operation("div"))
ui.Button_21.clicked.connect(lambda:operation("mod"))


def operation(key):
    global oper, x, y
    if key != "=" and key != "!":
        mytext = ui.textEdit.text()
        x = int(mytext)
        print(x)
        oper = key
        ui.textEdit.insert(key)
        ui.textEdit.clear()
        ui.lineEdit.setText(str(x) + oper)
    elif key == "=":
        mytext = ui.textEdit.text()
        y = int(mytext)
        print(y)
        ui.textEdit.clear()
        ui.lineEdit.clear()
        ui.textEdit.insert(str(x) + oper + str(y) + key)
        calc()
    elif key == "!":
        mytext = ui.textEdit.text()
        x = int(mytext)
        print(x)
        oper = key
        ui.textEdit.insert(key)
        ui.textEdit.clear()
        ui.textEdit.insert(str(x) + oper + "=")
        calc()

def Restart():
    x = 0
    y = 0
    oper = 0
    ui.textEdit.clear()
ui.Button_17.clicked.connect(lambda: Restart())
# Run main loop
sys.exit(app.exec_())
