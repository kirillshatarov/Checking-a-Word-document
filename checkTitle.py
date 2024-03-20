from docx import Document
from constants import CORRECTSEQUENCE, TITLE


def checkTitles(currentTitle, document):
    titleOnRussia = currentTitle
    currentTitle = TITLE[currentTitle]
    count = 1
    text = 'ЗАГОЛОВКИ.\n'

    for line in document.paragraphs:
        if line.style.name in TITLE.values():
            try:
                if count != CORRECTSEQUENCE[line.text.capitalize()]:
                    arr = []
                    for key, val in CORRECTSEQUENCE.items():
                        if val == count:
                            arr.append(key)
                    if arr:
                        text += f'Неверный порядок заголовка.\nОжидалось: "{arr[0]}"\t Получили: "{line.text}".\n'
                if line.style.name == currentTitle:
                    text += f'Верно оформлен заголовок: "{line.text}".\n'
                else:
                    text += f'Заголовок "{line.text}" оформлен в неверном стиле "{[key for key, val in TITLE.items() if line.style.name == val][0]}".\n' \
                            f'Этот заголовок ожидался в стиле "{titleOnRussia}".\n'
            except KeyError:
                text += f'"{line.text}" не является стандартом госта. ' \
                        f'Ожидалось: "{[key for key, value in CORRECTSEQUENCE.items() if value == count][0]}".\n'
            finally:
                text += '-----\n'
                count += 1

    return text
