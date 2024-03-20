from constants import TITLE, SETTER


# Проверка выравнивания
def checkSetters(currentSetter, document):
    currentSetterRussian = currentSetter
    currentSetter = SETTER[currentSetter]
    paragraphs = document.paragraphs
    text = 'ВЫРАВНИВАНИЕ АБЗАЦЕВ.\n'
    for index, paragraph in enumerate(paragraphs):
        if paragraph.style.name not in TITLE.values():
            if currentSetter != paragraph.alignment and paragraph.alignment is not None:
                text += f'Строка: "{paragraph.text[:25]}" не соответствует критерию. ' \
                        f'Выранивание должно быть: "{currentSetterRussian}".\n-----\n'
    if text == 'ВЫРАВНИВАНИЕ АБЗАЦЕВ.\n':
        return text + "Все оформлено верно.\n-----\n-----\n"
    return text + "Все остальные абзацы оформлены верно.\n-----\n-----\n"
