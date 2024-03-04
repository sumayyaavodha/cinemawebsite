from django import forms
from . models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['movie_name', 'desc', 'actors', 'category', 'image', 'release_date', 'trailer_link']