
from PyQt5 import QtCore, QtGui, QtWidgets
import NewGuiBot
import mysql.connector


ver = "3.0"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(722, 883)
        MainWindow.setMinimumSize(QtCore.QSize(722, 883))
        MainWindow.setMaximumSize(QtCore.QSize(722, 883))
        MainWindow.setStyleSheet("")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(230, 50, 241, 111))
        self.label_10.setStyleSheet("border-image: url(:/logo/logo white bez tla.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.BG = QtWidgets.QLabel(self.centralwidget)
        self.BG.setGeometry(QtCore.QRect(50, 0, 602, 841))
        self.BG.setMinimumSize(QtCore.QSize(600, 840))
        self.BG.setStyleSheet("background-color: rgb(40,36,46);\n"
"border-radius:50px;\n"
"")
        self.BG.setText("")
        self.BG.setObjectName("BG")
        self.minimaliseButton = QtWidgets.QToolButton(self.centralwidget)
        self.minimaliseButton.setGeometry(QtCore.QRect(570, 20, 16, 16))
        self.minimaliseButton.setStyleSheet("background-color: rgb(255, 189, 68);\n"
"image: url(:/min/minimize.png);\n"
"border-radius:8px;\n"
"")
        self.minimaliseButton.setText("")
        self.minimaliseButton.setIconSize(QtCore.QSize(25, 25))
        self.minimaliseButton.setObjectName("minimaliseButton")
        self.CloseButton = QtWidgets.QToolButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(590, 20, 16, 16))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(7)
        font.setBold(False)
        font.setWeight(50)
        self.CloseButton.setFont(font)
        self.CloseButton.setToolTipDuration(1)
        self.CloseButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CloseButton.setStyleSheet("background-color: rgb(255, 96, 92);\n"
"image: url(:/ex/close.png);\n"
"border-radius:8px;\n"
"")
        self.CloseButton.setText("")
        self.CloseButton.setIconSize(QtCore.QSize(25, 25))
        self.CloseButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.CloseButton.setAutoRaise(False)
        self.CloseButton.setObjectName("CloseButton")
        self.Password = QtWidgets.QLineEdit(self.centralwidget)
        self.Password.setGeometry(QtCore.QRect(120, 430, 461, 61))
        self.Password.setStyleSheet("color: rgba(255, 255,255,255);\n"
"background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 255);\n"
"padding-bottom:10px;")
        self.Password.setText("")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setAlignment(QtCore.Qt.AlignCenter)
        self.Password.setObjectName("Password")
        self.Login = QtWidgets.QLineEdit(self.centralwidget)
        self.Login.setGeometry(QtCore.QRect(120, 320, 461, 61))
        self.Login.setStyleSheet("color: rgba(255, 255,255,255);\n"
"background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom: 2px solid rgba(255, 255, 255, 255);\n"
"padding-bottom:10px;\n"
"")
        self.Login.setText("")
        self.Login.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.Login.setAlignment(QtCore.Qt.AlignCenter)
        self.Login.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.Login.setObjectName("Login")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(190, 200, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label_3.setFont(font)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 430, 51, 41))
        self.label_2.setStyleSheet("image: url(:/password/password-64.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 320, 51, 41))
        self.label_4.setStyleSheet("image: url(:/login/login-64.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.LoginButton = QtWidgets.QPushButton(self.centralwidget)
        self.LoginButton.setGeometry(QtCore.QRect(250, 570, 191, 23))
        self.LoginButton.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(79, 74, 84);\n"
"color: rgb(255, 255, 255);")
        self.LoginButton.setObjectName("LoginButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(120, 670, 461, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 685, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255,255,255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.facebookButton = QtWidgets.QPushButton(self.centralwidget)
        self.facebookButton.setGeometry(QtCore.QRect(270, 730, 41, 41))
        self.facebookButton.setStyleSheet("border-image: url(:/fb/facebook-64.png);")
        self.facebookButton.setText("")
        self.facebookButton.setObjectName("facebookButton")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 730, 41, 41))
        self.pushButton.setStyleSheet("border-image: url(:/ig/instagram-64.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 730, 41, 41))
        self.pushButton_2.setStyleSheet("border-image: url(:/email/mail-64.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(110, 20, 21, 16))
        self.label_14.setStyleSheet("color:rgb(255, 255, 255);")
        self.label_14.setObjectName("label_14")
        self.Ver = QtWidgets.QLabel(self.centralwidget)
        self.Ver.setGeometry(QtCore.QRect(130, 20, 61, 16))
        self.Ver.setStyleSheet("color:rgb(255, 255, 255);")
        self.Ver.setAlignment(QtCore.Qt.AlignCenter)
        self.Ver.setObjectName("Ver")
        self.BG.raise_()
        self.minimaliseButton.raise_()
        self.CloseButton.raise_()
        self.label_10.raise_()
        self.Password.raise_()
        self.Login.raise_()
        self.label_3.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.LoginButton.raise_()
        self.line.raise_()
        self.label.raise_()
        self.facebookButton.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.label_14.raise_()
        self.Ver.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.Login, self.Password)
        MainWindow.setTabOrder(self.Password, self.LoginButton)
        MainWindow.setTabOrder(self.LoginButton, self.facebookButton)
        MainWindow.setTabOrder(self.facebookButton, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.CloseButton)
        MainWindow.setTabOrder(self.CloseButton, self.minimaliseButton)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Password.setPlaceholderText(_translate("MainWindow", "Hasło"))
        self.Login.setPlaceholderText(_translate("MainWindow", "Login"))
        self.label_3.setText(_translate("MainWindow", "Zaloguj sie do Bota"))
        self.LoginButton.setText(_translate("MainWindow", "Zaloguj"))
        self.label.setText(_translate("MainWindow", "Kontakt"))
        self.label_14.setText(_translate("MainWindow", "Ver:"))
        self.Ver.setText(_translate("MainWindow", "testowa"))

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        ui = Ui_MainWindow()
        ui.setupUi(self)
        ui.CloseButton.clicked.connect(self.close)
        ui.minimaliseButton.clicked.connect(self.minimized)
        ui.Ver.setText(ver)
        ui.LoginButton.clicked.connect(self.Login)
        global l, p
        l = ui.Login
        p = ui.Password

        ### Funkcjonalności pozostałych Przycisków

    def close(self):
        app.exit()

    def minimized(self):
        self.showMinimized()

    def mousePressEvent(self, event):  # +
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):  # !!!
        if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

    def Login(self):
        login = l.text()
        password = p.text()
        testl = "Daniel"
        testp = "1234"
        print("Login: "+login+" Password: "+password)

        if(login==testl and password == testp):
                print("poprawne Dane")

        else:
              print("nieporpawne dane")

if __name__ == "__main__":
    import sys, res

    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
