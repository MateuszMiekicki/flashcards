from os import environ

from PyQt5 import QtWidgets, uic, QtCore, QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QDesktopWidget, QWidget, QMainWindow, QApplication, QPushButton
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
        widget.setCurrentIndex(widget.currentIndex() + 3)

    # Function of "Zaloguj" button in main window screen
    def gotologin(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CreateAccountScreen(QMainWindow):
    def __init__(self):
        super(CreateAccountScreen, self).__init__()
        uic.loadUi("createAccount_screen.ui", self)
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.backbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 3))

class ForgotPasswordScreen(QMainWindow):
    def __init__(self):
        super(ForgotPasswordScreen, self).__init__()
        uic.loadUi("forgotpassword_screen.ui", self)
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.backbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))


# Class initialization of login screen
class LoginScreen(QMainWindow):
    def __init__(self):
        super(LoginScreen, self).__init__()
        uic.loadUi("login_screen.ui", self)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginbtn.clicked.connect(self.login_function)
        self.accountbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() + 2))
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.backbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() - 1))
        self.forgotpasswordbtn.clicked.connect(lambda: widget.setCurrentIndex(widget.currentIndex() + 1))
        self.oldPos = self.pos()

    # Function of "Zaloguj" button in login screen
    def login_function(self):
        user = self.login_field.text()
        password = self.password_field.text()

        if user == 'admin' and password == 'admin':
            widget.addWidget(FlashcardsScreen())
            widget.setCurrentIndex(widget.currentIndex() + 3)
        if len(user) == 0 or len(password) == 0:
            widget.addWidget(FlashcardsScreen())
            widget.setCurrentIndex(widget.currentIndex() + 3)
            self.login_error.setText("Proszę uzupełnić wszystkie pola.")
        else:
            self.login_error.setText("Błędne dane, spróbuj ponownie")


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

class FlashcardsScreen(QMainWindow):

    # Initialization of welcome screen, connecting buttons to functions
    def __init__(self):
        super(FlashcardsScreen, self).__init__()
        widget.setFixedSize(800, 600)
        uic.loadUi('flashcards_screen.ui', self)
        self.n = 0
        self.m = 0
        self.number_of_groups = 1
        self.exitbtn.clicked.connect(lambda: widget.close())
        self.hidebtn.clicked.connect(self.hide_menu)
        self.flashcards_widget.hide()
        self.flashcards_widget_show = 0
        self.flashcards_card.hide()
        self.flashcards_card_show = 0
        self.edit_buttons.hide()
        self.flashcards_group_edit = 0
        self.addgroup.hide()
        self.addgroup_show = 0
        self.removegroup.hide()
        self.removegroup_show = 0
        self.group_2.hide()
        self.gotogroupsbtn.clicked.connect(self.flashcards_widget_screen)
        self.group_1.clicked.connect(self.flashcards_card_screen)
        self.nextbtn.clicked.connect(self.next_card)
        self.gotoeditorbtn.clicked.connect(self.edit_flashcards)
        self.addgroupbtn.clicked.connect(self.add_group)
        self.removegroupbtn.clicked.connect(self.remove_group)
        self.confirmbtn.clicked.connect(self.add_group_table)
        self.confirmbtn_2.clicked.connect(self.remove_group_table)
        self.logoutbtn.clicked.connect(self.logout_btn)
        self.oldPos = self.pos()
        self.example = [["2+2=?", "4"], ["Wzór na pole kwadratu", "P=a*a"]]

    def hide_menu(self):
        if self.hidebtn.text() == "<-":
            while(self.menu_widget.frameGeometry().width() > 41 or self.menu_widget.frameGeometry().height() > 41):
                if self.menu_widget.frameGeometry().width() > 41:
                    self.menu_widget.resize(self.menu_widget.frameGeometry().width() - 1, self.menu_widget.frameGeometry().height())
                elif self.menu_widget.frameGeometry().height() > 41:
                    self.menu_widget.resize(self.menu_widget.frameGeometry().width(),
                                         self.menu_widget.frameGeometry().height() - 1)
            if self.flashcards_widget_show == 1:
                self.flashcards_widget.resize(781, 561)
                self.flashcards_widget.move(0, 30)
                self.edit_buttons.resize(781, 51)
                self.addgroupbtn.move(170, 10)
                self.removegroupbtn.move(470, 10)
                self.addgroup.move(139, 419)
                self.removegroup.move(440, 419)
            elif self.flashcards_card_show == 1:
                self.flashcards_card.resize(711, 251)
                self.nextbtn.resize(711, 251)
                self.card_inside_txt.resize(641, 141)
                self.flashcards_card.move(45, 160)
                self.count_txt.move(650, 223)
            self.hidebtn.move(5, 10)
            self.hidebtn.setText("->")
        else:
            while (self.menu_widget.frameGeometry().width() < 171 or self.menu_widget.frameGeometry().height() < 601):
                if self.menu_widget.frameGeometry().width() < 171:
                    self.menu_widget.resize(self.menu_widget.frameGeometry().width() + 1,
                                         self.menu_widget.frameGeometry().height())
                elif self.menu_widget.frameGeometry().height() < 601:
                    self.menu_widget.resize(self.menu_widget.frameGeometry().width(),
                                         self.menu_widget.frameGeometry().height() + 1)
            if self.flashcards_widget_show == 1:
                self.flashcards_widget.resize(601, 571)
                self.flashcards_widget.move(180, 30)
                self.edit_buttons.resize(601, 51)
                self.addgroupbtn.move(100, 10)
                self.removegroupbtn.move(380, 10)
                self.addgroup.move(69, 419)
                self.removegroup.move(350, 419)
            elif self.flashcards_card_show == 1:
                self.flashcards_card.resize(541, 251)
                self.nextbtn.resize(541, 251)
                self.card_inside_txt.resize(461, 141)
                self.flashcards_card.move(210, 160)
                self.count_txt.move(476, 223)
            self.hidebtn.move(130, 10)
            self.hidebtn.setText("<-")

    def flashcards_widget_screen(self):
        if self.hidebtn.text() == "<-":
            self.flashcards_widget.resize(601, 571)
            self.flashcards_widget.move(180, 30)
            self.flashcards_card.resize(541, 251)
            self.nextbtn.resize(541, 251)
            self.card_inside_txt.resize(461, 141)
            self.flashcards_card.move(210, 160)
            self.edit_buttons.resize(601, 51)
            self.edit_buttons.move(0, 510)
        elif self.hidebtn.text() == "->":
            self.flashcards_widget.resize(541, 251)
            self.flashcards_widget.move(0, 30)
            self.flashcards_card.resize(711, 251)
            self.nextbtn.resize(711, 251)
            self.card_inside_txt.resize(641, 141)
            self.flashcards_card.move(45, 160)
            self.count_txt.move(650, 223)
            self.edit_buttons.resize(781, 51)
            self.edit_buttons.move(0, 510)
        if self.flashcards_widget_show == 1:
            if self.flashcards_group_edit == 1:
                self.edit_buttons.hide()
                self.flashcards_group_edit = 0
            elif self.flashcards_group_edit == 0:
                self.flashcards_widget.hide()
                self.flashcards_widget_show = 0
            if self.addgroup_show == 1:
                self.addgroup.hide()
                self.addgroup_show = 0
            if self.removegroup_show == 1:
                self.removegroup.hide()
                self.removegroup_show = 0
        elif self.flashcards_widget_show == 0:
            self.flashcards_widget.show()
            self.flashcards_widget_show = 1
            self.edit_buttons.hide()
            self.flashcards_group_edit = 0
        if self.flashcards_card_show == 1:
            self.flashcards_card.hide()
            self.m, self.n = 0, 0
            self.card_inside_txt.setStyleSheet("""
            QLabel#card_inside_txt{
            color: black;}
            """)
            self.flashcards_card_show = 0

    def flashcards_card_screen(self):
        if self.flashcards_widget_show == 1:
            self.flashcards_widget.hide()
            self.flashcards_widget_show = 0
        self.card_inside_txt.setText(self.example[0][0])
        self.count_txt.setText(str(self.m+1) + "/" + str(len(self.example)))
        if self.flashcards_card_show == 0:
            self.flashcards_card.show()
            self.flashcards_card_show = 1
        if self.addgroup_show == 1:
            self.addgroup.hide()
            self.addgroup_show = 0
        if self.removegroup_show == 1:
            self.removegroup.hide()
            self.removegroup_show = 0
        if self.hidebtn.text() == "->":
            if self.flashcards_card_show == 1:
                self.flashcards_card.resize(711, 251)
                self.nextbtn.resize(711, 251)
                self.card_inside_txt.resize(641, 141)
                self.flashcards_card.move(45, 160)
                self.count_txt.move(650, 223)
        self.n += 1

    def next_card(self):
        if self.n==1:
            self.card_inside_txt.setStyleSheet("""
            QLabel#card_inside_txt{
            color: white;}
            """)
        else:
            self.card_inside_txt.setStyleSheet("""
            QLabel#card_inside_txt{
            color: black;}
            """)
        self.card_inside_txt.setText(self.example[self.m][self.n])
        self.count_txt.setText(str(self.m+1) + "/" + str(len(self.example)))
        self.n += 1
        if self.n >=2:
            self.n = 0
            self.m += 1
        if self.m >= len(self.example):
            self.n = 0
            self.m = 0

    def edit_flashcards(self):
        if self.hidebtn.text() == "<-":
            self.flashcards_widget.resize(601, 571)
            self.flashcards_widget.move(180, 30)
            self.flashcards_card.resize(541, 251)
            self.nextbtn.resize(541, 251)
            self.card_inside_txt.resize(461, 141)
            self.flashcards_card.move(210, 160)
            self.edit_buttons.resize(601, 51)
            self.edit_buttons.move(0, 510)
        elif self.hidebtn.text() == "->":
            self.flashcards_widget.resize(541, 251)
            self.flashcards_widget.move(0, 30)
            self.flashcards_card.resize(711, 251)
            self.nextbtn.resize(711, 251)
            self.card_inside_txt.resize(641, 141)
            self.flashcards_card.move(45, 160)
            self.count_txt.move(650, 223)
            self.edit_buttons.resize(781, 51)
            self.edit_buttons.move(0, 510)
        if self.flashcards_widget_show == 0:
            self.flashcards_widget.show()
            self.flashcards_widget_show = 1
        if self.flashcards_group_edit == 0:
            self.edit_buttons.show()
            self.flashcards_group_edit = 1
        elif self.flashcards_group_edit == 1:
            self.edit_buttons.hide()
            self.flashcards_group_edit = 0
        if self.addgroup_show == 1:
            self.addgroup.hide()
            self.addgroup_show = 0
        if self.flashcards_card_show == 1:
            self.flashcards_card.hide()
            self.m, self.n = 0, 0
            self.card_inside_txt.setStyleSheet("""
            QLabel#card_inside_txt{
            color: black;}
            """)
            self.flashcards_card_show = 0

    def add_group(self):
        if self.addgroup_show == 0:
            self.addgroup.show()
            self.addgroup_show = 1
        elif self.addgroup_show == 1:
            self.addgroup.hide()
            self.addgroup_show = 0

    def add_group_table(self):
        self.groupname = self.group_name_txt.text()
        self.group_2.setText(self.groupname)
        self.group_2.show()

    def remove_group(self):
        if self.removegroup_show == 0:
            self.removegroup.show()
            self.removegroup_show = 1
        elif self.removegroup_show == 1:
            self.removegroup.hide()
            self.removegroup_show = 0

    def remove_group_table(self):
        self.groupname_2 = self.group_name_txt_2.text()
        if self.groupname_2 == self.group_2.text():
            self.group_2.hide()

    def logout_btn(self):
        widget.setCurrentIndex(widget.currentIndex() -3)

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
    forgot_password_screen = ForgotPasswordScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome_screen)
    widget.addWidget(login_screen)
    widget.addWidget(forgot_password_screen)
    widget.addWidget(account_screen)
    widget.setFixedSize(361, 471)
    widget.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    widget.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
    widget.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
    widget.show()
    sys.exit(app.exec_())