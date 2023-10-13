from django.shortcuts import render,HttpResponse
from blogs.models import Post,Category

# Create your views here.
def home(request):
    posts=Post.objects.all()[:11]
    category=Category.objects.all()
    return render(request,'home.html',{'posts': posts , 'category': category})



def post(request,urls):
    post= Post.objects.get(urls=urls)
    category=Category.objects.all()
    return render(request,'post.html',{'post':post,'category': category})
