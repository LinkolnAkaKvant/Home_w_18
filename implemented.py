from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.movie import MovieDAO

from service.movie import MovieService
from service.genre import GenreService
from service.director import DirectorService

from setup_db import db

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=director_dao.session)
movie_dao = MovieDAO(sission=db.session)

director_service = DirectorService(dao=director_dao)
genre_service = GenreService(dao=genre_dao)
movie_service = MovieService(dao=movie_dao)
