import PyQt5 as qt

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt

import sys, math, dill, time

class Calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setSpacing(0)
        self.counter = 0
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)

        self._createHeader()
        self._createDisplay()
        self._createMem()
        self._createButtons()

    def _createDisplay(self):
        self.answer = QLabel()
        self.answer.setText("")
        self.answer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.answer.setAlignment(qt.QtCore.Qt.AlignRight)
        self.answer.setObjectName("answer")
        self.generalLayout.addWidget(self.answer)

        self.display = QLineEdit()
        self.display.setFixedHeight(140)
        self.display.setAlignment(qt.QtCore.Qt.AlignRight)
        self.generalLayout.addWidget(self.display)

    def _createHeader(self):
        layout = QGridLayout()
        self.changeModes = QPushButton("☰")
        self.changeModes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.changeModes.setObjectName("top")
        self.changeModes.setFixedWidth(25)
        layout.addWidget(self.changeModes, 0, 0)
        self.changeModes.clicked.connect(self.mem)

        self.name = QLabel()
        self.name.setText("     Standard")
        self.name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.name.setAlignment(qt.QtCore.Qt.AlignLeft)
        layout.addWidget(self.name, 0, 1)

        self.history = QPushButton("Ø")
        self.history.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.history.setObjectName("top")
        self.history.setFixedWidth(25)
        layout.addWidget(self.history, 0, 2)
        self.history.clicked.connect(self.mem)

        layout.setSpacing(0)
        self.generalLayout.addLayout(layout)

    def _createMem(self):
        layout = QGridLayout()
        self.MC = QPushButton("MC")
        self.MC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MC.setObjectName("mem")
        self.MC.clicked.connect(self.mem)

        layout.addWidget(self.MC, 0, 0)

        self.MR = QPushButton("MR")
        self.MR.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MR.setObjectName("mem")
        self.MR.clicked.connect(self.mem)
        layout.addWidget(self.MR, 0, 1)


        self.Mplus = QPushButton("M+")
        self.Mplus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mplus.setObjectName("mem")
        self.Mplus.clicked.connect(self.mem)
        layout.addWidget(self.Mplus, 0, 2)

        self.Mminus = QPushButton("M-")
        self.Mminus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mminus.setObjectName("mem")
        self.Mminus.clicked.connect(self.mem)
        layout.addWidget(self.Mminus, 0, 3)

        self.MS = QPushButton("MS")
        self.MS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MS.setObjectName("mem")
        self.MS.clicked.connect(self.mem)
        layout.addWidget(self.MS, 0, 4)

        self.Mstar = QPushButton("M*")
        self.Mstar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mstar.setObjectName("mem")
        self.Mstar.clicked.connect(self.mem)
        layout.addWidget(self.Mstar, 0, 5)

        self.generalLayout.addLayout(layout)

    def _createButtons(self):
        self.buttons = {}
        self.functions = {}

        buttonslayout = QGridLayout()
        self.buttons = {

            '7': (2, 0),
            '8': (2, 1),
            '9': (2, 2),
            '4': (3, 0),
            '5': (3, 1),
            '6': (3, 2),
            '1': (4, 0),
            '2': (4, 1),
            '3': (4, 2),
            '0': (5, 1),
        }

        self.extras = {
            "%": (0,0),
            "√":(0, 1),
            "x²": (0, 2),
            '1/x': (0, 3),
            'CE': (1, 0),
            'C': (1, 1),
            "⮨": (1, 2),
            "±": (5, 0),
            '.': (5, 2),
        }

        self.functions = {
            '/': (1, 3),
            '*': (2, 3),
            '-': (3, 3),
            '+': (4, 3),
            '=': (5, 3),
        }

        for text, pos in self.buttons.items():
            self.buttons[text] = QPushButton(text)
            # self.buttons[text].setFixedSize(80, 40)
            self.buttons[text].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            buttonslayout.addWidget(self.buttons[text], pos[0], pos[1])

        for text, pos in self.functions.items():
            self.functions[text] = QPushButton(text)
            # self.buttons[text].setFixedSize(80, 40)
            self.functions[text].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.functions[text].setObjectName("functions")
            buttonslayout.addWidget(self.functions[text], pos[0], pos[1])

        for text, pos in self.extras.items():
            self.extras[text] = QPushButton(text)
            # self.buttons[text].setFixedSize(80, 40)
            self.extras[text].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.extras[text].setObjectName("extras")
            buttonslayout.addWidget(self.extras[text], pos[0], pos[1])

        self.functions["+"].clicked.connect(self.add)
        self.functions["-"].clicked.connect(self.sub)
        self.functions["*"].clicked.connect(self.mul)
        self.functions["/"].clicked.connect(self.div)
        self.functions["="].clicked.connect(self.eq)

        self.buttons["0"].clicked.connect(self.zero)
        self.buttons["1"].clicked.connect(self.one)
        self.buttons["2"].clicked.connect(self.two)
        self.buttons["3"].clicked.connect(self.three)
        self.buttons["4"].clicked.connect(self.four)
        self.buttons["5"].clicked.connect(self.five)
        self.buttons["6"].clicked.connect(self.six)
        self.buttons["7"].clicked.connect(self.seven)
        self.buttons["8"].clicked.connect(self.eight)
        self.buttons["9"].clicked.connect(self.nine)

        self.extras["CE"].clicked.connect(self.clear)
        self.extras["C"].clicked.connect(self.clear)
        self.extras["⮨"].clicked.connect(self.backspace)
        self.extras["%"].clicked.connect(self.per)
        self.extras["√"].clicked.connect(self.root)
        self.extras["x²"].clicked.connect(self.sq)
        self.extras["1/x"].clicked.connect(self.inv)

        buttonslayout.setSpacing(3)
        self.generalLayout.addLayout(buttonslayout)

    def appendDisplay(self, s):
        pass

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.eq()

    def add(self):
        self.logic()
        text = self.answer.text()
        self.answer.setText(text + "+")
        self.display.setText("")

    def sub(self):
        self.logic()
        text = self.answer.text()
        self.answer.setText(text + "-")
        self.display.setText("")

    def mul(self):
        self.logic()
        text = self.answer.text()
        self.answer.setText(text + "*")
        self.display.setText("")

    def div(self):
        self.logic()
        text = self.answer.text()
        self.answer.setText(text + "/")
        self.display.setText("")

    def per(self):
        self.answer.setText(str(self.answer.text() + self.display.text()))
        try:
            self.answer.setText(str(eval(self.answer.text()) / 100))
            print(self.answer.text())
        except Exception as e:
            print(e)

        self.display.setText("")

    def root(self):
        self.answer.setText(str(self.answer.text() + self.display.text()))
        try:
            self.answer.setText(str(math.sqrt(eval(self.answer.text()))))
            print(self.answer.text())
        except Exception as e:
            print(e)

        self.display.setText("")

    def sq(self):
        self.answer.setText(str(self.answer.text() + self.display.text()))
        try:
            self.answer.setText(str(eval(self.answer.text()) ** 2))
            print(self.answer.text())
        except Exception as e:
            print(e)

        self.display.setText("")

    def inv(self):
        self.answer.setText(str(self.answer.text() + self.display.text()))
        try:
            self.answer.setText(str(1/eval(self.answer.text())))
            print(self.answer.text())
        except Exception as e:
            print(e)

        self.display.setText("")

    def mem(self):
        f = open("add.lib", "rb")
        lib = dill.load(f)
        f.close()
        self.display.setText(str(lib.out(self.counter)))
        self.counter += 1
        if self.counter >= 14:
            self.counter = 0

    def zero(self):
        text = self.display.text()
        self.display.setText(text + "0")
    def one(self):
        text = self.display.text()
        self.display.setText(text + "1")
    def two(self):
        text = self.display.text()
        self.display.setText(text + "2")
    def three(self):
        text = self.display.text()
        self.display.setText(text + "3")
    def four(self):
        text = self.display.text()
        self.display.setText(text + "4")
    def five(self):
        text = self.display.text()
        self.display.setText(text + "5")
    def six(self):
        text = self.display.text()
        self.display.setText(text + "6")
    def seven(self):
        text = self.display.text()
        self.display.setText(text + "7")
    def eight(self):
        text = self.display.text()
        self.display.setText(text + "8")
    def nine(self):
        text = self.display.text()
        self.display.setText(text + "9")

    def eq(self):
        self.logic()
        text = self.answer.text()
        self.display.setText(text)
        self.answer.setText("")

    def clear(self):
        self.display.setText("")
        self.answer.setText("")

    def backspace(self):
        text = self.display.text()
        self.display.setText(text[:-1])

    def logic(self):
        self.answer.setText(str(self.answer.text() + self.display.text()))
        try:
            self.answer.setText(str(eval(self.answer.text())))
            # print(self.answer.text())
        except Exception as e:
            self.answer.setText("ERROR")
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calc()
    window.setWindowTitle("Calculator")
    window.resize(300,600)

    window.setStyleSheet(open("styles.css", "r").read())

    window.show()

    sys.exit(app.exec_())
