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
    strSQL = f'INSERT INTO cargo (nome_cargo) VALUES (\'{descricao}\') RETURNING id_cargo;'
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
    strSQL = f'INSERT INTO campus (nome_campus) VALUES (\'{descricao}\') RETURNING id_campus;'
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
    strSQL = f'INSERT INTO jornada_trabalho (jornada) VALUES (\'{descricao}\') RETURNING id_jornada;'
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
    strSQL = f'INSERT INTO setor_siape (nome_setor) VALUES (\'{descricao}\') RETURNING id_setor;'
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
    strSQL = f'INSERT INTO setor_suap (nome_setor_suap) VALUES (\'{descricao}\') RETURNING id_setor_suap;'
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
    strSQL = f'INSERT INTO disciplina_ingresso (nome_disciplina) VALUES (\'{descricao}\') RETURNING id_disciplina;'
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


def insereFuncao(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO funcao (nome_funcao) VALUES (\'{descricao}\') RETURNING id_funcao;'
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
    


def insereCategoria(descricao: str, conexao):
    inserido = False
    idRetorno = None
    strSQL = f'INSERT INTO categoria (nome_categoria) VALUES (\'{descricao}\') RETURNING id_categoria;'
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
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n{valores}\n\n'
    else:
        inserido = True
        idRetorno = cursorTable.fetchone()[0]
        conexao.commit()
    finally:
        return inserido, idRetorno
    
def consultaServidoresCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM servidores_campus ORDER BY sigla;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno



def consultaDocenteDisciplina(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM docentes_disciplinas;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno
    

def consultaDocenteDisciplina(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM docentes_disciplinas;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno
    
def consultaDisciplinaCampus(conexao):
    consultado = False
    idRetorno = None
    strSQL = 'SELECT * FROM disciplinas_campus ORDER BY sigla;'
    try:
        cursorTable = conexao.cursor()
        cursorTable.execute(strSQL)
    except:
        conexao.rollback()
        idRetorno = f'ERRO: {sys.exc_info()[0]} \n{strSQL} \n'
    else:
        consultado = True
        idRetorno = cursorTable.fetchall()
        conexao.commit()
    finally:
        return consultado, idRetorno