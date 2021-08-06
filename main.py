import PyQt5 as qt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton, QLineEdit, QVBoxLayout, QMainWindow, QGridLayout, QSizePolicy

from functools import partial
import sys

class Calc(QMainWindow):
    """PyCalc's View (GUI)."""
    def __init__(self):
        """View initializer."""
        super().__init__()
        # Set some main window's properties
        self.setWindowTitle('Calculator')
        # Set the central widget and the general layout
        self.generalLayout = QVBoxLayout()
        self.generalLayout.setSpacing(0)
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)
        self._centralWidget.setLayout(self.generalLayout)
        # Create the display and the buttons
        self._createHeader()
        self._createDisplay()
        self._createMem()
        self._createButtons()

        self.operator = ""
        self.operSet = False
        self.num = None

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

        layout.setSpacing(0)
        self.generalLayout.addLayout(layout)

    def _createMem(self):
        layout = QGridLayout()
        self.MC = QPushButton("MC")
        self.MC.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MC.setObjectName("mem")

        layout.addWidget(self.MC, 0, 0)

        self.MR = QPushButton("MR")
        self.MR.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MR.setObjectName("mem")
        layout.addWidget(self.MR, 0, 1)

        self.Mplus = QPushButton("M+")
        self.Mplus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mplus.setObjectName("mem")
        layout.addWidget(self.Mplus, 0, 2)

        self.Mminus = QPushButton("M-")
        self.Mminus.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mminus.setObjectName("mem")
        layout.addWidget(self.Mminus, 0, 3)

        self.MS = QPushButton("MS")
        self.MS.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.MS.setObjectName("mem")
        layout.addWidget(self.MS, 0, 4)

        self.Mstar = QPushButton("M*")
        self.Mstar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Mstar.setObjectName("mem")
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
        self.functions["="].clicked.connect(self.eval)

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

        # Add buttonsLayout to the general layout
        buttonslayout.setSpacing(3)
        self.generalLayout.addLayout(buttonslayout)

    def appendDisplay(self, s):
        pass

    def add(self):
        text = self.display.text()
        self.logic("+")

    def sub(self):
        text = self.display.text()
        self.logic("-")

    def mul(self):
        text = self.display.text()
        self.logic("*")

    def div(self):
        text = self.display.text()
        self.logic("/")

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


    def eval(self):
        # text = self.answer.text().strip("+").strip("-").strip("*").strip("/")
        self.logic("=")
        self.display.setText(str(self.num))
        self.answer.setText("")
        self.operSet = True

    def clear(self):
        self.display.setText("")
        self.answer.setText("")
        self.num = None

    def backspace(self):
        text = self.display.text()
        self.display.setText(text[:-1])

    def logic(self, func):
        if self.display.text() != "" and self.num != None:
            try:
                if self.operator == "+":
                    self.num = self.num + int(self.display.text())
                elif self.operator == "-":
                    self.num = self.num - int(self.display.text())
                elif self.operator == "*":
                    self.num = self.num * int(self.display.text())
                elif self.operator == "/":
                    self.num = self.num / int(self.display.text())

                self.operator = func
                self.answer.setText(str(self.num) + func)
                self.display.setText("")

            except Exception as e:
                self.display.setText("ERROR")
                self.answer.setText("")
                print(e)

        elif self.display.text() != "":
            self.num = int(self.display.text())
            self.operator = func
            self.answer.setText(str(self.num).strip("+").strip("-").strip("*").strip("/") + func)
            self.display.setText("")

        # elif not self.operSet and self.display.text() != "":
        #     self.operator = func
        #     self.num = int(self.display.text())
        #     self.answer.setText(str(self.num) + func)
        #     self.display.setText("")
        #     self.operSet = True



app = QApplication(sys.argv)
window = Calc()
window.setWindowTitle("Calculator")
window.resize(300,600)
# window.setFixedSize(300, 600)
# window.move(10,10)

window.setStyleSheet(open("styles.css", "r").read())
# hellomsg = QLabel("<h1> This is an hello label </h1>", parent=window)s
# hellomsg.move(10,10)

window.show()

sys.exit(app.exec_())
