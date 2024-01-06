-- Sql file
-- See all values grouped by their score and in descending order
SELECT
  score,
  count(score) AS number
FROM
  second_table
GROUP BY
  score
ORDER BY
  number DESC;
