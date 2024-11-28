import sys

from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog
import sqlite3
import datetime
import threading

from markdown.treeprocessors import isString

session = {
    'status': False,
    'user_id': None,
    'user_name': '',
    # Тут храняться id юзеров с которыми пользователь имеет чаты
    'chats_with': [],
    # Ативный чат
    'active_chat': '',
    'last_sender': None,
    'user_image': '',
}
# Подключение к БД
connection = sqlite3.connect('db/main_database.db')
cursor = connection.cursor()


# Класс окна с чатами
class Chats(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/chats.ui', self)
        self.chats_data = []
        self.chats_buttons = []
        self.chat_message_now = []

        self.get_data()
        self.print_chats_buttons()

        self.send_msg_btn.clicked.connect(self.send_msg)

        self.find_user_btn.clicked.connect(self.find_user)

        # self.run_every_n_seconds(5, self.example_task)

    def find_user(self):
        cursor.execute(f'''SELECT name FROM users WHERE name = "{self.find_user_input.text()}"''')
        res = cursor.fetchall()
        if res and res[0][0] not in session['chats_with']:
            req = f'{session['chats_with'] + [res[0][0]]}'
            print(req)
            cursor.execute(f'''UPDATE users SET chats_with = "{req}" WHERE id = {session['user_id']}''')
            connection.commit()
            self.get_data()
            self.print_chats_buttons()

    def get_data(self):
        self.chats_data = []
        for i in session['chats_with']:
            cursor.execute(
                f'''SELECT * FROM chats WHERE id_user_from = "{session['user_id']}" AND id_user_to = "{i}" OR id_user_from = "{i}" AND id_user_to = "{session['user_id']}" ORDER BY created_time''')
            self.chats_data.append((i, cursor.fetchall()))


    def print_chats_buttons(self):
        for i in self.chats_buttons:
            print(i)
            self.verticalLayout.removeWidget(i)
            i.deleteLater()
        for i in self.chats_data:
            self.chats_buttons.append(QPushButton(f'{i[0]}', parent=self.scrollAreaWidgetContents))
            self.verticalLayout.addWidget(self.chats_buttons[-1])
            self.chats_buttons[-1].clicked.connect(self.chat_btn_click)
            self.chats_buttons[-1].setStyleSheet("background-color: #fff;\n"
                                                 "border-radius: 5px;\n"
                                                 "color: #000;\n"
                                                 "padding: 10px 10px"
                                                 )
            cursor.execute(f"SELECT image FROM users WHERE id = '{i[0]}'")

            print(cursor.fetchall()[0][0].split('/')[-1])
            self.chats_buttons[-1].setIcon(QIcon(cursor.fetchall()[0][0].split('/')[-1]))
            self.chats_buttons[-1].iconSize = QSize(50, 60)




    def chat_btn_click(self):
        if session['last_sender'] != self.sender():
            session['last_sender'] = self.sender()
        self.active_chat_name.setText(self.sender().text())
        for i in self.chat_message_now:
            self.verticalLayout_2.removeWidget(i)
            i.deleteLater()
        self.chat_message_now = []
        for i in self.chats_data:
            if session['last_sender'].text() in str(i[0]):
                session['active_chat'] = i[0]
                for k in i[1]:
                    self.chat_message_now.append(QLabel(f'{k[3]}', parent=self.chat_area_contents))
                    self.chat_message_now[-1].setStyleSheet("width: 400px;\n"
                                                            "background-color: #fff;\n"
                                                            "border-radius: 20px;\n"
                                                            "color: #000;\n"
                                                            "padding: 10px 10px")
                    self.verticalLayout_2.addWidget(self.chat_message_now[-1])


    def send_msg(self):
        cursor.execute(
            f"INSERT INTO chats (id_user_from, id_user_to, msg, created_time) VALUES ('{session['user_id']}', '{session['active_chat']}', '{self.send_msg_input.text()}', '{datetime.datetime.now()}')")
        connection.commit()
        self.get_data()
        self.chat_btn_click()

    def run_every_n_seconds(self, seconds, action, *args):
        threading.Timer(seconds, self.run_every_n_seconds, [seconds, action] + list(args)).start()
        action(*args)

    def example_task(self):
        self.get_data()
        self.chat_btn_click()


class Login(QMainWindow):
    def __init__(self):
        self.ablob = None
        global session
        super().__init__()
        uic.loadUi('uic/login.ui', self)

        self.show_autowindow_status = False
        # События кнопок
        # Событие логина
        self.btn_log.clicked.connect(self.login)
        # Событие регистрации
        self.btn_reg.clicked.connect(self.register)

        self.reg_swap_btn.clicked.connect(self.show_autowindow)
        self.reg_swap_btn_2.clicked.connect(self.show_autowindow)

        self.pushButton.clicked.connect(self.open_file_user)

    def open_file_user(self):
        self.user_image = QFileDialog.getOpenFileName(self, 'Выбрать картинку', 'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]

    def show_autowindow(self):
        if self.show_autowindow_status:
            self.login_box.show()
            self.show_autowindow_status = not self.show_autowindow_status
            self.label_title.setText('Вход')
        else:
            self.label_title.setText('Регистрация')
            self.login_box.hide()
            self.show_autowindow_status = not self.show_autowindow_status

    # Функция изменения данных сессии
    def get_session(self):
        cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_log.text()}'")
        res = cursor.fetchall()
        global session
        session['user_id'] = res[0][0]
        session['user_name'] = res[0][1]
        session['chats_with'] = eval(res[0][3])
        session['user_image'] = res[0][4]
        session['status'] = True

    # Функция логина
    def login(self):
        cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_log.text()}'")
        res = cursor.fetchall()
        # Если такой логин имеется
        if res:
            # Если пароль правильный
            if res[0][2] == self.user_password_log.text():
                # Добавляем данные в глабольную переменную сессии
                self.get_session()
                # Смена окон
                self.chats_window = Chats()
                self.chats_window.show()
                self.hide()

            else:
                print('Не верный пароль')
        else:
            print('Не верный логин')

    # Функция регистрации
    def register(self):
        # Валидация совпадения паролей
        if self.user_password_reg.text() == self.user_passwordrep_reg.text():
            # Валидация на налечия пользователя с таким же именем
            cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_reg.text()}'")
            res = cursor.fetchall()
            # Если пользователя с таким именем нет
            if not res:
                # Запрос на добавление пользователя
                cursor.execute(
                    f"""INSERT INTO users (name, password, chats_with, image) VALUES ('{self.user_login_reg.text()}', '{self.user_password_reg.text()}', '[]', '{self.user_image}')""")
                connection.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
