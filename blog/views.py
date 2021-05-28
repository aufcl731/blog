from django.shortcuts import render, redirect
from blog.models import *

def main(request):
    msg = {'msg': request}
    return render(request, 'html/main.html', msg)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'html/detail.html', {'posts': post})
