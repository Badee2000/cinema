from ninja import ModelSchema, Schema
from .models import Movie
from datetime import datetime


class ProtagonistSchema(Schema):
    in_movie_name: str
    real_name: str


class MovieSchema(ModelSchema):
    """
    Creating a schema for the movie model. 
    """
    class Meta:
        model = Movie
        fields = '__all__'


class MovieCreateSchema(Schema):
    """
    Defining a CreateSchema for movies.
    """
    name: str
    protagonists: list[ProtagonistSchema]
    poster: str
    trailer: str
    start_date: datetime
    ranking: int
