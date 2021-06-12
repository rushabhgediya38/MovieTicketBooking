from django.db import models
from django.db.models import F


class M_state(models.Model):
    st_name = models.CharField(max_length=256)
    st_slug = models.SlugField(max_length=256, blank=True, null=True)

    def __str__(self):
        return self.st_slug

    class Meta:
        ordering = ('st_slug',)


class M_city(models.Model):
    m_state = models.ForeignKey(M_state, on_delete=models.CASCADE)
    ci_name = models.CharField(max_length=256)

    def __str__(self):
        return self.ci_name

    class Meta:
        ordering = ('ci_name',)


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

Movie_latest = [
    ('NOW', 'NOW'),
    ('COMING', 'COMING'),
    ('EXCLUSIVE', 'EXCLUSIVE'),
]


class M_Cast(models.Model):
    ca_img = models.ImageField(upload_to='movie-cast')
    ca_name = models.CharField(max_length=256)
    ca_as = models.CharField(max_length=256, blank=True, null=True)
    ca_actor = models.CharField(max_length=256, default='Actor')

    def __str__(self):
        return self.ca_name


class M_lang(models.Model):
    language = models.CharField(max_length=256)

    def __str__(self):
        return self.language


class M_Crew(models.Model):
    cr_img = models.ImageField(upload_to='movie-crew')
    cr_name = models.CharField(max_length=256)
    cr_actor = models.CharField(max_length=256)

    def __str__(self):
        return self.cr_name


class Movie(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField(upload_to='movie-images')
    M_latest = models.CharField(choices=Movie_latest, max_length=256, blank=True, null=True)
    M_type = models.CharField(choices=MovieTypes, max_length=256, blank=True, null=True)
    M_date = models.DateTimeField()
    M_hour = models.IntegerField()
    M_min = models.IntegerField()
    M_desc = models.TextField(max_length=5000)
    M_lang = models.ManyToManyField(to=M_lang)

    M_cast = models.ManyToManyField(to=M_Cast)
    M_crew = models.ManyToManyField(to=M_Crew)

    def __str__(self):
        return self.name


class Images(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_images')
    m_image = models.ImageField(upload_to='multiple-movie-images', null=True, blank=True)

    def get_image(self):
        if self.m_image:
            return self.image_url
        return '#'


class M_time(models.Model):
    m_time = models.CharField(max_length=10)

    def __str__(self):
        return str(self.m_time)


class M_Screen(models.Model):
    m_screen = models.CharField(max_length=256)

    def __str__(self):
        return str(self.m_screen)


class M_multiplex_name(models.Model):
    m_city_name = models.ForeignKey(M_city, on_delete=models.CASCADE)
    multiplex_name = models.CharField(max_length=256)
    multiplex_location = models.CharField(max_length=256)
    Multiplex_movie = models.ManyToManyField(to=Movie, blank=True, null=True)
    movie_time = models.ManyToManyField(to=M_time, blank=True, null=True)
    M_screen = models.ManyToManyField(to=M_Screen, blank=True, null=True)

    def __str__(self):
        return f'{self.multiplex_name} - {self.m_city_name}'

    class Meta:
        ordering = ('multiplex_name',)


