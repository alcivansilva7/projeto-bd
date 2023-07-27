CREATE VIEW servidores_campus AS
	SELECT  campus.nome_campus as sigla,
			categoria.nome_categoria as categoria,
	 COUNT	(servidor.matricula_servidor) AS qt_servidores
	  FROM	servidor
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
INNER JOIN	categoria ON servidor.id_categoria = categoria.id_categoria
GROUP BY	campus.nome_campus,
			categoria.nome_categoria;
			
SELECT * FROM servidores_campus ORDER BY sigla;



CREATE VIEW docentes_disciplinas AS	
	SELECT	servidor.nome,
			disciplina_ingresso.nome_disciplina AS disciplina
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN	categoria ON categoria.id_categoria = servidor.id_categoria
	 WHERE 	categoria.nome_categoria = 'docente'
  ORDER BY	disciplina_ingresso.nome_disciplina;
  
SELECT * FROM docentes_disciplinas;


CREATE VIEW disciplinas_campus AS	
	SELECT	disciplina_ingresso.nome_disciplina AS disciplina,
			campus.nome_campus as sigla,
	 COUNT	(servidor.matricula_servidor) AS qt_disciplinas
  	  FROM	servidor
INNER JOIN  disciplina_ingresso ON servidor.id_disciplina = disciplina_ingresso.id_disciplina
INNER JOIN	categoria ON categoria.id_categoria = servidor.id_categoria
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
	 WHERE 	categoria.nome_categoria = 'docente'
  GROUP BY	disciplina_ingresso.nome_disciplina,
  			campus.nome_campus;
  
SELECT * FROM disciplinas_campus ORDER BY sigla;