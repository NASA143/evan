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


class Ui_Chats(object):
    def setupUi(self, Chats):
        Chats.setObjectName("Chats")
        Chats.resize(1470, 878)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Chats.sizePolicy().hasHeightForWidth())
        Chats.setSizePolicy(sizePolicy)
        Chats.setStyleSheet("background-color: #fff;\n"
                            "")
        self.centralwidget = QtWidgets.QWidget(parent=Chats)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 790, 401, 91))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #fff;\n"
                                 "background-color: #466BFF;\n"
                                 "padding: 10px;")
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 401, 81))
        self.frame.setStyleSheet("background-color: #466BFF;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.find_user_btn = QtWidgets.QPushButton(parent=self.frame)
        self.find_user_btn.setGeometry(QtCore.QRect(350, 20, 41, 41))
        self.find_user_btn.setStyleSheet("background-color:#466BFF;\n"
                                         "border:none;\n"
                                         "border-radius: 10px;\n"
                                         "border: 2px solid #fff")
        self.find_user_btn.setText("")
        self.find_user_btn.setObjectName("find_user_btn")
        self.find_user_input = QtWidgets.QLineEdit(parent=self.frame)
        self.find_user_input.setGeometry(QtCore.QRect(70, 20, 321, 41))
        self.find_user_input.setStyleSheet("background-color: #fff;\n"
                                           "color: #000;\n"
                                           "padding-right: 60px;\n"
                                           "padding:5px;\n"
                                           "border-radius: 15px;")
        self.find_user_input.setObjectName("find_user_input")
        self.settings_btn = QtWidgets.QPushButton(parent=self.frame)
        self.settings_btn.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.settings_btn.setStyleSheet("background-color:#466BFF;\n"
                                        "border:2px solid #fff;\n"
                                        "border-radius: 10px;\n"
                                        "border: 2px solid #fff")
        self.settings_btn.setText("")
        self.settings_btn.setObjectName("settings_btn")
        self.find_user_input.raise_()
        self.find_user_btn.raise_()
        self.settings_btn.raise_()
        self.send_msg_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_msg_btn.setGeometry(QtCore.QRect(1400, 830, 40, 40))
        font = QtGui.QFont()
        font.setFamily("URW Bookman [UKWN]")
        self.send_msg_btn.setFont(font)
        self.send_msg_btn.setStyleSheet("background-color:#466BFF;\n"
                                        "border:none;\n"
                                        "border-radius: 20px;")
        self.send_msg_btn.setText("")
        self.send_msg_btn.setObjectName("send_msg_btn")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 80, 401, 711))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setStyleSheet("background-color: #466BFF;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.buttonsScrollArea = QtWidgets.QWidget()
        self.buttonsScrollArea.setGeometry(QtCore.QRect(0, 0, 385, 709))
        self.buttonsScrollArea.setObjectName("buttonsScrollArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.buttonsScrollArea)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.buttonsScrollArea)
        self.chat_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.chat_area.setGeometry(QtCore.QRect(400, 60, 1071, 761))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_area.sizePolicy().hasHeightForWidth())
        self.chat_area.setSizePolicy(sizePolicy)
        self.chat_area.setStyleSheet("background-color: #466BFF;")
        self.chat_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.chat_area.setWidgetResizable(True)
        self.chat_area.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.chat_area.setObjectName("chat_area")
        self.chat_area_contents = QtWidgets.QWidget()
        self.chat_area_contents.setGeometry(QtCore.QRect(1037, 741, 18, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chat_area_contents.sizePolicy().hasHeightForWidth())
        self.chat_area_contents.setSizePolicy(sizePolicy)
        self.chat_area_contents.setObjectName("chat_area_contents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.chat_area_contents)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chat_area.setWidget(self.chat_area_contents)
        self.send_msg_input = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.send_msg_input.setGeometry(QtCore.QRect(400, 820, 1071, 60))
        self.send_msg_input.setStyleSheet("color:black;\n"
                                          "background-color:#E8E8E8;\n"
                                          "border:none;\n"
                                          "")
        self.send_msg_input.setInputMask("")
        self.send_msg_input.setText("")
        self.send_msg_input.setObjectName("send_msg_input")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(399, 0, 1071, 61))
        self.groupBox.setStyleSheet("background-color: #466BFF;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.active_chat_name = QtWidgets.QLabel(parent=self.groupBox)
        self.active_chat_name.setGeometry(QtCore.QRect(20, 10, 431, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.active_chat_name.setFont(font)
        self.active_chat_name.setText("")
        self.active_chat_name.setObjectName("active_chat_name")
        self.refresh_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.refresh_btn.setGeometry(QtCore.QRect(1000, 10, 41, 41))
        self.refresh_btn.setStyleSheet("background-color:#466BFF;\n"
                                       "border:1px solid #fff;\n"
                                       "border-radius: 20px;")
        self.refresh_btn.setText("")
        self.refresh_btn.setObjectName("refresh_btn")
        self.export_btn = QtWidgets.QPushButton(parent=self.groupBox)
        self.export_btn.setGeometry(QtCore.QRect(950, 10, 41, 41))
        self.export_btn.setStyleSheet("background-color:#466BFF;\n"
                                      "border:none;\n"
                                      "border-radius: 10px;\n"
                                      "border: 2px solid #fff")
        self.export_btn.setText("")
        self.export_btn.setObjectName("export_btn")
        self.label.raise_()
        self.frame.raise_()
        self.scrollArea.raise_()
        self.chat_area.raise_()
        self.send_msg_input.raise_()
        self.send_msg_btn.raise_()
        self.groupBox.raise_()
        Chats.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chats)
        QtCore.QMetaObject.connectSlotsByName(Chats)

    def retranslateUi(self, Chats):
        _translate = QtCore.QCoreApplication.translate
        Chats.setWindowTitle(_translate("Chats", "MainWindow"))
        self.label.setText(_translate("Chats", "JustChat"))
        self.find_user_input.setPlaceholderText(_translate("Chats", "Имя пользователя"))
        self.send_msg_input.setPlaceholderText(_translate("Chats", "  Введите сообщение"))


class Ui_exit_dialog(object):
    def setupUi(self, exit_dialog):
        exit_dialog.setObjectName("exit_dialog")
        exit_dialog.resize(311, 154)
        exit_dialog.setStyleSheet("background-color: #fff")
        self.exit_btn = QtWidgets.QPushButton(parent=exit_dialog)
        self.exit_btn.setGeometry(QtCore.QRect(180, 110, 121, 31))
        self.exit_btn.setStyleSheet("background-color: #ff0000;\n"
                                    "font-size: 14px;\n"
                                    "")
        self.exit_btn.setObjectName("exit_btn")
        self.cansel_btn = QtWidgets.QPushButton(parent=exit_dialog)
        self.cansel_btn.setGeometry(QtCore.QRect(10, 110, 121, 31))
        self.cansel_btn.setStyleSheet("background: none;\n"
                                      "border: none;\n"
                                      "background-color: rgb(80, 80, 80)")
        self.cansel_btn.setObjectName("cansel_btn")
        self.label = QtWidgets.QLabel(parent=exit_dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 231, 31))
        self.label.setStyleSheet("font-size: 20px;\n"
                                 "color: #000;\n"
                                 "background:none;")
        self.label.setObjectName("label")

        self.retranslateUi(exit_dialog)
        QtCore.QMetaObject.connectSlotsByName(exit_dialog)

    def retranslateUi(self, exit_dialog):
        _translate = QtCore.QCoreApplication.translate
        exit_dialog.setWindowTitle(_translate("exit_dialog", "Dialog"))
        self.exit_btn.setText(_translate("exit_dialog", "Выйти"))
        self.cansel_btn.setText(_translate("exit_dialog", "Отмена"))
        self.label.setText(_translate("exit_dialog", "Вы точно хотите выйти?"))


class Ui_Autorization(object):
    def setupUi(self, Autorization):
        Autorization.setObjectName("Autorization")
        Autorization.resize(1256, 828)
        Autorization.setStyleSheet("background-color: #2A72EE")
        self.centralwidget = QtWidgets.QWidget(parent=Autorization)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1251, 821))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=self.horizontalLayoutWidget)
        self.groupBox.setEnabled(True)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_title = QtWidgets.QLabel(parent=self.groupBox)
        self.label_title.setGeometry(QtCore.QRect(50, 100, 341, 59))
        self.label_title.setStyleSheet("font-family: Inter;\n"
                                       "font-size: 48px;\n"
                                       "color: #fff")
        self.label_title.setObjectName("label_title")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(640, -10, 621, 819))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.reg_box = QtWidgets.QGroupBox(parent=self.groupBox)
        self.reg_box.setGeometry(QtCore.QRect(30, 200, 561, 341))
        self.reg_box.setStyleSheet("background-color: #fff;\n"
                                   "border:none;")
        self.reg_box.setTitle("")
        self.reg_box.setObjectName("reg_box")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.reg_box)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 261, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget)
        self.groupBox_4.setStyleSheet("border:none;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 48, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #000")
        self.label_2.setObjectName("label_2")
        self.user_login_reg = QtWidgets.QLineEdit(parent=self.groupBox_4)
        self.user_login_reg.setGeometry(QtCore.QRect(0, 20, 250, 35))
        self.user_login_reg.setStyleSheet("background-color:white;\n"
                                          "border: 2px solid #466BFF;\n"
                                          "border-radius: 0px;\n"
                                          "color: #000;")
        self.user_login_reg.setText("")
        self.user_login_reg.setObjectName("user_login_reg")
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget)
        self.groupBox_8.setStyleSheet("border:none;")
        self.groupBox_8.setTitle("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 59, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: #000")
        self.label_5.setObjectName("label_5")
        self.user_password_reg = QtWidgets.QLineEdit(parent=self.groupBox_8)
        self.user_password_reg.setGeometry(QtCore.QRect(0, 20, 250, 35))
        self.user_password_reg.setStyleSheet("background-color:white;\n"
                                             "border: 2px solid #466BFF;\n"
                                             "border-radius: 0px;\n"
                                             "color: #000;")
        self.user_password_reg.setText("")
        self.user_password_reg.setObjectName("user_password_reg")
        self.verticalLayout.addWidget(self.groupBox_8)
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget)
        self.groupBox_5.setStyleSheet("border:none;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.label = QtWidgets.QLabel(parent=self.groupBox_5)
        self.label.setGeometry(QtCore.QRect(0, 0, 144, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #000")
        self.label.setObjectName("label")
        self.user_passwordrep_reg = QtWidgets.QLineEdit(parent=self.groupBox_5)
        self.user_passwordrep_reg.setGeometry(QtCore.QRect(0, 20, 250, 35))
        self.user_passwordrep_reg.setStyleSheet("background-color:white;\n"
                                                "border: 2px solid #466BFF;\n"
                                                "border-radius: 0px;\n"
                                                "color: #000;")
        self.user_passwordrep_reg.setText("")
        self.user_passwordrep_reg.setObjectName("user_passwordrep_reg")
        self.verticalLayout.addWidget(self.groupBox_5)
        self.btn_reg = QtWidgets.QPushButton(parent=self.reg_box)
        self.btn_reg.setGeometry(QtCore.QRect(310, 280, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_reg.setFont(font)
        self.btn_reg.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_reg.setStyleSheet("color: #fff;\n"
                                   "background-color: #2A72EE;\n"
                                   "border-radius:0px;\n"
                                   "padding: 7px 14px;\n"
                                   "")
        self.btn_reg.setObjectName("btn_reg")
        self.reg_swap_btn = QtWidgets.QPushButton(parent=self.reg_box)
        self.reg_swap_btn.setGeometry(QtCore.QRect(400, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reg_swap_btn.setFont(font)
        self.reg_swap_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reg_swap_btn.setStyleSheet("border: none;\n"
                                        "background: none;\n"
                                        "color: #466BFF;")
        self.reg_swap_btn.setObjectName("reg_swap_btn")
        self.pushButton = QtWidgets.QPushButton(parent=self.reg_box)
        self.pushButton.setGeometry(QtCore.QRect(290, 80, 131, 23))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet("color: #fff;\n"
                                      "background-color: #2A72EE;\n"
                                      "border-radius:0px;\n"
                                      "padding: 7px 14px;\n"
                                      "")
        self.pushButton.setObjectName("pushButton")
        self.label_6 = QtWidgets.QLabel(parent=self.reg_box)
        self.label_6.setGeometry(QtCore.QRect(290, 50, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #000")
        self.label_6.setObjectName("label_6")
        self.user_image_link = QtWidgets.QLabel(parent=self.reg_box)
        self.user_image_link.setGeometry(QtCore.QRect(290, 110, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(10)
        font.setBold(False)
        self.user_image_link.setFont(font)
        self.user_image_link.setStyleSheet("color: #000")
        self.user_image_link.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTrailing | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.user_image_link.setObjectName("user_image_link")
        self.label_error_reg = QtWidgets.QLabel(parent=self.reg_box)
        self.label_error_reg.setGeometry(QtCore.QRect(20, 260, 251, 16))
        self.label_error_reg.setText("")
        self.label_error_reg.setObjectName("label_error_reg")
        self.login_box = QtWidgets.QGroupBox(parent=self.groupBox)
        self.login_box.setEnabled(True)
        self.login_box.setGeometry(QtCore.QRect(30, 200, 561, 341))
        self.login_box.setStyleSheet("background-color: #fff;\n"
                                     "border:none;")
        self.login_box.setTitle("")
        self.login_box.setObjectName("login_box")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(parent=self.login_box)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 50, 261, 141))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_2)
        self.groupBox_6.setStyleSheet("border:none;")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 59, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #000")
        self.label_3.setObjectName("label_3")
        self.user_login_log = QtWidgets.QLineEdit(parent=self.groupBox_6)
        self.user_login_log.setGeometry(QtCore.QRect(0, 20, 251, 31))
        self.user_login_log.setStyleSheet("background-color:white;\n"
                                          "border: 2px solid #466BFF;\n"
                                          "border-radius: 0px;\n"
                                          "color: #000;")
        self.user_login_log.setText("")
        self.user_login_log.setObjectName("user_login_log")
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.verticalLayoutWidget_2)
        self.groupBox_7.setStyleSheet("border:none;")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_7)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 59, 20))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: #000")
        self.label_4.setObjectName("label_4")
        self.user_password_log = QtWidgets.QLineEdit(parent=self.groupBox_7)
        self.user_password_log.setGeometry(QtCore.QRect(0, 21, 251, 31))
        self.user_password_log.setStyleSheet("background-color:white;\n"
                                             "border: 2px solid #466BFF;\n"
                                             "border-radius: 0px;\n"
                                             "color: #000;")
        self.user_password_log.setObjectName("user_password_log")
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.btn_log = QtWidgets.QPushButton(parent=self.login_box)
        self.btn_log.setGeometry(QtCore.QRect(400, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_log.setFont(font)
        self.btn_log.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn_log.setStyleSheet("color: #fff;\n"
                                   "background-color: #2A72EE;\n"
                                   "border-radius:0px;\n"
                                   "padding: 7px 14px;\n"
                                   "")
        self.btn_log.setObjectName("btn_log")
        self.reg_swap_btn_2 = QtWidgets.QPushButton(parent=self.login_box)
        self.reg_swap_btn_2.setGeometry(QtCore.QRect(400, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.reg_swap_btn_2.setFont(font)
        self.reg_swap_btn_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reg_swap_btn_2.setStyleSheet("border: none;\n"
                                          "background: none;\n"
                                          "color: #466BFF;")
        self.reg_swap_btn_2.setObjectName("reg_swap_btn_2")
        self.error_label = QtWidgets.QLabel(parent=self.login_box)
        self.error_label.setGeometry(QtCore.QRect(20, 180, 251, 16))
        self.error_label.setStyleSheet("color: #f00;")
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.reg_box.raise_()
        self.login_box.raise_()
        self.label_title.raise_()
        self.groupBox_2.raise_()
        self.horizontalLayout.addWidget(self.groupBox)
        Autorization.setCentralWidget(self.centralwidget)

        self.retranslateUi(Autorization)
        QtCore.QMetaObject.connectSlotsByName(Autorization)

    def retranslateUi(self, Autorization):
        _translate = QtCore.QCoreApplication.translate
        Autorization.setWindowTitle(_translate("Autorization", "MainWindow"))
        self.label_title.setText(_translate("Autorization", "Вход"))
        self.label_2.setText(_translate("Autorization", "Логин"))
        self.label_5.setText(_translate("Autorization", "Пароль"))
        self.label.setText(_translate("Autorization", "Повторите пароль"))
        self.btn_reg.setText(_translate("Autorization", "Зарегистрироваться"))
        self.reg_swap_btn.setText(_translate("Autorization", "Вход🠒"))
        self.pushButton.setText(_translate("Autorization", "Выбрать файл"))
        self.label_6.setText(_translate("Autorization", "Выбирите изображение профиля"))
        self.user_image_link.setText(_translate("Autorization", ""))
        self.label_3.setText(_translate("Autorization", "Логин"))
        self.label_4.setText(_translate("Autorization", "Пароль"))
        self.btn_log.setText(_translate("Autorization", "Войти"))
        self.reg_swap_btn_2.setText(_translate("Autorization", "Регистрация🠒"))


class ExitDialog(QDialog, Ui_exit_dialog):
    def __init__(self, wind):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('JustChat')
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
class Chats(QMainWindow, Ui_Chats):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        self.export_btn.clicked.connect(self.export)

        # Свойства кнопок
        self.find_user_btn.setIcon(QIcon('content/user-add.png'))
        self.find_user_btn.setIconSize(QSize(60, 60))

        self.settings_btn.setIcon(QIcon('content/lock.png'))
        self.settings_btn.setIconSize(QSize(60, 60))

        self.send_msg_btn.setIcon(QIcon('content/arrow-up.png'))
        self.send_msg_btn.setIconSize(QSize(20, 20))

        self.refresh_btn.setIcon(QIcon('content/clock-reqind.png'))
        self.refresh_btn.setIconSize(QSize(20, 20))

        self.export_btn.setIcon(QIcon('content/file-edit.png'))
        self.export_btn.setIconSize(QSize(30, 30))

    def export(self):
        if self.sender().text():
            if session['last_sender_id'] != self.sender().text():
                cursor.execute(f'''SELECT id FROM users WHERE name = "{self.sender().text()}"''')
                self.chat_click_id = cursor.fetchall()[0][0]
                session['active_chat'] = self.chat_click_id
            if session['last_sender'] != self.sender():
                session['last_sender'] = self.sender()

        if session['last_sender']:
            self.active_chat_name.setText(session['last_sender'].text())

        file = open("chat.txt", "w+")
        for i in self.chats_data:
            if self.chat_click_id == i[0]:
                for k in i[1]:
                    file.write(k[3] + '\n')
        file.close()

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


class Login(QMainWindow, Ui_Autorization):
    def __init__(self):
        self.ablob = None
        global session
        super().__init__()
        self.setupUi(self)
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
