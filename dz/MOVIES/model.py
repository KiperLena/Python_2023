import pickle
import os.path


class Movie: #данные об одном фильме
    def __init__(self, title, genre, director, year_of_release, duration, studio, actor):
        self.title = title
        self.genre = genre
        self.director = director
        self.year_of_release = year_of_release
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f"{self.title} ({self.genre})"  #что будет видно при просмотре


class MovieModel:
    def __init__(self):
        self.db_name = "db.txt"
        self.movies = self.load_data() #переменная где будет храниться то что сохранется

    def add_movie(self, dict_movie):
        movie = Movie(*dict_movie.values()) # экземпляр класса Movie
        self.movies[movie.title] = movie


    def get_all_movies(self):
        return self.movies.values()  #возвращает значения словаря

    def get_single_movie(self, user_title):
        movie = self.movies[user_title]
        dict_movie = {
            "название": movie.title,
            "жанр": movie.genre,
            "режиссер": movie.director,
            "год выпуска": movie.year_of_release,
            "длительность": movie.duration,
            "студия": movie.studio,
            "актеры": movie.actor
        }
        return dict_movie


    def remove_movie(self, user_title):
        return self.movies.pop(user_title)

    def load_data(self):
        if os.path.exists(self.db_name):
            with open(self.db_name, 'rb') as f:
                return pickle.load(f)
        else:
            return dict()

    def save_data(self):
        with open(self.db_name, 'wb') as f:
            pickle.dump(self.movies, f)
