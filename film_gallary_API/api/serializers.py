from rest_framework import serializers

from films.models import Genre, Film, Person, WatchedFilms, PlanFilms


class GenreSerializer(serializers.ModelSerializer):
    """Сериализатор для Жанров."""

    # name = serializers.CharField(source='genre')

    class Meta:
        model = Genre
        fields = ('name', )


class PersonSerializer(serializers.ModelSerializer):
    """Сериализатор для Персон."""

    class Meta:
        model = Person
        fields = ('name', )


class FilmSerializer(serializers.ModelSerializer):
    """Сериализатор для Фильмов."""

    type = serializers.StringRelatedField(read_only=True)
    country = serializers.StringRelatedField(read_only=True)
    genre = GenreSerializer(read_only=True, many=True)
    person = PersonSerializer(read_only=True, many=True)

    class Meta:
        model = Film
        fields = (
            'id',
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
    """Сериализатор для списка просмотренных фильмов.
    Используется для чтения.
    """

    film = FilmSerializer(read_only=True)

    class Meta:
        model = WatchedFilms
        fields = ('user', 'film', 'user_rating')


class WatchedFilmAddSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления просмотренного фильма."""

    class Meta:
        model = WatchedFilms
        fields = ('film', 'user_rating')


class PlanFilmListSerializer(serializers.ModelSerializer):
    """Сериализатор для списка планируемых фильмов.
    Используется для чтения.
    """

    film = FilmSerializer(read_only=True)

    class Meta:
        model = PlanFilms
        fields = ('user', 'film')


class PlanFilmAddSerializer(serializers.ModelSerializer):
    """Сериализатор для добавления планируемого фильма."""

    class Meta:
        model = PlanFilms
        fields = ('film', )
