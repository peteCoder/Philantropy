
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import *
from .forms import *
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.views.generic import *
from django.core.paginator import Paginator




#For the View of ERROR PAGES

def custom_error_view(request, exception=None): 
   return render(request, 'error/500.html', {})

def custom_permission_denied(request, exception=None):
   return render(request, 'error/403.html', {})

def custom_bad_request(request, exception=None):
   return render(request, 'error/400.html', {})

def custom_page_not_found(request, exception):
    return render(request, 'error/404.html', {})


class Blog(ListView):
    model = Post
    template_name = "blog.html"
    paginate_by = 3
    ordering = ['-date_created']


    context_object_name = "posts"


    def get_context_data(self, *args, **kwargs):
        
        context = super(Blog, self).get_context_data(*args, **kwargs)
       
        return context


def blog_single(request, pk):
    
    obj = get_object_or_404(Post, pk=pk)

    stuff = get_object_or_404(Post, pk=pk)
    total_likes = stuff.total_likes()

    liked = False
    if stuff.likes.filter(pk=request.user.id).exists():
        liked = True

    context = {
    'obj':obj,
   
    'total_likes': total_likes,
    }
    return render(request, "blog-single.html", context)



############################################################

def LikeView(request, pk):
    obj = get_object_or_404(Post, pk=request.POST.get('obj_id'))
    liked = False
    if obj.likes.filter(pk=request.user.id).exists():
        obj.likes.remove(request.user)
        liked = False
    else:
        obj.likes.add(request.user)
        liked = True
    return HttpResponseRedirect( reverse('article_detail', args=[str(pk)]))


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_blog/add_post.html'
    success_url = reverse_lazy("blog")

    def get_context_data(self, *args, **kwargs):
        
        context = super(AddPostView, self).get_context_data(*args, **kwargs)
       
        return context

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_blog/update_post.html'
    success_url = reverse_lazy('blog')

    def get_context_data(self, *args, **kwargs):
        
        context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
      
        return context

class DeletePostView(DeleteView):
    model = Post
    template_name = 'edit_blog/delete_post.html'
    success_url = reverse_lazy("blog")

    def get_context_data(self, *args, **kwargs):
       
        context = super(DeletePostView, self).get_context_data(*args, **kwargs)
        
        return context



