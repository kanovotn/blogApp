from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy 
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here
#def home(request):
#    return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    #ordering = ['-id']    
    
    def get_context_data(self, **kwargs):
        
        # Get stored posts into the list
        queryset = Post.objects.all()
        first_post = queryset.first()
        posts_list = list(queryset)

        # Remove the first post, it is stored separately
        if posts_list:
            posts_list.pop(0)
        
        # Call the base implementation first to get the context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['first_post'] = first_post
        context['posts_list'] = posts_list
        return context

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'
    
    def get_context_data(self, **kwargs):
        queryset = Category.objects.all()
        category_list = list(queryset)
        
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['category_list'] = category_list
        category_list_length = len(category_list)
        if (category_list_length % 2 == 0):
            context['category_list_half'] = category_list_length//2
        else:
            context['category_list_half'] = (category_list_length + 1)//2
        return context

class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'
    #field = {'title', 'body'}
    
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

    
class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = {'title', 'title_tag', 'body'}

class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')