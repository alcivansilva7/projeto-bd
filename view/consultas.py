#Importa os resultados das consultas
from dao.lib_database import *
#Importa a biblioteca dos sistema
import sys

#Exibe os resultados da consulta de tipos de servidores por campus
def servidoresCampus(conexaoDB):
    print('\nConsultando tipos de servidores por campus')
    retorno = consultaServidoresCampus(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nCampus: {i[0]}, Tipo de servidor: {i[1]}, Quantidade: {i[2]}")
    else:
        print(retorno[0])
        sys.exit()

#Exibe os resultados da consulta de docentes por disciplina
def docentesDisciplina(conexaoDB):
    print('\nConsultando docentes por disciplina')
    retorno = consultaDocenteDisciplina(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nDocente: {i[0]}, Disciplina: {i[1]}")
    else:
        print(retorno[0])
        sys.exit()

#Exibe os resultados da consulta de quantidade de docentes por disciplina e por campus
def quantidadeDocentesDisciplinas(conexaoDB):
    print('\nConsultando quantidade de docentes por disciplinas e por campus')
    retorno = consultaDisciplinaCampus(conexaoDB)
    if retorno[0] == True:
        for i in retorno[1]:
            print(f"\nDisciplina: {i[0]}, Campus: {i[1]}, Quantidade: {i[2]}")
    else:
        print(retorno[0])
        sys.exit()