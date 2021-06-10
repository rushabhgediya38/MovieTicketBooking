# Generated by Django 3.2.4 on 2021-06-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0006_movie_m_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='M_latest',
            field=models.CharField(blank=True, choices=[('NOW', 'NOW'), ('COMING', 'COMING'), ('EXCLUSIVE', 'EXCLUSIVE')], max_length=256, null=True),
        ),
    ]