from ninja import NinjaAPI, Body
from ninja.responses import Response
from urllib.parse import urlparse
from ninja.errors import ValidationError
from .models import Movie
from .schemas import MovieSchema, MovieCreateSchema

app = NinjaAPI()


@app.get('movies/', response=list[MovieSchema])
def get_movies(request):
    """
    Get all movies ordered by ranking.
    """
    try:
        return Movie.objects.order_by('-ranking')
    except ValidationError as e:
        return {'error': str(e)}


@app.post("movies/", response={201: list[MovieSchema]})
def create_movies(request, movies: list[MovieCreateSchema]):
    """
    Create multiple movies in one request (BULK).
    """

    created_movies = []
    errors = []

    for movie_data in movies:
        try:
            # Perform validation logic
            parsed_poster_url = urlparse(movie_data.poster)
            if not parsed_poster_url.path.lower().endswith(('.jpg', '.png', '.jpeg')):
                raise ValidationError({'poster': 'Invalid image format.'})

            parsed_trailer_url = urlparse(movie_data.trailer)
            if not (
                parsed_trailer_url.path.lower().endswith(
                    ('.mp4', '.webm', '.ogg', '.avi', '.mkv', '.flv')
                )
                or parsed_trailer_url.geturl().lower().startswith('https://youtu.be/')
                or parsed_trailer_url.geturl().lower().startswith('https://www.youtube.com/watch?v=')
            ):
                raise ValidationError({'trailer': 'Invalid video format.'})

            movie_model = Movie.objects.create(**movie_data.dict())
            created_movies.append(movie_model)
        except ValidationError as e:
            errors.append({'movie_data': movie_data.dict(), 'error': str(e)})

    if errors:
        # Here we response with the errors from bad input data.
        return Response(status=400, data=errors)

    return created_movies
