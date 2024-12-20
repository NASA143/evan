# Form implementation generated from reading ui file 'chats.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Chats(object):
    def setupUi(self, Chats):
        Chats.setObjectName("Chats")
        Chats.resize(1470, 878)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
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
        self.chat_area.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing)
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
