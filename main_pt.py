import os
from dotenv import load_dotenv

from src.core import main
import src.pt_meditation_lib as pt_meditation_lib

ENVIRONMENT_PATH = './environment/.env'

def run():
    print("Meditação Por do Sol, Idioma: pt-br")
    main(
        pt_meditation_lib.extract_text_from_pdf,
        pdf_file_name=os.getenv('PT_PDF_FILE_NAME', 'files/PDF-MetitaçãoPordoSol-pt.pdf'),
        start_page=int(os.getenv('PT_START_PAGE_NUMBER', '5')),
        end_page=int(os.getenv('PT_END_PAGE_NUMBER', '57')),
        json_output_file_name=os.getenv("PT_OUTPUT_FILE_NAME", '../outputs/output-pt.json')
    )


if __name__ == '__main__':
    load_dotenv(ENVIRONMENT_PATH)
    run()
