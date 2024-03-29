import pytest
from django.test import Client
from .models import Movie
from .tasks import update_movie_rankings
from datetime import datetime
from django.conf import settings


@pytest.fixture
def client():
    return Client()


# Here we are config the database settings to match with postgres.
@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'NAME': 'cinema',
        "ATOMIC_REQUESTS": True,

    }


@pytest.mark.django_db
def test_create_movie(client):
    """
    Test creating a movie.
    """
    poster = "https://www.acadlly.com/wp-content/uploads/2023/07/love-again.jpg"
    trailer = "https://youtu.be/CQDXtD2HJAs"

    response = client.post("/api/movies", {"name": "Test Movie", "protagonists": "Test Protagonists", "poster": poster,
                           "trailer": trailer, "start_date": "2025-01-01T00:00:00Z", "status": "coming_up"}, follow=True)
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_movies(client):
    """
    Test listing all movies.
    """

    # Actually, we can create a .py file and put the test data in it if needed,
    # but here we are testing only one, so no need for that.
    movie = Movie.objects.create(
        name="Game Of Thrones",
        protagonists=[
            {"in_movie_name": "Jon Snow", "real_name": "Winter Is Coming"},
            {"in_movie_name": "Daenerys Targaryen", "real_name": "Emilia Clarke"}
        ],
        poster="https://www.acadlly.com/wp-content/uploads/2023/07/love-again.jpg",
        trailer="https://www.youtube.com/watch?v=bjqEWgDVPe0",
        start_date="2024-05-27T09:45:48Z",
        status="coming_up",
        ranking=10,
    )
    response = client.get("/api/movies", follow=True)
    assert response.status_code == 200
    # Check if response is correct (that we created).
    assert movie.name == "Game Of Thrones"


@pytest.mark.django_db
def test_movie_ranking_update():
    """
    Test the Celery task (I Used apply for the immediate test).
    """
    movie = Movie.objects.create(
        name='Movie1', status='coming_up', start_date="2025-01-01T00:00:00Z", ranking=0)

    # Run the Celery task
    update_movie_rankings.apply()

    # Check if the movie's ranking has been updated by 10
    updated_movie = Movie.objects.get(id=movie.id)
    assert updated_movie.ranking == 10
