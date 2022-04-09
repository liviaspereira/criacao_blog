from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListViews.as_view(), name='post_list'),   # Conectando a URL sem argumento com a view PostListViews
    path("<slug:slug>/", views.PostDetailViews.as_view(), name="post_detail"), # Conectando a url que tem slug como argumento com a view PostDetailViews
    ]
