
# 3) The ranking of each movie, from creation (status="coming_up")
# to launch (status="running"),
# should be increased by 10 every 5 minutes.

from celery import shared_task
from .models import Movie


@shared_task
def update_movie_rankings():
    """
    Updating ranking for all movies that have "coming_up" status.
    """
    movies = Movie.objects.filter(status="coming_up")
    for movie in movies:
        movie.ranking += 10
        movie.save()
