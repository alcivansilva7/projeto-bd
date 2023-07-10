import psycopg2, sys

def conectaDB(server: str, database: str, dbuser: str, userpwd: str):
    conectado = False
    conexao = None
    try:
        conexao =  psycopg2.connect(f'dbname={database} user={dbuser} host={server} password={userpwd}')
    except:
        conexao = f'ERRO: {sys.exc_info()[0]}'
    else:
        conectado = True
    finally:
        return conectado, conexao
    
def insereCargo(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO cargo (nome_cargo) VALUES (\'{descricao}\') RETURNING nome_cargo;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_cargo FROM cargo WHERE nome_cargo = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CARGO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    

def insereCampus(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO campus (nome_campus) VALUES (\'{descricao}\') RETURNING nome_campus;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_campus FROM campus WHERE nome_campus = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CAMPUS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno


def insereJornada(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO jornada_trabalho (jornada) VALUES (\'{descricao}\') RETURNING jornada;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT jornada FROM jornada_trabalho WHERE jornada = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela JORNADA_TRABALHO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno


def insereSiape(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_siape (nome_setor) VALUES (\'{descricao}\') RETURNING nome_setor;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_setor FROM setor_siape WHERE nome_setor = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SETOR_SIAPE): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insereSuap(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO setor_suap (nome_setor_suap) VALUES (\'{descricao}\') RETURNING nome_setor_suap;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_setor_suap FROM setor_suap WHERE nome_setor_suap = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela SETOR_SUAP): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno


def insereDisciplina(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO disciplina_ingresso (nome_disciplina) VALUES (\'{descricao}\') RETURNING nome_disciplina;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_disciplina FROM disciplina_ingresso WHERE nome_disciplina = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela DISCIPLINA_INGRESSO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno


def insereCurriculo(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO curriculo_lattes (link_lattes) VALUES (\'{descricao}\') RETURNING link_lattes;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT link_lattes FROM curriculo_lattes WHERE link_lattes = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CURRICULO_LATTES): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno



def insereTelefones(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO telefones_institucionais (telefones) VALUES (\'{descricao}\') RETURNING telefones;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT telefones FROM telefones_institucionais WHERE telefones = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela TELEFONES_INSTITUCIONAIS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insereFuncao(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO funcao (nome_funcao) VALUES (\'{descricao}\') RETURNING nome_funcao;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_funcao FROM funcao WHERE nome_funcao = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela FUNCAO): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insereFotos(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO url_fotos (link_fotos) VALUES (\'{descricao}\') RETURNING link_fotos;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT link_fotos FROM url_fotos WHERE link_fotos = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela URL_FOTOS): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    


def insereCategoria(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO categoria (nome_categoria) VALUES (\'{descricao}\') RETURNING nome_categoria;'
    cursorTable = conexao.cursor()
    try:
        cursorTable.execute(strSQL)
    except psycopg2.erros.UniqueViolation:
        conexao.rollback()
        strSQL = f'SELECT nome_categoria FROM categoria WHERE nome_categoria = \'{descricao}\';'
        cursorTable.execute(strSQL)
        inserido =  True
        idRetorno = cursorTable.fetchone()[0]
    except:
        conexao.rollback()
        idRetorno = f'ERRO (Tabela CATEGORIA): {sys.exc_info()[0]} \n{descricao} \n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    

def insereServidor(campos: tuple, valores: tuple, conexao):
    inserido = False
    idRetorno = None
    strSQL = 'INSERT INTO servidor ('
    for i in campos:    strSQL += i + ', '
    strSQL = strSQL[:-2]
    strSQL += f') VALUES {valores} RETURNING matricula_servidor;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execyte(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n{valores}\n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno