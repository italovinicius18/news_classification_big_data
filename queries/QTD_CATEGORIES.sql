select
    split_part(url, '/', 4) as category,
    COUNT(*) AS quantidade
FROM
    news
where text != ''
GROUP BY
    category