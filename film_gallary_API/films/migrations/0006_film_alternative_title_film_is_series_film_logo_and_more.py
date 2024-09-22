# Generated by Django 4.2.16 on 2024-09-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_film_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='alternative_title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Альтернативное название'),
        ),
        migrations.AddField(
            model_name='film',
            name='is_series',
            field=models.BooleanField(default=False, verbose_name='Сериал'),
        ),
        migrations.AddField(
            model_name='film',
            name='logo',
            field=models.URLField(default=None, max_length=500, null=True, verbose_name='Ссылка на лого'),
        ),
        migrations.AddField(
            model_name='film',
            name='short_description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating_imdb',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Рейтинг критиков'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating_kp',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='Рейтинг кинопоиска'),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Год выпуска'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(default=None, max_length=255, null=True, verbose_name='Название'),
        ),
    ]
