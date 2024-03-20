import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QComboBox, QLineEdit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Главный QComboBox GOST
        self.main_combobox = QComboBox(self)
        self.main_combobox.addItems(["ГОСТ 7.32-2017", "ГОСТ 2.105-201", "Конкурс статей"])
        self.main_combobox.currentIndexChanged.connect(self.updateValues)
        layout.addWidget(self.main_combobox)

        # Первый QComboBox и QLineEdit
        self.combobox1 = QComboBox(self)
        self.lineedit1 = QLineEdit(self)
        layout.addWidget(self.combobox1)
        layout.addWidget(self.lineedit1)

        # Второй QComboBox и QLineEdit
        self.combobox2 = QComboBox(self)
        self.lineedit2 = QLineEdit(self)
        layout.addWidget(self.combobox2)
        layout.addWidget(self.lineedit2)

        self.updateValues(0)  # Инициализация значений по умолчанию

        self.setGeometry(100, 100, 650, 450)
        self.setWindowTitle('QComboBox Example')
        self.show()

    def updateValues(self, index):
        # Определяем значения для каждого пресета
        presets_values = {
            "ГОСТ 7.32-2017": {"ComboBox1": ["Заголовок", "Заголовок 1", "Заголовок 2", "Заголовок 3", "Заголовок 4"],
                               "LineEdit1": "1,25",
                               "ComboBox2": ["по ширине", "по левому", "по правому", "по центру", "по умолчанию"],
                               "LineEdit2": "1,5"},
            "ГОСТ 2.105-201": {"ComboBox1": ["Заголовок 1", "Заголовок", "Заголовок 2", "Заголовок 3", "Заголовок 4"],
                               "LineEdit1": "1,27",
                               "ComboBox2": ["по левому", "по ширине", "по правому", "по центру", "по умолчанию"],
                               "LineEdit2": "1"},
            "Конкурс статей": {"ComboBox1": ["Заголовок", "Заголовок 1", "Заголовок 2", "Заголовок 3", "Заголовок 4"],
                               "LineEdit1": "1,25",
                               "ComboBox2": ["по умолчанию", "по ширине", "по левому", "по правому", "по центру"],
                               "LineEdit2": "1"},
        }

        preset_values = presets_values[self.main_combobox.currentText()]

        # Заполняем первый QComboBox и QLineEdit
        self.combobox1.clear()
        self.combobox1.addItems(preset_values["ComboBox1"])
        self.lineedit1.setText(preset_values["LineEdit1"])

        # Заполняем второй QComboBox и QLineEdit
        self.combobox2.clear()
        self.combobox2.addItems(preset_values["ComboBox2"])
        self.lineedit2.setText(preset_values["LineEdit2"])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    sys.exit(app.exec_())
