import sys
from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
import sqlite3

SESSION = {
    'status': False,
    'user_id': None,
    'user_name': '',
    # Тут храняться id юзеров с которыми пользователь имеет чаты
    'chats_with': [],
}
# Подключение к БД
connection = sqlite3.connect('db/main_database.db')
cursor = connection.cursor()

# Класс окна с чатами
class Chats(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/chats.ui', self)

        # Массив с кортежами формата (все данные чата, экземпляр кнопки чата)
        self.chats_buttons = []

        # Добвление данных в массив с кнопками и информацией
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

            # Добавляем всё
            self.chats_buttons.append((data_of_btn_user, QtWidgets.QPushButton(f'{data_of_btn_user['user_id']}',
                                                                               parent=self.scrollAreaWidgetContents_2)))
        for i in self.chats_buttons:
            # Позиции кнопок
            self.pos_btn_y = 10
            self.pos_btn_y = self.pos_btn_y + 10
            i[1].move(10, self.pos_btn_y)
            print(i[1].pos()) # ПОЧЕМУ У НИХ ПОЗИЦИЯ ОДНА И ТА ЖЕ ЭТО ВЕДЬ РАЗНЫЕ ЭКЗЕМПЛЯРЫ



class Login(QMainWindow):
    def __init__(self):
        global SESSION
        super().__init__()
        uic.loadUi('uic/login.ui', self)

        self.btn_log.clicked.connect(self.login)
        self.btn_reg.clicked.connect(self.register)

    def get_session(self):
        cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_log.text()}'")
        res = cursor.fetchall()
        global SESSION
        SESSION['user_id'] = res[0][0]
        SESSION['user_name'] = res[0][1]
        SESSION['chats_with'] = eval(res[0][3])
        SESSION['status'] = True

    def login(self):
        cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_log.text()}'")
        res = cursor.fetchall()

        if res:
            if res[0][2] == self.user_password_log.text():
                self.get_session()
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
                cursor.execute(
                    f"INSERT INTO users (name, password) VALUES ('{self.user_login_reg.text()}', '{self.user_password_reg.text()}')")
                connection.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
