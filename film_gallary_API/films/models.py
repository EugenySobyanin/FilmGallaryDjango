from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Country(models.Model):
    name = models.CharField('Страна', max_length=255)

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField('Тип', max_length=100)

    def __str__(self) -> str:
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=100)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    name = models.CharField('Имя', max_length=255)

    def __str__(self) -> str:
        return self.name


class Film(models.Model):
    kinopoisk_dev_id = models.PositiveIntegerField(
        'ID от KinopoiskAPI',
        blank=True,
        null=True
    )
    title = models.CharField('Название', max_length=255, null=True, default=None)
    alternative_title = models.CharField('Альтернативное название', max_length=255, null=True, default=None)
    description = models.TextField('Описание', blank=True, null=True, default=None)
    short_description = models.TextField('Краткое описание', blank=True, null=True, default=None)
    rating_kp = models.DecimalField(
        'Рейтинг кинопоиска',
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True
    )
    rating_imdb = models.DecimalField(
        'Рейтинг критиков',
        max_digits=2,
        decimal_places=1,
        blank=True,
        null=True
    )
    release_year = models.IntegerField('Год выпуска', blank=True, null=True)
    movie_length = models.SmallIntegerField('Длительность', blank=True, null=True)
    poster = models.URLField('Ссылка на постер', max_length=500, null=True, default=None)
    logo = models.URLField('Ссылка на лого', max_length=500, null=True, default=None)
    is_series = models.BooleanField('Сериал', default=False)
    type = models.ForeignKey(
        Type,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Тип'
    )
    country = models.ManyToManyField(Country, through='FilmCountry')
    genre = models.ManyToManyField(Genre, through='FilmGenre')
    person = models.ManyToManyField(Person, through='FilmPerson')

    def __str__(self) -> str:
        return self.title


class FilmCountry(models.Model):
    """Промежуточная таблица для связи 'Многие ко многим' для фильмов и стран."""

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )


class FilmGenre(models.Model):
    """Промежуточная таблица для связи 'Многие ко многим' для фильмов и жанров."""

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.film} - {self.genre}'


class FilmPerson(models.Model):
    """Промежуточная таблица для связи 'Многие ко многим' для фильмов и персон."""

    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'{self.film} - {self.person}'


class WatchedFilms(models.Model):
    """Промежуточная таблица для свзяи ''Многие ко многим'
    для хранения данных о просмотренных пользователем фильмов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )
    user_rating = models.DecimalField(
        'Оценка пользователя',
        max_digits=2,
        decimal_places=1
    )

    def __str__(self) -> str:
        return f'{self.user} - {self.film}'


class PlanFilms(models.Model):
    """Промежуточная таблица для свзяи ''Многие ко многим'
    для хранения данных о просмотренных пользователем фильмов."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    film = models.ForeignKey(
        Film,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f'P{self.user} - {self.film}'
