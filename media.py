import webbrowser
class Movie():
    VALID_RATINGS = ["G","PG", "PG-13", "R"]
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer)
    
class Shows():
    
    
    def __init__(self, show_title, show_storyline, poster_image, trailer_youtube_url):
        self.title = show_title
        self.storyline = show_storyline
        self.poster_image_url = poster_image 
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer)