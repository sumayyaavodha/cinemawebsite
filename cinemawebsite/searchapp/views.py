from django.db.models import Q
from django.shortcuts import render
from cinemaapp.models import Movie
# Create your views here.

def SearchResult(request):
    movies = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        movies = Movie.objects.all().filter(Q(movie_name__contains=query) | Q(actors__contains=query) | Q(desc__contains=query))
    return render(request, "search.html", {'query': query, 'movies': movies})