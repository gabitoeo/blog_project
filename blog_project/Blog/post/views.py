from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/post_form.html'
    success_url = reverse_lazy('post-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
