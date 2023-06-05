CREATE TABLE news_grouped AS
SELECT
    *, CASE
        WHEN category = 'economia' THEN 'Economia'
        WHEN category = 'politica' THEN 'Politica'
        WHEN category = 'internacional' THEN 'Internacional'
        WHEN category = 'mundo' THEN 'Mundo'
        WHEN category IN ('saude', 'bemestar', 'ciencia-e-saude') THEN 'Saude'
        WHEN category = 'nacional' THEN 'Nacional'
        WHEN category IN ('pop-arte', 'carnaval', 'turismo-e-viagem', 'estilo') THEN 'Entretenimento'
        WHEN category IN ('ciencia', 'tecnologia', 'inovacao') THEN 'Ciencia'
        WHEN category = 'educacao' THEN 'Educacao'
        WHEN category = 'esportes' THEN 'Esportes'
        WHEN category IN ('natureza', 'meio-ambiente') THEN 'Natureza'
        WHEN category IN ('sp', 'pe', 'pb', 'mg', 'rj', 'ro', 'df', 'ba', 'es', 'pr', 'pi', 'rs', 'al', 'ce', 'ap', 'sc', 'ac', 'se', 'am', 'pa', 'go', 'sao-paulo', 'pernambuco', 'rn', 'ma', 'mato-grosso', 'distrito-federal') THEN 'Regional'
    END AS grouped_category
FROM
    news_raw
WHERE
    category IN ('economia', 'politica', 'internacional', 'mundo', 'saude', 'bemestar', 'ciencia-e-saude', 'nacional', 'pop-arte', 'carnaval', 'turismo-e-viagem', 'estilo', 'tecnologia', 'ciencia', 'inovacao', 'educacao', 'esportes', 'natureza', 'meio-ambiente', 'sp', 'pe', 'pb', 'mg', 'rj', 'ro', 'df', 'ba', 'es', 'pr', 'pi', 'rs', 'al', 'ce', 'ap', 'sc', 'ac', 'se', 'am', 'pa', 'go', 'sao-paulo', 'pernambuco', 'rn', 'ma', 'mato-grosso', 'distrito-federal')
