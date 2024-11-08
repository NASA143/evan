import sys
from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
import sqlite3
import datetime

SESSION = {
    'status': False,
    'user_id': None,
    'user_name': '',
    # Тут храняться id юзеров с которыми пользователь имеет чаты
    'chats_with': [],
    # Ативный чат
    'active_chat': '',
}
# Подключение к БД
connection = sqlite3.connect('db/main_database.db')
cursor = connection.cursor()

# Класс окна с чатами
class Chats(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/chats.ui', self)
        self.chats_buttons_print()

        self.send_msg_btn.clicked.connect(self.send_msg)


    def chats_buttons_print(self):
        # Массив с кортежами формата (все данные чата, экземпляр кнопки чата)
        self.chats_buttons = []

        # Добвление данных в массив с кнопками и информацией
        self.pos_btn_y = 10
        for i in SESSION['chats_with']:
            # Словрь с данными чата
            data_of_btn_user = {
                'user_id': i,
            }

            # Получаем сообщения и информацию о них ОТ ПОЛЬЗОВАТЕЛЯ, заносим их в переменную в словаре
            cursor.execute(f"SELECT * FROM chats WHERE id_user_from = '{SESSION['user_id']}' AND id_user_to = '{i}'")
            data_of_btn_user['message_from_me'] = cursor.fetchall()

            # Получаем сообщения и информацию о них ПОЛЬЗОВАТЕЛЮ, заносим их в переменную в словаре
            cursor.execute(f"SELECT * FROM chats WHERE id_user_from = '{i}' AND id_user_to = '{SESSION['user_id']}'")
            data_of_btn_user['message_to_me'] = cursor.fetchall()

            data_of_btn_user['message_all'] = [*data_of_btn_user['message_to_me'], *data_of_btn_user['message_from_me']]

            # Добавляем всё
            self.chats_buttons.append((data_of_btn_user, QtWidgets.QPushButton(f'{data_of_btn_user['user_id']}',
                                                                               parent=self.scrollAreaWidgetContents)))

            # Параметры кнопок
            # Позиция и размер
            self.verticalLayout.addWidget(self.chats_buttons[-1][1])
            # События кнопок
            self.chats_buttons[-1][1].clicked.connect(self.chat_btn_click)
            # расстояние между кнопками
            self.pos_btn_y += 40

        print(*self.chats_buttons)

    # Событие смены окна чата
    def chat_btn_click(self):
        self.verticalLayout_2.removeWidget(self)
        self.chat_message = []
        for i in self.chats_buttons:
            if self.sender() in i:
                SESSION['active_chat'] = i[0]['user_id']
                # Изменение активного чата
                for j in i[0]['message_all']:
                    print(j)
                    self.chat_message.append(QLabel(f'{j[3]}',parent=self.chat_area_contents))
                    self.verticalLayout_2.addWidget(self.chat_message[-1])






    # Функция отправки сообщения
    def send_msg(self):
        # Добавление записи в таблицу с сообщениями
        cursor.execute(f"INSERT INTO chats (id_user_from, id_user_to, msg, created_time) VALUES ('{SESSION['user_id']}', '{SESSION['active_chat']}', '{self.send_msg_input.text()}', '{datetime.datetime.now()}')")
        connection.commit()


class Login(QMainWindow):
    def __init__(self):
        global SESSION
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
        global SESSION
        SESSION['user_id'] = res[0][0]
        SESSION['user_name'] = res[0][1]
        SESSION['chats_with'] = eval(res[0][3])
        SESSION['status'] = True

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
                    f"INSERT INTO users (name, password, chats_with) VALUES ('{self.user_login_reg.text()}', '{self.user_password_reg.text()}', '[]')")
                connection.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
