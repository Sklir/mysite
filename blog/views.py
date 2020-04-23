from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.

def main(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/main.html', {'posts':posts})

def slim(request):
    return render(request, 'blog/slim.html')

def mass(request):
    return render(request, 'blog/mass.html')

def crossfit(request):
    return render(request, 'blog/crossfit.html')