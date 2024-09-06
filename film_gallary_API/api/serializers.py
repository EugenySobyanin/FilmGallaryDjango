from rest_framework import serializers

from films.models import Genre, Film, Person, WatchedFilms, PlanFilms


class GenreSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source='genre')

    class Meta:
        model = Genre
        fields = ('name', )


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = ('name', )


class FilmSerializer(serializers.ModelSerializer):
    type = serializers.StringRelatedField(read_only=True)
    country = serializers.StringRelatedField(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    person = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Film
        fields = (
            'title',
            'rating_kp',
            'rating_imdb',
            'release_year',
            'type',
            'country',
            'genre',
            'person',
        )


class WatchedFilmListSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)

    class Meta:
        model = WatchedFilms
        fields = ('film', 'user_rating')
        
        
class WatchedFilmAddSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = WatchedFilms
        fields = ('film', 'user_rating')


class PlanFilmSerializer(serializers.ModelSerializer):
    film = FilmSerializer(read_only=True)
    
    class Meta:
        model = PlanFilms
        fields = ('film')