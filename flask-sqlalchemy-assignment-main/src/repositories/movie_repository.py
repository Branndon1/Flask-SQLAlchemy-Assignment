class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
         return self.session.query(movie).all()
        
    def get_movie_by_id(self, movie_id):
       return self.session.query(Movie).filter(Movie.id == movie_id).first()

    def create_movie(self, title, director, rating):
        movie = Movie(title=title, director=director, rating=rating)
        self.session.add(movie)
        self.session.commit()
        return movie.id

    def search_movies(self, title):
      return self.session.query(Movie).filter(Movie.title.ilike(f'%{title}%')).all()

# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
