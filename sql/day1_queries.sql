SELECT COUNT(*) FROM benchmark_indices;

SELECT * FROM benchmark_indices
LIMIT 5;

SELECT
    index_name,
    AVG(close_value) AS average_close
FROM benchmark_indices
GROUP BY index_name;