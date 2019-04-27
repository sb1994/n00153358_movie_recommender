# Generated by Django 2.1.2 on 2019-02-28 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('backdrop_path', models.CharField(max_length=120)),
                ('budget', models.CharField(max_length=120)),
                ('tmdb_id', models.CharField(max_length=120)),
                ('orginal_title', models.TextField()),
                ('overview', models.TextField()),
                ('poster_path', models.TextField()),
                ('popularity', models.TextField()),
                ('status', models.TextField()),
                ('release_date', models.TextField()),
                ('runtime', models.TextField()),
                ('tagline', models.TextField()),
                ('title', models.TextField()),
                ('video', models.TextField()),
                ('vote_average', models.TextField()),
                ('vote_count', models.TextField()),
            ],
        ),
    ]