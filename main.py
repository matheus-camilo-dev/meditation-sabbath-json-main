from dotenv import load_dotenv
import main_pt as pt_meditation
import main_es as es_meditation

ENVIRONMENT_PATH = './environment/.env'

if __name__ == '__main__':
    load_dotenv(ENVIRONMENT_PATH)
    pt_meditation.run()
    print("")
    es_meditation.run()
