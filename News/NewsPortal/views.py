from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin


class PostView(ListView):

    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = Post.objects.all().order_by('-dateCreation')
    #     self.filterset = PostFilter(self.request.GET, queryset=queryset)
    #     return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now', ] = datetime.utcnow()
        # context['filterset'] = self.filterset
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'one_news.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class PostSearchView(ListView):
    model = Post
    template_name = "search.html"
    context_object_name = 'posts_search'
    ordering = '-dateCreation'
    paginated_by = 10

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-dateCreation')
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['time_now', ] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


# def create_news(request):
#     form = PostForm()
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/news/')
#     return render(request, 'news_create.html', {'form': form})


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = "news_create.html"


def PostDelete(request, pk):
    post = Post.objects.get(pk=pk)
    # page_path = request.path
    post.delete()
    # return redirect(page_path)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST or None, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list_of_news')
    else:
        form = PostForm(instance=post)
    return render(request, 'news_update.html', {
        'post': post,
        'form': form})
