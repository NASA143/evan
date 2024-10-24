import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sqlite3



SESSION = {
    'status': False,
    'user_name': '',
    'chats_with': '',
}

connection = sqlite3.connect('db/main_database.db')
cursor = connection.cursor()

class Chats(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/chats.ui', self)
        self.chats = []
        for i in SESSION['chats_with']:
            cursor.execute(f"SELECT name FROM users WHERE id = '{i}'")
            self.list_chats.addItem(cursor.fetchall()[0][0])



class Login(QMainWindow):
    def __init__(self):
        global SESSION
        super().__init__()
        uic.loadUi('uic/login.ui', self)

        self.btn_log.clicked.connect(self.login)
        self.btn_reg.clicked.connect(self.register)

    def login(self):
        cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_log.text()}'")
        res = cursor.fetchall()

        if res:
            if res[0][2] == self.user_password_log.text():
                global SESSION
                SESSION['status'] = True
                SESSION['user_name'] = res[0][1]
                SESSION['chats_with'] = eval(res[0][3])
                self.chats_window = Chats()
                self.chats_window.show()
                self.hide()
            else:
                print('Не верный пароль')
        else:
            print('Не верный логин')

    def register(self):
        if self.user_password_reg.text() == self.user_passwordrep_reg.text():
            cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_reg.text()}'")
            res = cursor.fetchall()
            if not res:
                cursor.execute(f"INSERT INTO users (name, password) VALUES ('{self.user_login_reg.text()}', '{self.user_password_reg.text()}')")
                connection.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())

