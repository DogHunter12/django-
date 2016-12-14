from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
import warnings

# Create your views here.
from blog.models import Article


def home(request):
    return render(request, 'blog/home.html', {'movies': Article.objects.all()})


def about(request):
    return render(request, 'blog/about.html')


def movies(request, movie_id):
    return render(request, 'blog/movies.html', {'movie': get_object_or_404(Article, id=movie_id)})