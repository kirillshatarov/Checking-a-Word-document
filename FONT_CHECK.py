from docx import Document

def check_font_properties(docx_file):
    doc = Document(docx_file)

    # Задаем ожидаемые значения размера шрифта и стиля шрифта
    expected_font_size = 14
    expected_font_style = "Times New Roman"

    for i, paragraph in enumerate(doc.paragraphs):
        # print(paragraph.style.font.size)
        for run in paragraph.runs:
            # Проверяем соответствие размера шрифта
            if run.font.size is not None:
                if run.font.size.pt != expected_font_size:
                    print(f"Несоответствие размера шрифта в абзаце: {i}. Размер = {run.font.size.pt}")
            else:
                print(f"Размера шрифта в абзаце: {i} ОК. Размер = {run.font.size} (по умолчанию)")

            # Проверяем соответствие стиля шрифта
            if run.font.name is not None:
                if run.font.name != expected_font_style:
                    print(f"Несоответствие стиля шрифта в абзаце: {i}. Стиль = {run.font.name}")
            else:
                print(f"Стиль шрифта в абзаце: {i} ОК. Стиль = {paragraph.style.font.name} (по умолчанию)")


# Пример использования
check_font_properties("test.docx")
