--  a script that lists all shows contained in the database
SELECT tv_shows.title,tv_show_genres.genre_id FROM tv_shows
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_generes.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
