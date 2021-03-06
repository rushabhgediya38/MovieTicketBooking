# Generated by Django 3.2.4 on 2021-06-12 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieApp', '0010_alter_m_state_st_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='m_city',
            options={'ordering': ('ci_name',)},
        ),
        migrations.AlterModelOptions(
            name='m_state',
            options={'ordering': ('st_slug',)},
        ),
        migrations.CreateModel(
            name='M_multiplex_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multiplex_name', models.CharField(max_length=256)),
                ('multiplex_location', models.CharField(max_length=256)),
                ('m_city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MovieApp.m_city')),
            ],
            options={
                'ordering': ('multiplex_name',),
            },
        ),
    ]
