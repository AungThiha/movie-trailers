"""
list of movies that pass a function named 'open_movies_page' in fresh_tomatoes module to create a html page
"""

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story III",
						"June 15, 2010",
 						"The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
 						"https://www.movieposter.com/posters/archive/main/98/MPW-49351",
 						"https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
					"December 10, 2009",
					"A paraplegic marine dispatched to the moon Pandora on a unique mission becomes torn between following his orders and protecting the world he feels is his home.",
					"http://www.impawards.com/2009/posters/avatar.jpg",
					"https://www.youtube.com/watch?v=5PSNL1qE6VY")

the_martian = media.Movie("The Martian",
						"September 24, 2015",
						"During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.",
						"http://cdn.traileraddict.com/content/20th-century-fox/martian2015.jpg",
						"https://www.youtube.com/watch?v=Ue4PCI0NamI")

superman = media.Movie("Superman",
						"December 15, 1978",
						"An alien orphan is sent from his dying planet to Earth, where he grows up to become his adoptive home's first and greatest superhero.",
						"http://img04.deviantart.net/8b6c/i/2015/119/5/c/superman_1978_film_poster_by_photorevival-d3l7adc.jpg",
						"https://www.youtube.com/watch?v=q-v1RyLNWU8")

spiderman_II = media.Movie("Spider-man II",
							"June 25, 2004",
							"Peter Parker is beset with troubles in his failing personal life as he battles a brilliant scientist named Doctor Otto Octavius",
							"http://vignette3.wikia.nocookie.net/spiderman-films/images/0/02/Spider-Man_2_Poster.jpg/revision/latest?cb=20121105001752",
							"https://www.youtube.com/watch?v=enmFqm_N_ZE")

spiderman_III = media.Movie("Spider-man III",
							"April 16, 2007",
							"A strange black entity from another world bonds with Peter Parker and causes inner turmoil as he contends with new villains, temptations, and revenge.",
							"http://vignette2.wikia.nocookie.net/marvelmovies/images/3/31/Spider-man_3_poster.jpg/revision/latest?cb=20080402014330",
							"https://www.youtube.com/watch?v=MTIP-Ih_GR0")

movies = [ toy_story, avatar, the_martian, superman, spiderman_II, spiderman_III]

# pass movies list to open_movies_page in fresh_tamatoes module to create html page
fresh_tomatoes.open_movies_page(movies)