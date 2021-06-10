# Generated by Django 3.2.4 on 2021-06-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0003_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='M_lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='M_lang',
            field=models.ManyToManyField(to='MovieApp.M_lang'),
        ),
    ]