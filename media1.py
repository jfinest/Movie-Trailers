import webbrowser


class Movie():
	""" This class will be used to create a list of movies which will
	show title, a movie poster and a trailer in the browser to the user. """

	def __init__(self, movie_title, poster_image, trailer_youtube):
		""" This is a constructor that takes 3 parameter. The movie title,
		movie poster image url and movie youtube trailer url. """
		self.title = movie_title
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
