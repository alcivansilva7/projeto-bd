from lib_exemplo import *
from lib_database import *
from constantes import *
from conexao_db import *

retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

if not retConexao[0]:
    print(retConexao[1])
    sys.exit()


connDB = retConexao[1]

print('\nConsultando tipos de servidores por campus')
retorno = consultaServidoresCampus(connDB)
if retorno[0] == True:
    for i in retorno[1]:
        print(f"\nCampus: {i[0]}, Tipo de servidor: {i[1]}, Quantidade: {i[2]}")
else:
    print(retorno[0])
    sys.exit()

print('\nConsultando docentes por disciplina')
retorno = consultaDocenteDisciplina(connDB)
if retorno[0] == True:
    for i in retorno[1]:
        print(f"\nDocente: {i[0]}, Disciplina: {i[1]}")
else:
    print(retorno[0])
    sys.exit()

print('\nConsultando quantidade de docentes por disciplinas e por campus')
retorno = consultaDisciplinaCampus(connDB)
if retorno[0] == True:
    for i in retorno[1]:
        print(f"\nDisciplina: {i[0]}, Campus: {i[1]}, Quantidade: {i[2]}")
else:
    print(retorno[0])
    sys.exit()



connDB.close()