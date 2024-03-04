from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render, redirect, get_object_or_404
from . forms import MovieForm
from . models import MovieCategory, Movie

# Create your views here.
def home(request, c_slug=None):
    if c_slug is not None:
        movie = get_object_or_404(MovieCategory, slug=c_slug)
        movies = Movie.objects.filter(category=movie)
    else:
        movies=Movie.objects.all()
    movie_categ=MovieCategory.objects.all()
    # paginator = Paginator(movie, 6)
    # try:
    #     page = int(request.GET.get('page', '1'))
    # except:
    #     page = 1
    # try:
    #     movies = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     movies = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'res': movies, 'category': movie_categ})


def detail(request, movie_id):
    movies = Movie.objects.get(id=movie_id)
    return render(request, "detail.html", {'ansr': movies})

def update(request, id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, "edit.html", {'form': form, 'movie': movie})

def delete(request, id):
    if request.method=="POST":
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request, "delete.html",)

def add_movie(request):
    if request.method=="POST":
        movie_name=request.POST.get('movie_name')
        desc=request.POST.get('desc')
        category=request.POST.get('category')
        actors=request.POST.get('actors')
        date=request.POST.get('date')
        link=request.POST.get('link')
        image=request.FILES['image']
        movie=Movie(movie_name=movie_name, desc=desc, category_id=category, actors=actors, image=image, release_date=date, trailer_link=link)
        movie.save()
        return redirect('/')
    return render(request, "add.html")