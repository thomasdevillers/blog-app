from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post #import Post model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #login required to create post
from django.contrib.auth.models import User #import User model

# Create your views here.

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context) #templates/blog/home.html

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #default is object_list
    ordering = ['-date_posted'] #order by date_posted (newest to oldest) (minus sign reverses order)
    paginate_by = 3 #5 posts per page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #default is object_list
    ordering = ['-date_posted'] #order by date_posted (newest to oldest) (minus sign reverses order)
    paginate_by = 3 #5 posts per page

    def get_queryset(self): #override get_queryset method
        user = get_object_or_404(User, username=self.kwargs.get('username')) #get username from url
        return Post.objects.filter(author=user).order_by('-date_posted') #return posts by user

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content'] #fields to display in form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content'] #fields to display in form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #prevent users from updating other users' posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): #delete post
    model = Post
    success_url = '/' #redirect to home page after deleting post

    def test_func(self): #prevent users from deleting other users' posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
        'title': "About"
    }
    return render(request, 'blog/about.html', context) #templates/blog/about.html
