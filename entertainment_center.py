import media
import fresh_tomatoes

troy = media.Movie("Troy", "Story of Achilles" , 
					"https://images-na.ssl-images-amazon.com/images/I/612Z1A--gWL._SY355_.jpg" , 
					"https://www.youtube.com/watch?v=znTLzRJimeY.com")

gone_in_60_seconds = media.Movie("Gone in 60 Seconds", "Movie about stealing cars" , 
								"http://strayhair.com/wp-content/uploads/2016/02/featured-gone-in-60.jpg" , 
								"https://www.youtube.com/watch?v=cxCE9gDm1vo")

thirteen_hours= media.Movie("13 Hours", "During an attack on a U.S. compound in Libya, a security team struggles to make sense out of the chaos.",
				"https://images-na.ssl-images-amazon.com/images/I/91zhWpXHVzL._SL1500_.jpg", 
				"https://www.youtube.com/watch?v=5MBjAN7jqsQ")

sicario= media.Movie("Sicario", "An idealistic FBI agent is enlisted by a government task force to aid in the escalating war against drugs at the border area between the U.S. and Mexico.",
		 "http://t3.gstatic.com/images?q=tbn:ANd9GcT4oUDoLOJuqZNW-rZGnc4TquZoOKcNmkwCgDzikSL6enj4XH7R",
		 "https://www.youtube.com/watch?v=sR0SDT2GeFg")

black_panther=media.Movie("Black Panther","T'Challa, after the death of his father, the King of Wakanda, returns home to the isolated, technologically advanced African nation to succeed to the throne and take his rightful place as king.",
				"http://t1.gstatic.com/images?q=tbn:ANd9GcS9XmH8C4x242GdYwyZtIOFOUqaZ5XMPSxY5zc2nVR_pbteQcSq",
				"https://www.youtube.com/watch?v=xjDjIWPwcPU")

mobsters = media.Movie("Mobsters", "From start to finish, it's a story of friendship between 4 street-wise males who don't mind using violence to achieve the lives that they want. They trust no one but each other which is vital to their success as mobsters.",
			"https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Mobsters_poster.jpg/220px-Mobsters_poster.jpg",
			"https://www.youtube.com/watch?v=uCrDhmD3khg")

boondocks = media.Shows("Boondocks", "Based on the comic strip, Huey and Riley move away from the city and out to the suburbs with their irascible grandfather. Biting socio-political commentary ensues.",
			  "https://www.watchcartoononline.io/thumbs/Boondocks-Season-3-Episode-5-English-Dubbed.jpg",
			  "https://www.youtube.com/watch?v=r6GRGEw7P9I")
dragon_ball_super = media.Shows("Dragon Ball Super", "The continuing adventures of the mighty warrior Son Goku, as he encounters new worlds and new warriors to fight.",
					  "http://img1.ak.crunchyroll.com/i/spire4/0caa4a6297700ea5ce63a45d9596d2bf1476994570_full.jpg",
					  "https://www.youtube.com/watch?v=giKGGDfT0DQ")
game_of_thrones = media.Shows("Game of Thrones", "Nine noble families fight for control over the mythical lands of Westeros, while a forgotten race returns after being dormant for thousands of years.",
					"http://ll-c.ooyala.com/e1/11cnduYjE6BQ5jWju1l4_-cAa5rebe7x/promo322954306",
					"https://www.youtube.com/watch?v=-5xdTlgaaaw")
the_wire = media.Shows("The Wire","Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.",
			"https://upload.wikimedia.org/wikipedia/en/2/2d/The_Wire_-_Season_1.jpg",
			"https://www.youtube.com/watch?v=uDcQbk78CSw")
power = media.Shows("Power","James Ghost St. Patrick, a wealthy New York night club owner who has it all, catering for the city's elite and dreaming big, lives a double life as a drug kingpin.",
		 "https://images-na.ssl-images-amazon.com/images/M/MV5BOTA4NTkzMjUzOF5BMl5BanBnXkFtZTgwNzg5ODkxOTE@._V1_SX170_CR0,0,170,250_AL_.jpg",
		 "https://www.youtube.com/watch?v=0bbwp6feNwM")
narcos = media.Shows("Narcos", "chronicles the rise of the cocaine trade in Colombia and the gripping real-life stories of drug kingpins of the late '80s in this raw, gritty original series.",
			"http://theurbantwist.com/wp-content/uploads/2016/09/narcos-cover.jpg",
			"https://www.youtube.com/watch?v=U7elNhHwgBU")


movies = [troy, gone_in_60_seconds, sicario, thirteen_hours, black_panther, mobsters]
shows = [boondocks,dragon_ball_super,game_of_thrones,the_wire,power,narcos] 
fresh_tomatoes.open_movies_page(movies, shows)

