# Meditation-Sabbath-Json-Main
- ## Descrição rápida
### Esse script tem como objetivo "automatizar" mais o processo de atualização de meditação de por do sol, e ao mesmo tempo, possibilitar a exibição no app 7me da meditação de forma nativa. Por meio das meditações de por do sol em pdf, da configuração nas variáveis de ambiente, e da execução do script, é gerado um ou mais arquivos json com os dados de cada página da meditação.


&nbsp;
- ## Requisitos
    - ### Python 3.8+ com pip 22.0.4+

&nbsp;
- ## Passo a passo para executar o software no Windows
### 0.1 Configuração e ativação do ambiente virtual (opcional)
#### Executar o seguinte comando no terminal na pasta raiz do projeto
```cmd
python -m venv env
env\Scripts\activate
```

Sempre que for executar o script, verifique se o ambiente virtual está ativado (aparece o nome '(env)' na linha de commando). Se não estive ativo, basta rodar na pasta raiz o último comando acima.

&nbsp;
### 1. Instalação das dependencias
#### Executar o seguinte comando no terminal na pasta raiz do projeto
```cmd
pip install -r requirements.txt
```

&nbsp;
### 2. Configuração das variáveis de ambiente
#### Neste caso é necessário conferir se as informações em `./environment/.env` estão corretas e alterar se necessário.

&nbsp;
### 3. Execução do script
#### Executar o seguinte comando no terminal na pasta raiz do projeto

##### 3.1 Execução apenas da versão português
```cmd
python main_pt.py
```

##### 3.2 Execução apenas da versão espanhol
```cmd
python main_es.py
```

##### 3.3 Execução apenas da versão português e espanhol
```cmd
python main.py
```

O(s) arquivo(s) resultantes são armazenados na pasta `./outputs/`, com os nomes `output-pt.json` para português e `output-es.json` para espanhol;

&nbsp;
- ## Descrição de pastas
    - ### `environment/`
        #### Variáveis de ambiente do projeto
    - ### `files/`
        #### Arquivos staticos como: os *pdfs* a serem analizados e a lista dos livros da bíblia nos dois idiomas
    - ### `outputs/`
        #### Pasta onde fica os resulados dos scripts, ou seja, os JSON gerados. Criada após a geração do primeiro JSON, caso não exista a pasta.
    - ### `src/`
        #### Aqui estão os códigos em python para geração dos JSON
    - ### `env/` (opcional)
        #### Pasta com as dependências do projeto. Pasta não versionada. Semelhante a node_modules do javascript

&nbsp;
- ## Descrição arquivo de ambiente `./environment/.env`
    - ### BIBLE_BOOKS_FILE_PATH
        #### Caminho da lista de nomes livros da bíblia nos idiomas português e espanhol

    - ### PT_PDF_FILE_NAME
        #### Caminho do pdf no idioma português para geração do JSON

    - ### PT_START_PAGE_NUMBER
        #### Página inicial do pdf em português para geração do JSON

    - ### PT_END_PAGE_NUMBER
        #### Página final do pdf em português para geração do JSON

    - ### PT_OUTPUT_FILE_NAME
        #### Caminho do arquivo JSON gerado no idioma espanhol

    - ### ES_PDF_FILE_NAME
        #### Caminho do pdf no idioma espanhol para geração do JSON

    - ### ES_START_PAGE_NUMBER
        #### Página inicial do pdf em espanhol para geração do JSON

    - ### ES_END_PAGE_NUMBER
        #### Página final do pdf em espanhol para geração do JSON

    - ### ES_OUTPUT_FILE_NAME
        #### Caminho do arquivo JSON gerado no idioma espanhol

    - ### GENERATED_TIME_KEY=generated_time
        ### Nome da chave do JSON para registro de data de geração do JSON
    - ### MAIN_DATA_KEY=text_records
        ### Nome da chave do JSON para registro dos dados gerados
