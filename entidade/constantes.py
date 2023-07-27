# importa a biblioteca OS para poder obter o diretório atual
import os

# Obtendo o diretório atual pois o arquivo está no mesmo diretório
APP_DIR = os.path.dirname(os.path.abspath(__file__))

# Definindo a página de código de caracteres para Português do Brasil
# Dessa forma ele irá respeitar as acentuações de palavras na hora de inserir no banco
CODE_PAGE = "utf-8"

#Define o separador em ; para que ele saiba onde é o começo e o fim de cada coluna
SEPARATOR = ";"