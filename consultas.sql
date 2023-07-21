CREATE VIEW servidores_campus AS
	SELECT  campus.nome_campus as sigla,
			categoria.nome_categoria as categoria,
			COUNT(servidor.matricula_servidor) AS qt_servidores
	  FROM	servidor
INNER JOIN	campus ON servidor.id_campus = campus.id_campus
INNER JOIN	categoria ON servidor.id_categoria = categoria.id_categoria
GROUP BY	campus.nome_campus,
			categoria.nome_categoria;
			
SELECT * FROM servidores_campus ORDER BY sigla;