from django.contrib import admin
from .models import MovieCategory, Movie


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MovieCategory, CategoryAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ['movie_name', 'slug', 'actors', 'release_date']
    list_editable = ['actors', 'release_date']
    prepopulated_fields = {'slug': ('movie_name',)}
    list_per_page = 15


admin.site.register(Movie, MovieAdmin)
