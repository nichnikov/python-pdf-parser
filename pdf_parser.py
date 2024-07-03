import PyPDF2
# Для анализа структуры PDF и извлечения текста
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure
# Для извлечения текста из таблиц в PDF
import pdfplumber
# Для извлечения изображений из PDF
from PIL import Image
from pdf2image import convert_from_path
# Для выполнения OCR, чтобы извлекать тексты из изображений 
import pytesseract 
# Для удаления дополнительно созданных файлов
import os


def text_extraction(element):
    # Извлекаем текст из вложенного текстового элемента
    line_text = element.get_text()
    
    # Находим форматы текста
    # Инициализируем список со всеми форматами, встречающимися в строке текста
    line_formats = []
    for text_line in element:
        if isinstance(text_line, LTTextContainer):
            # Итеративно обходим каждый символ в строке текста
            for character in text_line:
                if isinstance(character, LTChar):
                    # Добавляем к символу название шрифта
                    line_formats.append(character.fontname)
                    # Добавляем к символу размер шрифта
                    line_formats.append(character.size)
    # Находим уникальные размеры и названия шрифтов в строке
    format_per_line = list(set(line_formats))
    
    # Возвращаем кортеж с текстом в каждой строке вместе с его форматом
    return (line_text, format_per_line)

# "test1_en.pdf"
pdf_path = os.path.join("data", "test2_ru.pdf")

pages_texts = []
for pagenum, page in enumerate(extract_pages(pdf_path)):
    if pagenum > 5:
        break
    print(pagenum, page)
    text = ""
    for element in page:
         if isinstance(element, LTTextContainer):
             text += " " + text_extraction(element)[0]
             # print(text_extraction(element))
    pages_texts.append(text)

for p_tx in pages_texts:
    print(p_tx) 