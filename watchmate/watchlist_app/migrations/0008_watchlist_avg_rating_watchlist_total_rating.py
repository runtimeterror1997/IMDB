# Generated by Django 4.0.3 on 2023-01-11 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist_app', '0007_review_review_user_alter_review_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='watchlist',
            name='avg_rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='watchlist',
            name='total_rating',
            field=models.IntegerField(default=0),
        ),
    ]
