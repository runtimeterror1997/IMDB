# Generated by Django 4.0.3 on 2023-01-12 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0008_watchlist_avg_rating_watchlist_total_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='genre',
        ),
        migrations.DeleteModel(
            name='MovieGenre',
        ),
    ]
