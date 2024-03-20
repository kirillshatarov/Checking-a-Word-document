import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Main Window')

        self.button = QPushButton('Toggle Content', self)
        self.button.clicked.connect(self.toggle_content)

        self.label1 = QLabel('Content 1', self)
        self.label2 = QLabel('TERMINAL 2', self)
        self.button2 = QPushButton('Кнопка', self)
        self.button2.setGeometry(80, 80, 161, 41)

        self.label2.hide()  # Изначально скрываем вторую метку
        self.button2.hide()

        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        layout.addWidget(self.button2)

        self.setLayout(layout)

        self.initial_state = True  # Флаг для отслеживания начального состояния

    def toggle_content(self):
        if self.initial_state:
            self.label1.hide()
            self.label2.show()
            self.button2.show()
        else:
            self.label1.show()
            self.label2.hide()
            self.button2.hide()

        self.initial_state = not self.initial_state  # Изменяем флаг состояния


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
