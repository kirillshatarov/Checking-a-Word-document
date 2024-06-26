from docx.enum.text import WD_ALIGN_PARAGRAPH

# !!!!!! ГОСТЫ - 7.32-2017, 2.105-2019, Статьи !!!!!!

SIZE_L, SIZE_W = 450, 670  # размеры окна
READ_ONLY = True  # только чтение
# тип шрифта
FONT_TYPE = "Times New Roman"
# размер шрифта
FONT_SIZE = {'7.32-2017': 12,
             '2.105-2019': 14,
             'Статьи': 14}
# цвет шрифта
FONT_COLOR = {'7.32-2017': 'black',
              '2.105-2019': 'black',
              'Статьи': 'black'}
# Поля
FIELD = {'7.32-2017': {
    'left': '30',
    'right': '15',
    'bottom': '20',
    'top': '20'
},
    '2.105-2019': {
        'left': '>3',
        'right': '>3',
        'bottom': '>10',
        'top': '>10'
    },
    'Статьи': {
        'left': '20',
        'right': '20',
        'bottom': '20',
        'top': '20'
    }
}
# Отступ первой строки (абзацный отступ)
paragraphIndention = {
    '7.32-2017': '12.5',
    '2.105-2019': '12.5-17',
    # Для статьи нет отступа первой строки
}

# Интервал между абзацами.
# Ключ - ГОСТ. Значения - список, в котором
# первый элемент - интервал ДО абзаца,
# второй элемент - интервал ПОСЛЕ абзаца
INTERVALS = {'7.32-2017': [0, 0],
             '2.105-2019': [0, 0],
             'Статьи': [0, 0]}

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

CORRECTSEQUENCE_GOST = {
    '7.32': {
        'Титульный лист': 1,
        'Список исполнителей': 2,
        'Сожержание': 3,
        'Термины и определения': 4,
        'Перечень сокращений и обозначений': 5,
        'Введение': 6,
        'Основная часть': 7,
        'Заключение': 8,
        'Список использованных источников': 9,
        'Приложения': 10
    },
    '2.105-2019': {
        'Титульный лист': 1,
        'Обозначения и сокращения': 2,
        'Термины и определения': 3,
        'Приложения': 4,
        'Ссылочные нормативные документы': 5,
        'Библиография': 6
    },
    'Статьи': {
        'Заголовок': 1,
        'Список литературы': 2,
    }
}

# Выравнивание абзацев ГОСТЫ
SETTER_GOST = {
    '7.32-2017': {
        'heading': WD_ALIGN_PARAGRAPH.LEFT,
        'text': WD_ALIGN_PARAGRAPH.LEFT,
        'numberPage': WD_ALIGN_PARAGRAPH.RIGHT
    }
    # Для остальных гостов, не предусмотрено выравнивание.
}

# Межстрочный интервал
LINE_SPACE = {
    '7.32-2017': '1.5',
    '2.105-2019': '1.5-2',
    'Статьи': '1.5'

}

# Выравнивание абзацев
SETTER = {
    "по ширине": WD_ALIGN_PARAGRAPH.JUSTIFY, "по левому": WD_ALIGN_PARAGRAPH.LEFT,
    "по правому": WD_ALIGN_PARAGRAPH.RIGHT, "по центру": WD_ALIGN_PARAGRAPH.CENTER,
    "по умолчанию": WD_ALIGN_PARAGRAPH is None
}
