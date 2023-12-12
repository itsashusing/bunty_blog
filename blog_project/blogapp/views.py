from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .form import AddPostForm, EditPostForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def Home(request):
    posts = Post.objects.all().order_by('-id')
    total = Post.objects.all().count()

    items_per_page = 4
    paginator=Paginator(posts,items_per_page)

    page = request.GET.get('page')


    try:
        # Get the Page object for the given page number
        current_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        current_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        current_page = paginator.page(paginator.num_pages)

    return render(request, 'blogapp/home.html', {'title': 'Home', 'posts': posts, 'total': total,'current_page': current_page})


def DetailsView(request, id):
    post = Post.objects.get(id=id)
    print(post.author)
    print(request.user)
    return render(request, 'blogapp/details.html', {'title': 'Home', 'post': post})




@login_required
def DeleteView(request, id):
    post = Post.objects.get(id=id)
    if request.user == post.author:
        post.delete()
        return redirect('/')
    else:
        messages.error(request,f'You have not permission to perform certain operations')
        return redirect('/')



@login_required
def AddPost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            body = request.POST['body']
            author = request.user
            form = Post(title=title, body=body, author=author)
            form.save()
            messages.success(request, f'New post has been added successfully.')
            return redirect('/')
        else:
            messages.error(
                request, f'Something went wrong tyr after some time.')
    else:
        form = AddPostForm()

    return render(request, 'blogapp/addpostform.html', {'form': form})


@login_required
def EditPost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = EditPostForm(request.POST)
        if form.is_valid():
            form = EditPostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
            messages.success(
                request, f'Your post has been updated successfully.')
            return redirect('/')
        else:
            messages.error(
                request, f'Something went wrong tyr after some time.')

    form = EditPostForm(instance=post)
    return render(request, 'blogapp/editpost.html', {'form': form})

def MyPosts(request,id):
    posts=Post.objects.filter(author_id=id)
    total = Post.objects.filter(author_id=id).count()

    items_per_page = 2
    paginator=Paginator(posts,items_per_page)

    page = request.GET.get('page')


    try:
        # Get the Page object for the given page number
        current_page = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        current_page = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        current_page = paginator.page(paginator.num_pages)


    return render(request,'blogapp/mypost.html',{'posts':posts,'total':total,'current_page':current_page})
