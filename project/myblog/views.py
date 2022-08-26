from django.shortcuts import render, redirect
from myblog.models import Post, Comment, Contact
from datetime import datetime
from myblog.forms import CommentForm, ContactForm
from django.http import HttpResponseRedirect


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {'posts': posts}
    return render(request, 'blog_index.html', context)


def blog_category(request, category):
    posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )
            comment.save()
    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog_detail.html', context)


def blog_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message'],
            )
            contact.save()
            return redirect('blog_index')

    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'blog_contact.html', context)
