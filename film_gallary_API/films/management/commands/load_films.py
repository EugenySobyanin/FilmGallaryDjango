import requests
from django.core.management.base import BaseCommand
from django.db import transaction
from films.models import Film, Type, Country, Genre


class Command(BaseCommand):
    help = 'Load films from Kinopoisk API into the database'

    API_URL = 'https://api.kinopoisk.dev/v1.4/movie'
    HEADERS = {
        'accept': 'application/json',
        'X-API-KEY': 'QM90F9Y-V2P4X0N-PKP66KR-YX4339W'
    }

    def handle(self, *args, **options):
        page = 1
        while True:
            response = requests.get(self.API_URL, headers=self.HEADERS, params={
                'page': page,
                'limit': 250,
                'selectFields': [
                    'id', 'name', 'alternativeName', 'description', 'shortDescription',
                    'type', 'isSeries', 'year', 'rating', 'movieLength',
                    'genres', 'countries', 'poster', 'logo', 'videos'
                ],
                'sortField': 'id',
                'sortType': '1'
            })

            if response.status_code != 200:
                self.stdout.write(self.style.ERROR(f'Error fetching data: {response.status_code}'))
                break

            data = response.json()
            docs = data.get('docs', [])

            if not docs:
                self.stdout.write(self.style.WARNING('No more films found.'))
                break

            for doc in docs:
                try:
                    with transaction.atomic():  # Начало транзакции
                        title = doc['name'] if doc.get('name') else doc.get('alternativeName')
                        film, created = Film.objects.get_or_create(
                            kinopoisk_dev_id=doc['id'],
                            defaults={
                                'title': title,
                                'alternative_title': doc.get('alternativeName'),
                                'description': doc['description'],
                                'short_description': doc.get('shortDescription'),
                                'release_year': doc.get('year'),
                                'movie_length': doc.get('movieLength'),
                                'poster': doc['poster']['url'] if doc.get('poster') else None,
                                'logo': doc['logo']['url'] if doc.get('logo') else None,
                                'is_series': doc['isSeries'],
                            }
                        )

                        # Сохранение типов
                        if doc.get('type'):
                            film.type, _ = Type.objects.get_or_create(name=doc['type'])

                        # Сохранение стран
                        for country_data in doc.get('countries', []):
                            country, _ = Country.objects.get_or_create(name=country_data['name'])
                            film.country.add(country)

                        # Сохранение жанров
                        for genre_data in doc.get('genres', []):
                            genre, _ = Genre.objects.get_or_create(name=genre_data['name'])
                            film.genre.add(genre)

                        # Сохранение рейтингов
                        film.rating_kp = doc['rating']['kp']
                        film.rating_imdb = doc['rating']['imdb']
                        film.save()

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f'Error processing film {doc.get("name", "unknown")}: {e}'))
                    # Ошибка внутри блока transaction.atomic вызовет откат

            self.stdout.write(self.style.SUCCESS(f'Successfully loaded page {page} of films.'))
            page += 1