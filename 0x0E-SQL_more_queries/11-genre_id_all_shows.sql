-- Script that lists all tv shows genres
SELECT tv_shows.title, tv_show_genres.genre_id -- Query to join tv shows
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
