CREATE DATABASE ifrn;

--DROP SCHEMA public CASCADE;
--CREATE SCHEMA public;

CREATE TABLE cargo(
    id_cargo    SERIAL NOT NULL,
    nome_cargo  VARCHAR(255),
    CONSTRAINT pk_id_cargo PRIMARY KEY (id_cargo),
    CONSTRAINT un_nome_cargo UNIQUE(nome_cargo)
);
CREATE TABLE campus(
    id_campus     SERIAL NOT NULL,
    nome_campus   VARCHAR(10) NOT NULL,
    CONSTRAINT pk_id_campus PRIMARY KEY (id_campus),
    CONSTRAINT un_nome_campus UNIQUE(nome_campus)
);
CREATE TABLE jornada_trabalho(
    id_jornada  SERIAL NOT NULL,
    jornada     VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_jornada PRIMARY KEY (id_jornada),
    CONSTRAINT un_jornada UNIQUE(jornada)
);
CREATE TABLE setor_siape(
    id_setor    SERIAL NOT NULL,
    nome_setor  VARCHAR(15) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_setor PRIMARY KEY (id_setor),
    CONSTRAINT un_nome_setor UNIQUE(nome_setor)
);
CREATE TABLE setor_suap(
    id_setor_suap   SERIAL NOT NULL,
    nome_setor_suap VARCHAR(15) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_setor_suap PRIMARY KEY (id_setor_suap),
    CONSTRAINT un_nome_setor_suap UNIQUE(nome_setor_suap)
);
CREATE TABLE disciplina_ingresso(
    id_disciplina   SERIAL NOT NULL,
    nome_disciplina VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_disciplina PRIMARY KEY (id_disciplina),
    CONSTRAINT un_nome_disciplina UNIQUE(nome_disciplina)
);
CREATE TABLE funcao(
    id_funcao   SERIAL NOT NULL,
    nome_funcao VARCHAR(255) DEFAULT '------' NOT NULL,
    CONSTRAINT pk_id_funcao PRIMARY KEY (id_funcao),
    CONSTRAINT un_nome_funcao UNIQUE(nome_funcao)
);
CREATE TABLE categoria(
    id_categoria    SERIAL NOT NULL,
    nome_categoria  VARCHAR(255) NOT NULL,
    CONSTRAINT pk_id_categoria PRIMARY KEY (id_categoria),
    CONSTRAINT un_nome_categoria UNIQUE(nome_categoria)
);
CREATE TABLE servidor(
    matricula_servidor  BIGINT NOT NULL,
    nome                VARCHAR(255) NOT NULL,
    link_fotos          VARCHAR(255) DEFAULT '------' NOT NULL,
    link_lattes         VARCHAR(255) DEFAULT '------' NOT NULL,
    telefones           TEXT DEFAULT '------' NOT NULL,
    id_campus           INTEGER NOT NULL,
    id_cargo            INTEGER NOT NULL,
    id_setor            INTEGER NOT NULL,
    id_disciplina       INTEGER NOT NULL,
    id_setor_suap       INTEGER NOT NULL,
    id_jornada          INTEGER NOT NULL,
    id_categoria        INTEGER NOT NULL,
    id_funcao           INTEGER NOT NULL,
    
    CONSTRAINT pk_matricula_servidor PRIMARY KEY (matricula_servidor),
  
    CONSTRAINT fk_servidor_id_funcao FOREIGN KEY (id_funcao)
                REFERENCES funcao (id_funcao),
    CONSTRAINT fk_servidor_id_disciplina FOREIGN KEY (id_disciplina)
                REFERENCES disciplina_ingresso (id_disciplina),
    CONSTRAINT fk_servidor_id_categoria FOREIGN KEY (id_categoria)
                REFERENCES categoria (id_categoria),
    CONSTRAINT fk_servidor_id_cargo FOREIGN KEY (id_cargo)
                REFERENCES cargo (id_cargo),
    CONSTRAINT fk_servidor_id_setor FOREIGN KEY (id_setor)
                REFERENCES setor_siape (id_setor),
    CONSTRAINT fk_servidor_id_jornada FOREIGN KEY (id_jornada)
                REFERENCES jornada_trabalho (id_jornada),
    CONSTRAINT fk_servidor_id_campus FOREIGN KEY(id_campus)
                REFERENCES campus (id_campus),
    CONSTRAINT fk_servidor_id_setor_suap FOREIGN KEY (id_setor_suap)
                REFERENCES setor_suap(id_setor_suap)
);