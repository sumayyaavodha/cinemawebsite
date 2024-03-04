from . models import MovieCategory

def menu_links(request):
    links=MovieCategory.objects.all()
    return dict(links=links)