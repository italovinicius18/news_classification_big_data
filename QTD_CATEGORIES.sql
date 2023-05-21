select
	MAX(url),
    split_part(url, '/', 4) as categoria,
    COUNT(*) AS quantidade
FROM
    news
GROUP BY
    categoria;