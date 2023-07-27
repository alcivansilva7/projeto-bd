# Importa SYS para retorar algum erro na leitura do arquivo caso ocorra
import sys
# Importa as informações do diretório
from entidade.constantes import *

# Essa função lê o arquivo e separa o cabeçalho e os dados
# Depois retorna os dados do arquivo para serem inseridos no banco de dados
def lerArquivo(nomeArquivo: str):
    lido = False
    dados_retorno = dict()
    try:
        arq_ = open(nomeArquivo, 'r', encoding=CODE_PAGE)
    except FileNotFoundError:
        dados_retorno = f'\nERRO: Arquivo Inexistente!'
    except:
        dados_retorno = f'\n ERRO: {sys.exc_info()[0]}'
    else:
        while True:
            linha = arq_.readline()[:-1]
            if not linha: break
            cabecalho =  linha.split(SEPARATOR)
            while True:
                linha = arq_.readline()[:-1]
                if not linha: break
                linha = linha.split(SEPARATOR)
                dados_retorno[linha[9]] = dict(zip(cabecalho, linha))
            lido = True
        arq_.close()
    finally:
        return lido, dados_retorno