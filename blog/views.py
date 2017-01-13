from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
import socket

from .models import Post

class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'latest_posts_list'


    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(
            publish__lte=timezone.now()
        ).order_by('-publish')

    def get_context_data(self,**kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['title'] = 'Jason Snider [dot] Com'
        context['description'] = 'Jason Snider [dot] Com'
        context['keywords'] = 'Jason Snider [dot] Com'
        return context

class DetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
