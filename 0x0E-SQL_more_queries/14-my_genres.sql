-- List all genres of the show, Dexter
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres
INNER JOIN tv_shows
ON tv_genres.id=tv_show_genres.genre_id
WHERE tv_genres.id = tv_show_genres.genre_id AND tv_shows.title="Dexter" AND tv_show_genres.show_id=tv_shows.id
GROUP BY tv_genres.name;