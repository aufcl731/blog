from django.shortcuts import render, redirect
from django.utils import timezone
from blog.models import Post

def main(request):
    msg = {'msg': request}
    return render(request, 'html/main.html', {})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'html/detail.html', {'posts': post})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    list2 = Post.objects.filter(title__contains='title')
    print(posts)
    print(list2)
    return render(request, 'html/post_list.html', {'posts': posts, 'list2': list2})




