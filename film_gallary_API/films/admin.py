from django.contrib import admin

from .models import Country, Genre, Type, Person, Film, WatchedFilms, PlanFilms, FilmGenre, FilmPerson


admin.site.register(Country)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Person)
admin.site.register(Film)
admin.site.register(WatchedFilms)
admin.site.register(PlanFilms)
admin.site.register(FilmGenre)
admin.site.register(FilmPerson)