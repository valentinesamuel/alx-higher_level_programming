-- List number of records with same score in table, second_table, in database hbtn_0c_0
SELECT score, COUNT(score) AS number FROM second_table AS C
GROUP BY score
ORDER BY score DESC;