from docx import Document
from constants import TITLE


def checkIndents(currentIndent, document):
    paragraphs = document.paragraphs
    currentIndent = currentIndent.replace(',', '.')
    result = f'ОТСТУПЫ ПЕРВОЙ СТРОКИ АБЗАЦЕВ. ({currentIndent} см)\n'
    for paragraph in paragraphs:
        # Проверяем, не является ли абзац заголовком
        if paragraph.style.name not in TITLE.values():
            # проверяем, является ли абзац - списоком, если да, то идем дальше по документу.
            if len(paragraph._element.xpath('./w:pPr/w:numPr')) > 0:
                continue
            if paragraph.paragraph_format.first_line_indent is not None:
                # Округление так как в first_line_indent.cm не ровное число, а ~1.2505972222222221
                if round(paragraph.paragraph_format.first_line_indent.cm, 2) != float(currentIndent):
                    result += f'Абзац: "{paragraph.text[:25]}" оформлен неверно. Его отступ ' \
                              f'составляет: {round(paragraph.paragraph_format.first_line_indent.cm, 2)} см.\n-----\n'

    if result.count('\n') == 1:
        return "Все отступы оформлены верно."
    return result + 'Все остальные отступы оформлены верно.\n-----\n-----\n'
