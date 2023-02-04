from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "nikita/index.html", {
        "posts": posts
    })

def about_me(request):
    return render(request, "nikita/about_me.html")


def post_details(request, slug):

    return render(request, "nikita/post_detail.html")


def custom_404(request, exception):
    return render(request, "404.html", status=404)