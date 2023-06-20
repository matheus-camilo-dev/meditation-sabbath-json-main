import PyPDF2
from src.core import *

def extract_text_from_pdf(pdf_path, start_page, end_page, bible_books):
    text_records = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(start_page, min(end_page, num_pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            date_display, _, remaining_text = text.partition("\n")
            remaining_text = re.sub(r"(\d)([A-Za-z])", r"\1 \2", remaining_text)

            if (page_num+1) >= 14:
                date_display = date_display[2:]
            else:
                date_display = date_display[1:]

            date_temp = date_display.replace("de ", "")

            date, date_temp = get_date_by_text(transform_month_names_to_numbers, date_display)

            title, _, remaining_text = remaining_text.partition("\n")
            
            verse_text, remaining_text = get_verse_text_and_remaining_text(remaining_text, bible_books)

            verse_text = verse_text.replace("(", "")
            verse_text = verse_text.replace('”', '')
            verse_text = verse_text.replace('“', '')
            
            verse_ref, _, remaining_text = remaining_text.partition("\n")
            verse_ref = verse_ref.replace(').', '')

            cleaned_text = format_paragraphs(remaining_text)
            cleaned_text = remove_unnecessary_text(cleaned_text)
            
            text_record = get_result_dict(page_num, cleaned_text, date_display, date_temp, date, title, verse_text, verse_ref)
            text_records.append(text_record)
    return text_records

def transform_month_names_to_numbers(date_temp):
    month_names = [
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre"
    ]
    for index, month_name in enumerate(month_names, start=1):
        date_temp = date_temp.replace(month_name, str(index))
    return date_temp