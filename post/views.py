from django.shortcuts import render ,get_object_or_404,redirect
# from .forms import *

from .models import *


# Create your views here.
def about(request):
    return render(request,'about.html',{})

#def brand(request):
 #   post=Post.objects.filter(status='p').order_by('-publish')
  #  contax={'post':Post}
   # return render(request,'brand.html',contax)

def contact(request):
    if request .method== 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        masege=request.POST.get('masege')
        print(name,email,phone,masege)
        Contact.object.create(name=name,email=email,phone=phone,masege=masege)
        return redirect('post:index')
    else:
        return render(request,'contact.html',{})
# def contact (request):
#     if request.method == 'POST':
#         form=Cracte_contact(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('post:about')
#     else:
#         form =Cracte_contact(request.POST)
#     contax={'form':form}
#     return render (request,'.html',contax)  
def brand(request):
    return render (request,'brand.html',{})
def index(request):
    return render (request,'index.html',{})
def special(request):
    return render (request,'special.html',{})





