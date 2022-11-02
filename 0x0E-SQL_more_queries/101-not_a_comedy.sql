-- List shows without genre Comedy
SELECT title FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id=tv_shows.id
WHERE tv_show_genres.genre_id NOT IN (
      SELECT tv_genres.id FROM tv_genres
      WHERE name="comedy")
GROUP BY title
ORDER BY title
;