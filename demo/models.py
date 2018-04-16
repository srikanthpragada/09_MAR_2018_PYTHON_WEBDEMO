from django.db import models

# Create your models here.

class Course:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def __str__(self):
        return "Course : %s, Fee = %d" % (self.name, self.fee)


class Movies:
     movies = {'Vizag' : ['Movie1','Movie2'],
               'Chennai' : ['Movie3','Movie4'],
               'Hyderabad' : ['Movie10', 'Movie11'],
               'Mumbai': ['Movie8', 'Movie9','Movie6']
               };

     @staticmethod
     def get_cities():
         return  Movies.movies.keys()

     @staticmethod
     def get_movies(city):
         return Movies.movies[city]  # list of movies in the given city




