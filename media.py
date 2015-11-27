"""
this module contains the movie class that needed to create
movie instance which in turn needed to create movie trailer website
"""
import webbrowser
class Movie():
	"""
    Constructor for Movie
    title:
        title of the movie in string
	storyline:
		plot of the movie in string
	poster_image_url:
		image url that shows the poster image of the movie
    trailer_youtube_url:
        trailer of the movie from youtube
    """
	def __init__(self, title, release_date, storyline, poster_image_url,
	 trailer_youtube_url):
		self.title = title
		self.release_date = release_date
		self.storyline = storyline
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	"""
	To show trailer in browser
	"""
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)