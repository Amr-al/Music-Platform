# Generated by Django 4.1.2 on 2022-11-10 19:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artists', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New Album', max_length=50)),
                ('creation_datetime', models.DateTimeField(auto_now_add=True)),
                ('release_datetime', models.DateTimeField()),
                ('cost', models.FloatField()),
                ('approved', models.BooleanField(default=False)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='artists.artist')),
            ],
            options={
                'db_table': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('audio', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])),
                ('song_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='albums.album')),
            ],
        ),
        migrations.AddConstraint(
            model_name='album',
            constraint=models.CheckConstraint(check=models.Q(('name__regex', '[1-9]'), _negated=True), name='name must not contain any special characters or numbers'),
        ),
    ]