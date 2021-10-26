from os import environ
from PyQt5 import QtWidgets, uic
import sys


# Main class for initializing main app window
class MainScreen(QtWidgets.QMainWindow):

    # Initialization of welcome screen, connecting buttons to functions
    def __init__(self):
        super(MainScreen, self).__init__()
        uic.loadUi('welcome_screen.ui', self)
        self.login.clicked.connect(self.gotologin)

    # Function of "Zaloguj" button in main window screen
    def gotologin(self):
        login = LoginScreen()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex() + 1)


# Class initialization of login screen
class LoginScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login_screen.ui", self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.login_function)

    # Function of "Zaloguj" button in login screen
    def login_function(self):
        user = self.login_field.text()
        password = self.password_field.text()

        if len(user) == 0 or len(password) == 0:
            self.login_error.setText("Proszę uzupełnić wszystkie pola.")


# Basic main init (loading Qt functions, screen resolution,
# showing result on the screen)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(win)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()
    sys.exit(app.exec_())
