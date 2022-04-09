from django.views.generic import DetailView, ListView
from .models import Post 

class PostListViews(ListView):
    model = Post 

class PostDetailViews(DetailView):
    model = Post