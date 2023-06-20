import os
from dotenv import load_dotenv

from src.core import main
import src.es_meditation_lib as es_meditation_lib


ENVIRONMENT_PATH = './environment/.env'

def run():
    print("Meditação Por do Sol, Idioma: es")
    main(
        es_meditation_lib.extract_text_from_pdf,
        pdf_file_name=os.getenv('ES_PDF_FILE_NAME', 'files/PDF-MetitaçãoPordoSol-es.pdf'),
        start_page=int(os.getenv('ES_START_PAGE_NUMBER', '7')),
        end_page=int(os.getenv('ES_END_PAGE_NUMBER', '57')),
        json_output_file_name=os.getenv("ES_OUTPUT_FILE_NAME", '../outputs/output-es.json')
    )


if __name__ == '__main__':
    load_dotenv(ENVIRONMENT_PATH)
    run()
