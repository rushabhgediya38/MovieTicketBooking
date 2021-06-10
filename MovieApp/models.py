from django.db import models


MovieTypes = [
    ('Action', 'Action'),
    ('Comedy', 'Comedy'),
    ('Drama', 'Drama'),
    ('Fantasy', 'Fantasy'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Romance', 'Romance'),
    ('Thriller', 'Thriller'),
]

# MovieScreen = [
#     ('2D', '2D'),
#     ('3D', '3D'),
#     ('4DX', '4DX'),
# ]


class M_Screen(models.Model):
    m_screen = models.CharField(max_length=256)

    def __str__(self):
        return str(self.m_screen)


class M_Cast(models.Model):
    ca_img = models.ImageField(upload_to='movie-cast')
    ca_name = models.CharField(max_length=256)
    ca_actor = models.CharField(max_length=256, default='Actor')

    def __str__(self):
        return self.ca_name


class M_Crew(models.Model):
    cr_img = models.ImageField(upload_to='movie-crew')
    cr_name = models.CharField(max_length=256)
    cr_actor = models.CharField(max_length=256)

    def __str__(self):
        return self.cr_name


class Movie(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='movie-images')
    M_date = models.DateTimeField()
    M_hour = models.IntegerField()
    M_min = models.IntegerField()
    M_desc = models.TextField(max_length=5000)
    M_screen = models.ManyToManyField(to=M_Screen)
    M_cast = models.ManyToManyField(to=M_Cast)
    M_crew = models.ManyToManyField(to=M_Crew)

    def __str__(self):
        return self.name

