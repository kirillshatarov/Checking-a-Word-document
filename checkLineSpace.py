def checkLineSpaces(currentLineSpace, document):
    currentLineSpace = currentLineSpace.replace(',', '.')
    paragraphs = document.paragraphs
    text = f'МЕЖСТРОЧНЫЙ ИНТЕРВАЛ. ({currentLineSpace} см)\n'
    for paragraph in paragraphs:
        if paragraph.paragraph_format.line_spacing != float(currentLineSpace) and \
                paragraph is not None:
            text += f'Абзац: "{paragraph.text[:25]}" не соотвествует межстрочному интервалу. ' \
                    f'У этого абзаца он составляет: {paragraph.paragraph_format.line_spacing}.\n-----\n'
    if text == f'МЕЖСТРОЧНЫЙ ИНТЕРВАЛ. ({currentLineSpace} см)\n':
        return text + 'Все абзацы оформлены верно.\n-----\n-----\n'
    return text + 'Все остальные абзацы оформлены верно.\n-----\n-----\n'
