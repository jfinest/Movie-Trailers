import fresh_tomatoes import media1

#Creating instances of favorite movies

wanted = media1.Movie("Wanted",
"https://www.movieposter.com/posters/archive/main/94/MPW-47474",
"https://www.youtube.com/watch?v=edpEspHOeVU")

conjouring = media1.Movie("Conjouring",
"http://cdn.collider.com/wp-content/uploads/the-conjuring-uk-poster.jpg",
"https://www.youtube.com/watch?v=Vjk2So3KvSQ")

replacement = media1.Movie("The Replacement",
"http://i.imgur.com/hx5YAyn.jpg", "https://youtube.com/watch?v=MJVxQhCJG_8")

interstellar = media1.Movie("Interstellar",
"https://littleredreviewer.files.wordpress.com/2014/11/interstellar-movie-
poster.jpg", "https://www.youtube.com/watch?v=Rt2LHkSwdPQ")

miles = media1.Movie(" 8 Miles ",
"https://upload.wikimedia.org/wikipedia/en/8/8b/Eight_mile_ver2.jpg",
"https://www.youtube.com/watch?v=axGVrfwm9L4")

# Variable holding list of favorite movies into movi = [wanted, conjouring,
replacement, interstellar, miles]

#invoiking open.movies.page function from fresh_tomatoes with list of movies
fresh_tomatoes.open_movies_page(movi)


