# Generated by Django 3.2.4 on 2021-06-13 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0021_alter_m_multiplex_name_m_screen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='M_lang',
        ),
        migrations.AddField(
            model_name='m_multiplex_name',
            name='M_lang',
            field=models.ManyToManyField(blank=True, null=True, to='MovieApp.M_lang'),
        ),
    ]
