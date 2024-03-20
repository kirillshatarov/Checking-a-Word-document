import sys
import json
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (QApplication, QToolBar, QFileDialog, QLabel, QMainWindow, QPlainTextEdit, QVBoxLayout,
                             QWidget, QMessageBox, QPushButton, QComboBox)

from ml import Ui_MainWindow
from secondWindow import SecondWindow
from constants import READ_ONLY, TITLE, SETTER, GOST
from checkTitle import checkTitles
from checkIndent import checkIndents
from checkSetter import checkSetters
from checkLineSpace import checkLineSpaces
from docx import Document


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(QSize(700, 850))  # Размер окна при сворачивании
        # self.setMaximumSize(QSize(800, 900))

        # начальные значения
        self.pathFile = ''
        self.currentTitle = self.ui.titlePicked
        self.currentAlign = self.ui.pickAlignmentLabel
        # self.currentGost = self.ui.gostPicked
        self.ui.filePicked.setText('')

        # события кнопок
        self.ui.pickFileButton.clicked.connect(self.pickFileButton_Clicked)
        self.ui.checkFile.clicked.connect(self.checkFile_Clicked)
        self.ui.choiceTitle.activated.connect(self.choiceTitleActive)
        self.ui.pickAligment.activated.connect(self.choiceAlignActive)
        # self.ui.choiceGost.activated.connect(self.choiceGostActive)
        self.ui.enterIndent.textEdited.connect(self.changeIndentLabel)
        self.ui.enterLineSpace.textEdited.connect(self.changeLineSpaceLabel)
        self.ui.window2_button.clicked.connect(self.open_second_window)  # Открытие второго окна для проверки по гостам

        # Подключаем события перетаскивания
        self.ui.dropLabel.dragEnterEvent = self.dragEnterEvent
        self.ui.dropLabel.dropEvent = self.dropEvent

        # Добавляем обработку событий перетаскивания файлов
        self.ui.filePicked.setAcceptDrops(True)

        self.ui.choiceTitle.addItems(TITLE.keys())
        self.ui.pickAligment.addItems(SETTER.keys())
        # self.ui.choiceGost.addItems(GOST.keys())
        self.ui.titlePicked.setText(self.ui.choiceTitle.currentText())
        self.ui.pickAlignmentLabel.setText(self.ui.pickAligment.currentText())
        # self.ui.gostPicked.setText(self.ui.choiceGost.currentText())

        self.plain_text = QPlainTextEdit()
        self.plain_text.setReadOnly(READ_ONLY)

        layout = QVBoxLayout(self)
        layout.addWidget(self.plain_text)

        w = QWidget()
        w.setLayout(layout)
        self.ui.answer.setWidget(w)

        self.setWindowTitle("ML title")

        self.showMaximized()  # Полноэкранный режим

        self.second_window = None

    def open_second_window(self):
        self.second_window = SecondWindow(self)
        self.second_window.show()

    def changeIndentLabel(self, text):
        self.ui.enterIndentLabel.setText(text + ' см')

    def changeLineSpaceLabel(self, text):
        self.ui.enterLineSpaceLabel.setText(text + ' см')

    def choiceTitleActive(self, index):
        self.ui.titlePicked.setText(self.ui.choiceTitle.itemText(index))
        self.currentTitle = self.ui.titlePicked

    def choiceAlignActive(self, index):
        self.ui.pickAlignmentLabel.setText(self.ui.pickAligment.itemText(index))
        self.currentAlign = self.ui.pickAlignmentLabel

    # def choiceGostActive(self, index):
    #     self.ui.gostPicked.setText(self.ui.choiceGost.itemText(index))
    #     self.currentGost = self.ui.gostPicked

    def pickFileButton_Clicked(self):
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         "Выбрать файл",
                                                         '.',
                                                         'Word files (*.docx)')
        if filename == '':
            self.ui.filePicked.setText('Файл не выбран.')
            self.pathFile = ''
        else:
            self.pathFile = filename
            filename = filename.split('/')[-1]
            self.ui.filePicked.setText(filename)

    def checkFile_Clicked(self):
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
            if self.ui.enterIndent.text() == '':
                self.ui.enterIndent.setText('0')
            document = Document(self.pathFile)
            text = checkIndents(self.ui.enterIndent.text(), document)
            text += checkSetters(self.currentAlign.text(), document)
            text += checkLineSpaces(self.ui.enterLineSpace.text(), document)
            text += checkTitles(self.currentTitle.text(), document)
            # text += checkTitles(self.currentGost.text(), document)
            document.save(self.pathFile)
            self.plain_text.setPlainText(text)

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
            self.ui.filePicked.setText(filename)
            self.pathFile = file_path
            event.acceptProposedAction()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec_()
