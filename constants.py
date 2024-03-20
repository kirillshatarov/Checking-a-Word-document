from docx.enum.text import WD_ALIGN_PARAGRAPH

SIZE_L, SIZE_W = 550, 850  # размеры окна
READ_ONLY = True  # только чтение

# Все возможные заголовки
TITLE = {'Заголовок': 'Title',
         'Заголовок 1': 'Heading 1',
         'Заголовок 2': 'Heading 2',
         'Заголовок 3': 'Heading 3',
         'Заголовок 4': 'Heading 4'}

# Тут должен быть правильный порядок Заголовков
CORRECTSEQUENCE = {"Содержание": 1,
                   "Введение": 2,
                   "Теоретическая часть": 3,
                   "Принцип работы протоколов http и https": 4,
                   "База данных mongodb": 5}

# Выравнивание параграфов
SETTER = {
    "по ширине": WD_ALIGN_PARAGRAPH.JUSTIFY, "по левому": WD_ALIGN_PARAGRAPH.LEFT,
    "по правому": WD_ALIGN_PARAGRAPH.RIGHT, "по центру": WD_ALIGN_PARAGRAPH.CENTER,
    "по умолчанию": WD_ALIGN_PARAGRAPH is None
}

# ГОСТЫ
GOST = {
    "ГОСТ 7.32-2017": "Presets 1",
    "ГОСТ 2.105-2019": "Presets 2",
    "Конкурс статей": "Presets 3"}
