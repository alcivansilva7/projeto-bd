# Importa a bibioteca do sistema
import sys
# Importando as informações necessárias para poder inserir os dados no banco
from entidade.lib_exemplo import *
from dao.lib_database import *
from entidade.constantes import *
from entidade.conexao_db import *

# Lê de fato o arquivo e insere os dados no banco de acordo com suas tabelas
# Também verifica os que não há necessidade de repetir e insere no banco sem as repetições
def inserirDados():
    retLeitura  = lerArquivo(APP_DIR + '\\dados_extraidos_recursos_servidores.csv')

# Caso dê algum erro na leitura do arquivo encerra o programa
    if not retLeitura[0]:
        print(retLeitura[1])
        sys.exit()

    print('\nTratando os dados lidos')
    dados_lidos = retLeitura[1]
# Gerando SETS com os dados a serem inseridos nas tabelas exceto na tabela SERVIDOR

    setCategoria                = set(map(lambda c: c['categoria'], dados_lidos.values()))
    setCargo                    = set(map(lambda c: c['cargo'], dados_lidos.values()))
    setSetorSiape               = set(map(lambda c: c['setor_siape'], dados_lidos.values()))
    setDisciplinaIngresso       = set(map(lambda c: c['disciplina_ingresso'], dados_lidos.values()))
    setSetorSuap                = set(map(lambda c: c['setor_suap'], dados_lidos.values()))
    setFuncao                   = set(map(lambda c: c['funcao'], dados_lidos.values()))
    setJornadaTrabalho          = set(map(lambda c: c['jornada_trabalho'], dados_lidos.values()))
    setCampus                   = set(map(lambda c: c['campus'], dados_lidos.values()))

# Abre a conexão com o banco
    retConexao = conectaDB(DB_HOST, DB_NAME, DB_USER, DB_PASS)

# Encerra o programa caso haja algum erro na conexão e exibe o erro encontrado
    if not retConexao[0]:
        print(retConexao[1])
        sys.exit()

# Armazenna os dados da conexão com o banco
    connDB = retConexao[1]

# Insere os dados na tabela CATEGORIA
    print('\nInserindo dados na tabela CATEGORIA')
    dictCategoria = dict()
    for categoria in setCategoria:
        if not categoria: categoria = '------'
        retorno = insereCategoria(categoria, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCategoria[categoria] = retorno[1]

#Insere os dados na tabela CARGO
    print('\nInserindo dados na tabela CARGO')
    dictCargo = dict()
    for cargo in setCargo:
        if not cargo: cargo = '------'
        retorno = insereCargo(cargo, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCargo[cargo] = retorno[1]

#Insere os dados na tabela SETOR_SIAPE
    print('\nInserindo dados na tabela SETOR_SIAPE')
    dictSetorSiape = dict()
    for setorSiape in setSetorSiape:
        if not setorSiape: setorSiape = '------'
        retorno = insereSiape(setorSiape, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictSetorSiape[setorSiape] = retorno[1]

#Insere os dados na tabela DISCIPLINA_INGRESSO
    print('\nInserindo dados na tabela DISCIPLINA_INGRESSO')
    dictDisciplinaIngresso = dict()
    for disciplinaIngresso in setDisciplinaIngresso:
        if not disciplinaIngresso: disciplinaIngresso = '------'
        retorno = insereDisciplina(disciplinaIngresso, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictDisciplinaIngresso[disciplinaIngresso] = retorno[1]

#Insere os dados na tabela SETOR SUAP
    print('\nInserindo dados na tabela SETOR_SUAP')
    dictSetorSuap = dict()
    for setorSuap in setSetorSuap:
        if not setorSuap: setorSuap = '------'
        retorno = insereSuap(setorSuap, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictSetorSuap[setorSuap] = retorno[1]

#Insere os dados na tabela FUNCAO
    print('\nInserindo dados na tabela FUNCAO')
    dictFuncao = dict()
    for funcao in setFuncao:
        if not funcao: funcao  = '------'
        retorno = insereFuncao(funcao, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictFuncao[funcao] = retorno[1]

#Insere os dados na tabela JORNADA_TRABALHO
    print('\nInserindo dados na tabela JORNADA_TRABALHO')
    dictJornadaTrabalho = dict()
    for jornadaTrabalho in setJornadaTrabalho:
        if not jornadaTrabalho: jornadaTrabalho = '------'
        retorno = insereJornada(jornadaTrabalho, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictJornadaTrabalho[jornadaTrabalho] = retorno[1]

#Insere os dados na tabela CAMPUS
    print('\nInserindo dados na tabela CAMPUS')
    dictCampus = dict()
    for campus in setCampus:
        if not campus: campus = '------'
        retorno = insereCampus(campus, connDB)
        if not retorno[0]:
            print(retorno[1])
            continue
        dictCampus[campus] = retorno[1]

#Insere os dados na tabela SERVIDOR
    print('\nInserindo dados na tabela SERVIDOR')
    tupleCampos = tuple(['id_categoria'         ,   'id_cargo'      ,  'id_setor'       ,
                        'id_disciplina'        ,   'id_setor_suap' ,  'nome'           ,
                        'id_funcao'            ,   'id_jornada'    ,  'telefones'   ,
                        'matricula_servidor'   ,   'link_lattes'     ,  'id_campus'      ,   
                        'link_fotos'])


    for k,v in dados_lidos.items():
        if dados_lidos[k]['categoria']                  == '': dados_lidos[k]['categoria']                  = '------'
        if dados_lidos[k]['cargo']                      == '': dados_lidos[k]['cargo']                      = '------'
        if dados_lidos[k]['setor_siape']                == '': dados_lidos[k]['setor_siape']                = '------'
        if dados_lidos[k]['disciplina_ingresso']        == '': dados_lidos[k]['disciplina_ingresso']        = '------'
        if dados_lidos[k]['setor_suap']                 == '': dados_lidos[k]['setor_suap']                 = '------'
        if dados_lidos[k]['funcao']                     == '': dados_lidos[k]['funcao']                     = '------'
        if dados_lidos[k]['jornada_trabalho']           == '': dados_lidos[k]['jornada_trabalho']           = '------'
        if dados_lidos[k]['campus']                     == '': dados_lidos[k]['campus']                     = '------'

        dados_lidos[k]['categoria']                  = dictCategoria[dados_lidos[k]['categoria']]
        dados_lidos[k]['cargo']                      = dictCargo[dados_lidos[k]['cargo']]
        dados_lidos[k]['setor_siape']                = dictSetorSiape[dados_lidos[k]['setor_siape']]
        dados_lidos[k]['disciplina_ingresso']        = dictDisciplinaIngresso[dados_lidos[k]['disciplina_ingresso']]
        dados_lidos[k]['setor_suap']                 = dictSetorSuap[dados_lidos[k]['setor_suap']]
        dados_lidos[k]['funcao']                     = dictFuncao[dados_lidos[k]['funcao']]
        dados_lidos[k]['jornada_trabalho']           = dictJornadaTrabalho[dados_lidos[k]['jornada_trabalho']]
        dados_lidos[k]['campus']                     = dictCampus[dados_lidos[k]['campus']]


        tupleValores = tuple(v.values())

        retorno = insereServidor(tupleCampos, tupleValores, connDB)

        if not retorno[0]: print(retorno[1])
#ENCERRA A CONEXÃO COM O BANCO
    connDB.close()