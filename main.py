# ИМПОРТ ВСЕХ МОДУЛЕЙ
import sys
from PyQt6 import uic, QtCore, QtWidgets, QtGui
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QFileDialog, QInputDialog, QDialog, \
    QDialogButtonBox
import sqlite3
import datetime

# ПЕРЕМЕННАЯ СЕССИИ
session = {
    'status': False,  # Статус активности сессии
    'user_id': None,  # id активного юзера
    'user_name': '',  # имя активного юзера
    'chats_with': [],  # id пользователей с которыми имеются чаты
    'active_chat': '',  # Активный чат
    'last_sender': None,  # Последня кнопка чатов, которую нажали
    'user_image': '',  # Статус активности сессии
    'last_sender_id': '',  # Статус активности сессии
}

# Подключение к БД
connection = sqlite3.connect('db/main_database.db')
cursor = connection.cursor()


class ExitDialog(QDialog):
    def __init__(self, wind):
        super().__init__()
        self.setWindowTitle('JustChat')
        uic.loadUi('uic/exitdialog.ui', self)
        self.cansel_btn.clicked.connect(self.cansel_btn_event)
        self.exit_btn.clicked.connect(self.exit_btn_event)
        self.wind = wind

    def cansel_btn_event(self):
        self.hide()

    def exit_btn_event(self):
        self.wind.hide()
        ex.show()
        self.hide()


# Класс окна с чатами
class Chats(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('uic/chats.ui', self)
        self.setWindowTitle('JustChat')
        self.chats_data = []  # Данные о чатах пользователя
        self.chats_buttons = []  # Массив с экземплярами кнопок чата
        self.chat_message_now = []  # Сообщения активного чата
        self.chat_click_id = ''

        # Вызов основных функций
        self.get_data()
        self.print_chats_buttons()

        # Присвоение функций для кнопок
        self.send_msg_btn.clicked.connect(self.send_msg)
        self.find_user_btn.clicked.connect(self.find_user)
        self.settings_btn.clicked.connect(self.exit_app)
        self.refresh_btn.clicked.connect(self.refresh)

        # Свойства кнопок
        self.find_user_btn.setIcon(QIcon('content/user-add.png'))
        self.find_user_btn.setIconSize(QSize(60, 60))

        self.settings_btn.setIcon(QIcon('content/lock.png'))
        self.settings_btn.setIconSize(QSize(60, 60))

        self.send_msg_btn.setIcon(QIcon('content/arrow-up.png'))
        self.send_msg_btn.setIconSize(QSize(20, 20))

        self.refresh_btn.setIcon(QIcon('content/clock-reqind.png'))
        self.refresh_btn.setIconSize(QSize(20, 20))

    def refresh(self):
        print('aaa')
        self.get_data()
        self.chat_btn_click()

    def exit_app(self):
        self.fdia = ExitDialog(self)
        self.fdia.show()

    # Функция добавления нового чата по имени пользователя
    def find_user(self):
        # Запрос на поиск юзера с введенным именем
        cursor.execute(f'''SELECT id FROM users WHERE name = "{self.find_user_input.text()}"''')
        res = cursor.fetchall()

        # Если такой юзер нашелся и его нет в уже имеющихся чатах
        if res and res[0][0] not in session['chats_with']:
            # Добавляем id нового чата
            session['chats_with'].append(res[0][0])
            # Изменяем соответсвующую строку в БД
            cursor.execute(
                f'''UPDATE users SET chats_with = "{session['chats_with']}" WHERE id = {session['user_id']}''')
            connection.commit()
            cursor.execute(f'''SELECT chats_with FROM users WHERE name = "{self.find_user_input.text()}"''')
            req = eval(cursor.fetchall()[0][0])
            req.append(session['user_id'])
            cursor.execute(f'''UPDATE users SET chats_with = "{req}" WHERE name = "{self.find_user_input.text()}"''')
            connection.commit()

        # Обновление отображаемых данных
        self.get_data()
        self.print_chats_buttons()

    # Получение данных о чатах пользователя
    def get_data(self):
        self.chats_data = []
        for i in session['chats_with']:
            cursor.execute(
                f'''SELECT * FROM chats WHERE id_user_from = "{session['user_id']}" AND id_user_to = "{i}" 
                OR id_user_from = "{i}" AND id_user_to = "{session['user_id']}" ORDER BY created_time''')
            self.chats_data.append((i, cursor.fetchall()))

    # Отрисовка кнопок чатов
    def print_chats_buttons(self):
        # Очистка и удаление старых экземпляров
        for i in self.chats_buttons:
            self.verticalLayout.removeWidget(i)
            i.deleteLater()
        self.chats_buttons = []

        # Добавление кнопок в соответсвии с имеющимеся чатами
        for i in self.chats_data:
            # Запрос на получение имени пользователя
            cursor.execute(f'''SELECT name FROM users WHERE id = {i[0]}''')
            # Добавление экземпляра кнопки
            self.chats_buttons.append(QPushButton(f'{cursor.fetchall()[0][0]}', parent=self.buttonsScrollArea))
            # Добавление кпоки в лэйаут
            self.verticalLayout.addWidget(self.chats_buttons[-1])
            # Свойства кнопки
            self.chats_buttons[-1].clicked.connect(self.chat_btn_click)
            self.chats_buttons[-1].setStyleSheet("background-color: #fff;\n"
                                                 "border-radius: 10px;\n"
                                                 "color: #000;\n"
                                                 "padding: 5px 5px;\n"
                                                 "text-align: left;"
                                                 )
            # Добавление иконки пользователя чата
            cursor.execute(f"SELECT image FROM users WHERE id = '{i[0]}'")
            self.chats_buttons[-1].setIcon(QIcon('content/' + cursor.fetchall()[0][0].split('/')[-1]))
            self.chats_buttons[-1].setIconSize(QSize(50, 50))

    # Событие нажатия на кнопку чата (смена чата)
    def chat_btn_click(self):
        # Узнаем кто вызвал функцию
        if self.sender().text():
            if session['last_sender_id'] != self.sender().text():
                cursor.execute(f'''SELECT id FROM users WHERE name = "{self.sender().text()}"''')
                self.chat_click_id = cursor.fetchall()[0][0]
                session['active_chat'] = self.chat_click_id
            if session['last_sender'] != self.sender():
                session['last_sender'] = self.sender()

        if session['last_sender']:
            self.active_chat_name.setText(session['last_sender'].text())

        for i in self.chat_message_now:
            self.verticalLayout_2.removeWidget(i)
            i.deleteLater()
        self.chat_message_now = []
        for i in self.chats_data:
            if self.chat_click_id == i[0]:
                for k in i[1]:
                    self.chat_message_now.append(QLabel(
                        f'Вы:\n{k[3]}' if k[1] == session['user_id'] else f'{session['last_sender'].text()}:\n{k[3]}',
                        parent=self.chat_area_contents))
                    self.chat_message_now[-1].setStyleSheet("width: 400px;\n"
                                                            "background-color: #fff;\n"
                                                            "border-radius: 5px;\n"
                                                            "color: #000;\n"
                                                            "padding: 10px 10px;\n"
                                                            "font-size: 20px")
                    self.verticalLayout_2.addWidget(self.chat_message_now[-1])

    # Отправка сообщения
    def send_msg(self):
        cursor.execute(
            f"INSERT INTO chats (id_user_from, id_user_to, msg, created_time) "
            f"VALUES ('{session['user_id']}', '{session['active_chat']}',"
            f" '{self.send_msg_input.text()}', '{datetime.datetime.now()}')")
        connection.commit()
        self.send_msg_input.setText('')
        self.get_data()
        self.chat_btn_click()


class Login(QMainWindow):
    def __init__(self):
        self.ablob = None
        global session
        super().__init__()
        uic.loadUi('uic/login.ui', self)
        self.setWindowTitle('JustChat')

        self.show_autowindow_status = False
        # События кнопок
        # Событие логина
        self.btn_log.clicked.connect(self.login)
        # Событие регистрации
        self.btn_reg.clicked.connect(self.register)
        # Смена окон авторизации и регистрации
        self.reg_swap_btn.clicked.connect(self.show_autowindow)
        self.reg_swap_btn_2.clicked.connect(self.show_autowindow)

        self.pushButton.clicked.connect(self.open_file_user)
        self.user_image = None

    def open_file_user(self):
        self.user_image = \
            QFileDialog.getOpenFileName(self, 'Выбрать картинку', 'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[
                0]
        self.user_image_link.setText(self.user_image)

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
                # Очистка полей
                self.user_login_log.setText('')
                self.user_password_log.setText('')
                # Смена окон
                self.chats_window = Chats()
                self.chats_window.show()
                self.hide()

            else:
                self.error_label.setStyleSheet("color: #f00;\n")
                self.error_label.setText('Неверный пароль')
        else:
            self.error_label.setStyleSheet("color: #f00;\n")
            self.error_label.setText('Неверный логин')

    # Функция регистрации
    def register(self):
        # Валидация совпадения паролей
        if self.user_password_reg.text() == self.user_passwordrep_reg.text():
            # Валидация на налечия пользователя с таким же именем
            cursor.execute(f"SELECT * FROM users WHERE name = '{self.user_login_reg.text()}'")
            res = cursor.fetchall()
            # Если пользователя с таким именем нет
            if not res:
                if self.user_image == '':
                    self.user_image = '/home/ivi/Рабочий стол/evan/content/user_image_default.png'
                # Запрос на добавление пользователя
                cursor.execute(
                    f"""INSERT INTO users (name, password, chats_with, image) VALUES
                     ('{self.user_login_reg.text()}', '{self.user_password_reg.text()}', '[]', '{self.user_image}')""")
                connection.commit()
                self.label_error_reg.setStyleSheet("color: #0f0;\n")
                self.label_error_reg.setText('Успешно')
            else:
                self.label_error_reg.setStyleSheet("color: #f00;\n")
                self.label_error_reg.setText('Логин занят')
        else:
            self.label_error_reg.setStyleSheet("color: #f00;\n")
            self.label_error_reg.setText('Пароли не совпадают')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Login()
    ex.show()
    sys.exit(app.exec())
