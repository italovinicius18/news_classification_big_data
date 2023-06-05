CREATE TABLE news_raw AS
SELECT ROW_NUMBER() OVER (ORDER BY url) AS idx, *, split_part(url, '/', 4) as category
FROM news
WHERE text != '';