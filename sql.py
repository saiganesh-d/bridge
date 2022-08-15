WITH cities AS (
    SELECT
      c.continent,
      c.country,
      json = '[' + STRING_AGG(j.json, ',') + ']'
    FROM countries c
    CROSS APPLY (
        SELECT
          c.city
        FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
    ) j(json)
    GROUP BY
      c.continent,
      c.country
),
countries AS (
    SELECT
      c.continent,
      json = '{' + STRING_AGG('"' + STRING_ESCAPE(c.country, 'json') + '":' + c.json, ',') + '}'
    FROM cities c
    GROUP BY
      c.continent
)
SELECT
  '{' + STRING_AGG('"' + STRING_ESCAPE(c.continent, 'json') + '":' + c.json, ',') + '}'
FROM countries c;
