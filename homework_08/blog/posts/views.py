from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DetailView


# Create your views here.
class PostDetailView(DetailView):
    model = Post
    slug_field = 'id'
    slug_url_kwarg = 'id'

class PostsListView(ListView):
    model = Post
    paginate_by = 5


class PostsCreateView(CreateView):
    model = Post
    success_url = reverse_lazy('posts:posts_list')
    # fields = '__all__'
    fields = ('preview_pic', 'title', 'body')
    template_name_suffix = '_create_form'


class PostsUpdateView(UpdateView):
    model = Post
    success_url = reverse_lazy('posts:posts_list')
    fields = ('preview_pic', 'title', 'body')
    pk_url_kwarg = 'item_pk'
    template_name_suffix = '_update_form'

