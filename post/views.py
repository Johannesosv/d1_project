from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
def index(request):
   # return HttpResponse('HELLO FROM POST')
   post=Post.objects.all()[:10]
   context = {
   'title': 'Latest Posts',
   'post': post
   }
   return render(request,'post/index.html',context)
   
def details(request,id):
	p = Post.objects.get(id=id)

	context ={
	'p': p

	}
	return render(request,'post/details.html',context)