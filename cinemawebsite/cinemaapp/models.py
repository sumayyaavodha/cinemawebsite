from django.db import models
from django.urls import reverse


# Create your models here.
class MovieCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'moviecategory'
        verbose_name_plural = 'moviecategories'

    def get_url(self):
        return reverse('cinemaapp:movie_category', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class Movie(models.Model):
    movie_name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    image = models.ImageField(upload_to='gallery', blank=True)
    desc = models.TextField(blank=True)
    actors = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(MovieCategory, on_delete=models.CASCADE)
    release_date = models.DateField(null=True, blank=True)
    trailer_link = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('movie_name',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'

    def get_url(self):
        return reverse('cinemaapp:category', args=[self.category.slug, self.slug])

    def __str__(self):
        return '{}'.format(self.movie_name)