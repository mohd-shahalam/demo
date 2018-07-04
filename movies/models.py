from django.db import models

class Movie(models.Model):
    actor=models.CharField(max_length=30)
    actor_movie=models.CharField(max_length=20)
    genre=models.CharField(max_length=50)
    movie_logo=models.CharField(max_length=40)

class Song(models.Model):
    movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type=models.CharField(max_length=50)
    song_name=models.CharField(max_length=100)