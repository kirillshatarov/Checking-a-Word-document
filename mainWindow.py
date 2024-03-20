import json
import sys

import docx
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import (QApplication, QLabel, QPushButton, QComboBox, QLineEdit, QVBoxLayout,
                             QWidget, QScrollArea, QPlainTextEdit, QMessageBox, QFileDialog)

from constants import READ_ONLY, SETTER
from docx_cls import FileManger
from secondWindow import SecondWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(QSize(760, 850))  # Размер окна при сворачивании
        self.initUI()
        self.pathFile = ''
        self.pathFile = ''
        # self.second_window = None
        # self.plain_text = None

    def initUI(self):
        # self.centralwidget = QWidget()
        # Создаем QLabel для обработки перетаскивания файлов
        self.dropLabel = QLabel('Перетащите файл сюда', self)
        self.dropLabel.setGeometry(QtCore.QRect(250, 370, 400, 80))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dropLabel.setFont(font)
        self.dropLabel.setAcceptDrops(True)
        # self.dropLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Кнопка для открывания второго окна
        self.window2_button = QPushButton("Проверить по ГОСТ", self)
        self.window2_button.setGeometry(QtCore.QRect(540, 10, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.window2_button.setFont(font)

        # Кнопка выбора файла
        self.pickFileButton = QPushButton("Выбрать файл", self)
        self.pickFileButton.setGeometry(QtCore.QRect(20, 390, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickFileButton.setFont(font)

        self.pickAligment = QComboBox(self)
        self.pickAligment.setGeometry(QtCore.QRect(20, 200, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickAligment.setFont(font)

        self.labelAlignment = QLabel('Укажите выравнивание:', self)
        self.labelAlignment.setGeometry(QtCore.QRect(20, 160, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelAlignment.setFont(font)

        self.pickAlignmentLabel = QLabel(self)
        self.pickAlignmentLabel.setGeometry(QtCore.QRect(190, 200, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pickAlignmentLabel.setFont(font)
        # self.pickAlignmentLabel.setAlignment(QtCore.Qt.AlignCenter)

        self.pickIndent = QLabel('Укажите отступ в см:', self)
        self.pickIndent.setGeometry(QtCore.QRect(350, 250, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickIndent.setFont(font)

        self.enterIndent = QLineEdit(self)
        self.enterIndent.setGeometry(QtCore.QRect(350, 290, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterIndent.setFont(font)
        self.enterIndent.setPlaceholderText('0')
        self.enterIndent.setValidator(QtGui.QDoubleValidator())

        self.enterIndentLabel = QLabel(' см', self)
        self.enterIndentLabel.setGeometry(QtCore.QRect(440, 290, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterIndentLabel.setFont(font)

        self.enterLineSpace = QLineEdit(self)
        self.enterLineSpace.setGeometry(QtCore.QRect(350, 200, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(75)
        self.enterLineSpace.setFont(font)
        self.enterLineSpace.setPlaceholderText('1')
        self.enterLineSpace.setValidator(QtGui.QDoubleValidator())

        self.pickLineSpace = QLabel('Укажите межстрочный интервал в см:', self)
        self.pickLineSpace.setGeometry(QtCore.QRect(350, 160, 410, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickLineSpace.setFont(font)

        self.enterLineSpaceLabel = QLabel(' см', self)
        self.enterLineSpaceLabel.setGeometry(QtCore.QRect(440, 200, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enterLineSpaceLabel.setFont(font)

        self.enterFont = QLineEdit(self)
        self.enterFont.setGeometry(QtCore.QRect(20, 110, 240, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enterFont.setFont(font)

        self.pickFont = QLabel('Укажите стиль шрифта', self)
        self.pickFont.setGeometry(QtCore.QRect(20, 70, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickFont.setFont(font)

        self.enterFontSize = QLineEdit(self)
        self.enterFontSize.setGeometry(QtCore.QRect(350, 110, 240, 35))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enterFontSize.setFont(font)

        self.pickFontSize = QLabel('Укажите размер шрифта', self)
        self.pickFontSize.setGeometry(QtCore.QRect(350, 70, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickFontSize.setFont(font)

        self.filePicked = QLabel("", self)
        self.filePicked.setGeometry(QtCore.QRect(220, 510, 400, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.filePicked.setFont(font)
        # self.filePicked.setAlignment(QtCore.Qt.AlignCenter)

        self.pickFile = QLabel('Выберите файл (docx):', self)
        self.pickFile.setGeometry(QtCore.QRect(30, 350, 250, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pickFile.setFont(font)

        self.checkFile = QPushButton('Проверка файла', self)
        self.checkFile.setGeometry(QtCore.QRect(20, 500, 181, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.checkFile.setFont(font)

        self.title = QLabel('Проверка файла по своим настройкам', self)
        self.title.setGeometry(QtCore.QRect(30, 20, 470, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        self.confirm_button = QPushButton('Подтвердить настройки', self)
        self.confirm_button.setGeometry(QtCore.QRect(20, 270, 250, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confirm_button.setFont(font)
        self.filename_settings = "My settings"  # название файла со своими настройками проверки

        self.downloadFile = QPushButton("Скачать проверенный файл", self)
        self.downloadFile.setGeometry(20, 790, 280, 40)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.downloadFile.setFont(font)

        self.answer = QScrollArea(self)
        self.answer.setGeometry(QtCore.QRect(20, 550, 600, 230))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.answer.setFont(font)
        self.answer.setWidgetResizable(True)
        self.answer.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)

        self.plain_text = QPlainTextEdit()
        self.plain_text.setReadOnly(READ_ONLY)

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 230, 119))

        # layout = QVBoxLayout(self)
        #
        # layout.addWidget(self.title)
        # layout.addWidget(self.pickFont)
        # layout.addWidget(self.choiceFont)
        # layout.addWidget(self.titlePicked)
        #
        # layout.addWidget(self.labelAlignment)
        # layout.addWidget(self.pickAligment)
        # layout.addWidget(self.pickAlignmentLabel)
        #
        # layout.addWidget(self.pickIndent)
        # layout.addWidget(self.enterIndent)
        # layout.addWidget(self.enterIndentLabel)
        #
        # layout.addWidget(self.pickLineSpace)
        # layout.addWidget(self.enterLineSpace)
        # layout.addWidget(self.enterLineSpaceLabel)
        #
        # layout.addWidget(self.window2_button)
        #
        # layout.addWidget(self.pickFile)
        # layout.addWidget(self.dropLabel)
        # layout.addWidget(self.pickFileButton)
        # layout.addWidget(self.filePicked)
        # layout.addWidget(self.checkFile)
        #
        # layout.addWidget(self.answer)
        #
        # self.setLayout(layout)

        layout_2 = QVBoxLayout(self)
        layout_2.addWidget(self.plain_text)

        w = QWidget()
        w.setLayout(layout_2)
        self.answer.setWidget(w)

        #
        # события кнопок
        #

        self.pickFileButton.clicked.connect(self.pickFileButton_Clicked)
        self.checkFile.clicked.connect(self.checkFile_Clicked)
        # self.choiceFont.textEdited.connect(self.choiceTitleActive)
        self.pickAligment.activated.connect(self.choiceAlignActive)
        self.enterIndent.textEdited.connect(self.changeIndentLabel)
        self.enterLineSpace.textEdited.connect(self.changeLineSpaceLabel)
        self.window2_button.clicked.connect(self.open_second_window)  # Открытие второго окна для проверки по гостам
        self.confirm_button.clicked.connect(self.confirm_settings)  # Подтверждение настроек
        self.downloadFile.clicked.connect(self.save_ready_file)  # скачивание проверенного файла

        # Подключаем события перетаскивания
        self.dropLabel.dragEnterEvent = self.dragEnterEvent

        self.dropLabel.dropEvent = self.dropEvent

        # Добавляем обработку событий перетаскивания файлов
        self.filePicked.setAcceptDrops(True)

        # self.choiceTitle.addItems(TITLE.keys())
        # self.titlePicked.setText(self.choiceTitle.currentText())
        self.pickAligment.addItems(SETTER.keys())
        self.pickAlignmentLabel.setText(self.pickAligment.currentText())

    def open_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()

    def confirm_settings(self):
        # currentIndent = currentIndent.replace(',', '.')
        data = {
            "name": self.filename_settings,
            "font-style": self.enterFont.text(),
            "font-size": self.enterFontSize.text(),
            "paragraph-indent": self.enterIndent.text().replace(',', '.'),
            "interval": self.enterLineSpace.text().replace(',', '.'),
            "alignment": self.pickAligment.currentText()
        }
        # print(self.filename, self.enterFont.text(), self.enterFontSize.text(), self.enterIndent.text(), self.enterLineSpace.text(), self.pickAligment.currentText())
        with open('./files/gost/' + self.filename_settings + '.json', "w", encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

    def changeIndentLabel(self, text):
        self.enterIndentLabel.setText(text + ' см')

    def changeLineSpaceLabel(self, text):
        self.enterLineSpaceLabel.setText(text + ' см')

    # def choiceTitleActive(self, index):
    #     self.titlePicked.setText(self.choiceTitle.itemText(index))
    #     self.currentTitle = self.titlePicked

    def choiceAlignActive(self, index):
        self.pickAlignmentLabel.setText(self.pickAligment.itemText(index))
        self.currentAlign = self.pickAlignmentLabel

    def pickFileButton_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         '.',
                                                         'Word files (*.docx)')
        if filename == '':
            self.filePicked.setText('Файл не выбран.')
            self.pathFile = ''
        else:
            self.pathFile = filename
            filename = filename.split('/')[-1]
            self.filePicked.setText(filename)

    def checkFile_Clicked(self):
        print(self.pathFile)
        if self.pathFile == '':
            try:
                self.notSelectFile = QMessageBox()
                self.notSelectFile.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                self.notSelectFile.setText('Вы не выбрали файл!')
                self.notSelectFile.setWindowTitle('Ошибка!')
                self.notSelectFile.setIcon(QMessageBox.Warning)
                res = self.notSelectFile.exec()
            except Exception as e:
                pass
        else:
            self.fileName = self.pathFile.split('/')[-1]
            self.path = f'./{self.fileName}'
            print(self.path)
            obj = FileManger(docx.Document(self.path), gost="My settings", doc_rej=False)
            print(1)
            errors = obj.is_correct_document()
            print(2)
            self.plain_text.clear()
            self.plain_text.setPlainText(errors)

    def save_ready_file(self):
        obj2 = FileManger(docx.Document(self.path), gost="My settings", doc_rej=True)
        obj2.is_correct_document()

    def dragEnterEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls() and mime_data.urls()[0].isLocalFile():
            event.acceptProposedAction()

    def dropEvent(self, event):
        mime_data = event.mimeData()
        if mime_data.hasUrls() and mime_data.urls()[0].isLocalFile():
            file_path = mime_data.urls()[0].toLocalFile()
            filename = file_path.split('/')[-1]
            # filename = file_path
            self.filePicked.setText(filename)
            self.pathFile = file_path
            event.acceptProposedAction()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    # main_window.confirm_settings()  # Вызываем сохранение файла JSON перед завершением приложения
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main_window = MainWindow()
#     main_window.show()
#     sys.exit(app.exec_())


# if __name__ == '__main__':
#     app = QApplication([])
#     main_window = MainWindow()
#     main_window.show()
#     app.exec_()
