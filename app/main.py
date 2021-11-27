from os import environ

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QApplication
import sys


# Main class for initializing main app window
class MainScreen(QMainWindow):

    # Initialization of welcome screen, connecting buttons to functions
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi('welcome_screen.ui', self)
        self.loginbtn.clicked.connect(self.gotologin)
        self.accountbtn.clicked.connect(self.gotoCAccount)
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.oldPos = self.pos()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def gotoCAccount(self):
        create_account = CreateAccountScreen()
        widget.addWidget(create_account)
        widget.setCurrentIndex(widget.currentIndex() + 2)

    # Function of "Zaloguj" button in main window screen
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccountScreen(QMainWindow):
    def __init__(self):
        super(CreateAccountScreen, self).__init__()
        uic.loadUi("createAccount_screen.ui", self)
        self.exitbtn.clicked.connect(lambda: widget.close())


# Class initialization of login screen
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login_screen.ui", self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbtn.clicked.connect(self.login_function)
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.accountbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() + 1))
        self.oldPos = self.pos()

    # Function of "Zaloguj" button in login screen
    def login_function(self):
        user = self.login_field.text()
        password = self.password_field.text()

        if len(user) == 0 or len(password) == 0:
            self.login_error.setText("Proszę uzupełnić wszystkie pola.")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


# Basic main init (loading Qt functions, screen resolution,
# showing result on the screen)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    welcome_screen = MainScreen()
    login_screen = LoginScreen()
    account_screen = CreateAccountScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome_screen)
    widget.addWidget(login_screen)
    widget.addWidget(account_screen)
    widget.setFixedSize(361, 471)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
    widget.show()
    sys.exit(app.exec_())
