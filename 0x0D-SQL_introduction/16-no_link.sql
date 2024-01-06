-- Sql file
-- Just read the sql by now
SELECT
  score,
  name
FROM
  second_table
WHERE
  name IS NOT NULL
ORDER BY
  score DESC;
