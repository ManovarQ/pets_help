from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
# from .forms import PostForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic, View

# Create your views here.
class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'pets/pets.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'pets/pets_detail.html', {'post':post})


class AddComments(View):
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')


# def create_post(request):
#     if request.method == "POST":
#         formset = PostForm(request.POST, request.FILES)
#         if formset.is_valid():
#             formset.save()
#             return HttpResponseRedirect(('/'))
#         else:
#             raise ValueError('Some logic broken')
#
#     elif request.method == "GET":
#         post_form = PostForm()
#         return render(request, "pets/create_post.html", context={"form":post_form})
#     else:
#         raise ValueError(f'Method {request.method} is not supported')

# class PostFormView(generic.FormView):
#     template_name = 'pets/create_post.html'
#     form_class = PostForm
#     success_url = '/'

class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'description', 'author', 'date', 'img']
