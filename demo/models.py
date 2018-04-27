# Create your models here.

from django.db import models


# DBCourse class
class DBCourse(models.Model):
    title = models.CharField(max_length=20)
    duration = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.title


class DBStudent(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    course = models.ForeignKey('DBCourse', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Course:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def __str__(self):
        return "Course : %s, Fee = %d" % (self.name, self.fee)


class Movies:
    movies = {'Vizag': ['Movie1', 'Movie2'],
              'Chennai': ['Movie3', 'Movie4'],
              'Hyderabad': ['Movie10', 'Movie11'],
              'Mumbai': ['Movie8', 'Movie9', 'Movie6']
              };

    @staticmethod
    def get_cities():
        return Movies.movies.keys()

    @staticmethod
    def get_movies(city):
        return Movies.movies[city]  # list of movies in the given city
