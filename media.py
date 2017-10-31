import webbrowser


class Movie():
        """Movie() Class create an instance of a movie object and fills its values"""
        VALID_RATINGS = ["G", "PG", "PG-13", "R"]

        def __init__(self, movie_title, movie_storyline,
                     poster_image, trailer_youtube_url):
            """Function contructs the object with values passed through"""
            self.title = movie_title
            self.storyline = movie_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube_url

        def show_trailer(self):
            """Function opens up the trailer of the movie in a browser"""
            webbrowser.open(self.trailer)


class Shows():
        """Shows() Class create an instance of a movie object and fills its values"""
        def __init__(self, show_title, show_storyline,
                     poster_image, trailer_youtube_url):
            """Function contructs the object with values passed through"""
            self.title = show_title
            self.storyline = show_storyline
            self.poster_image_url = poster_image
            self.trailer_youtube_url = trailer_youtube_url

        def show_trailer(self):
            """Function opens up the trailer of the tv show in a browser"""
            webbrowser.open(self.trailer)
