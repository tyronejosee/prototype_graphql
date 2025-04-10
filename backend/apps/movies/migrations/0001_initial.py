# Generated by Django 5.1.5 on 2025-01-28 18:06

import django.core.validators
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('casts', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1888), django.core.validators.MaxValueValidator(2025)])),
                ('description', models.TextField()),
                ('trailer_url', models.URLField(blank=True, null=True)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='movies/')),
                ('is_featured', models.BooleanField(default=False)),
                ('country_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.country')),
                ('director_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='casts.director')),
                ('genre_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.genre')),
                ('language_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categories.language')),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ['-year'],
            },
        ),
    ]
