from datetime import datetime
import json
import os
import re


def read_bible_books(file_path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        bible_books = [line.strip() for line in file.readlines() if line.strip()]
    return bible_books

def format_paragraphs(remaining_text: str) -> str:
    cleaned_text = ""
    index = 0
    while index < len(remaining_text):
        if remaining_text[index] == "\n":
            if index + 1 < len(remaining_text):
                if remaining_text[index + 1].isupper() or remaining_text[index + 1] == "-":
                    cleaned_text += "\n\t"
            index += 1
        else:
            cleaned_text += remaining_text[index]
            index += 1
    return cleaned_text

def get_verse_text_and_remaining_text(remaining_text:str, bible_books:list[str]) -> list[str]:
    verse_text = remaining_text
    for book in bible_books:
        if book in remaining_text:
            verse_text, _, _ = remaining_text.partition(book)
            break

    remaining_text = remaining_text.replace(verse_text, "")
    verse_text = verse_text.replace("\n", "")
    return [verse_text, remaining_text]

def get_date_by_text(transform_month_names_to_numbers_function, date_temp: str) -> list[str]:
    date_temp += " de 2023"
    date_temp = re.sub(r"\s{2,}", " ", date_temp)
    date_temp = transform_month_names_to_numbers_function(date_temp)
    date_temp = date_temp.replace("de ", "")
    date_temp = date_temp.replace(" ", "/")
    try:
        date = datetime.strptime(date_temp, "%d/%m/%Y")
    except ValueError:
        date = None
    return [date, date_temp]

def remove_unnecessary_text(cleaned_text: str) -> str:
    return cleaned_text.replace(
        "46149 – Meditação Por do Sol - 2023\nDesigner Editor(a) Coor. Ped. C. Q. R. F . Marketing14 October 2022 9:50 am\nP1\nP2", ""
    )

def datetime_to_string(date) -> str:
    if date is None:
        return ""
    return date.strftime("%Y-%m-%d")

def get_result_dict(page_num: int, cleaned_text:str, date_display:datetime, date_temp:datetime, date:datetime, title:str, verse_text:str, verse_ref:str) -> dict:
    return {
        "page_number": page_num + 1,
        "text": cleaned_text.strip(),
        "date_display": date_display.strip(),
        "date_temp": date_temp.strip(),
        "date": datetime_to_string(date),
        "title": title.strip(),
        "verse_text": verse_text.strip(),
        "verse_ref": verse_ref.strip()
    }   

def main(extract_pdf_function, pdf_file_name:str, start_page:int, end_page:int, json_output_file_name:str) -> None:
    bible_books_file_path = os.getenv('BIBLE_BOOKS_FILE_PATH', 'files/bible_books.txt')
    bible_books = read_bible_books(bible_books_file_path)

    extracted_text_records = extract_pdf_function(pdf_file_name, start_page, end_page, bible_books)

    data = {
        os.getenv('GENERATED_TIME_KEY', 'generated_time'): datetime.now(),
        os.getenv('MAIN_DATA_KEY', 'text_records'): extracted_text_records
    }

    pdf_dir = os.path.dirname(pdf_file_name)

    path = f'.\{json_output_file_name.split("/")[0]}'
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
    
    with open(json_output_file_name, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, default=datetime_to_string)

    print("Text extracted from page", start_page, "to", end_page, "has been saved to", json_output_file_name)
