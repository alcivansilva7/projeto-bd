import sys
from entidade.conexao_db import *
from entidade.lib_exemplo import *
from view.exemplo_database import *
from view.consultas import *


def main():
    retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

    if not retConexao[0]:
        print(retConexao[1])
        sys.exit()

    connDB = retConexao[1]
    while True:
        opcao = int(input('''
        Escolha sua opção:
        0 - Sair do programa
        1 - Inserir dados no banco
        2 - Consultar tipos de servidores por campus
        3 - Consultar docentes por disciplina
        4 - Consultar quantidade de docentes por disciplinas e por campus
        >> '''))

        if opcao == 0:
            print("ENCERRANDO O PROGRAMA!")
            connDB.close()
            sys.exit()
        elif opcao == 1:
            inserirDados()
        elif opcao == 2:
            servidoresCampus(connDB)
        elif opcao == 3:
            docentesDisciplina(connDB)
        elif opcao == 4:
            quantidadeDocentesDisciplinas(connDB)

if __name__ == "__main__":
    main()