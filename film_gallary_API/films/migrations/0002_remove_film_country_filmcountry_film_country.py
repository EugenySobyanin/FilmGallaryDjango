# Generated by Django 4.2.16 on 2024-09-22 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='country',
        ),
        migrations.CreateModel(
            name='FilmCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.country')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='country',
            field=models.ManyToManyField(through='films.FilmCountry', to='films.country'),
        ),
    ]
