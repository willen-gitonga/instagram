from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewPostForm,EditProfileForm,UpdateProfileForm

@login_required(login_url='/accounts/login/')
def home(request):
    images = Post.get_images()
    
    return render(request, 'index.html', {"images":images})


@login_required(login_url='/accounts/login/')
def search(request):
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        search_profiles = User.objects.filter(username__icontains=search_term)
        profile = Profile.objects.all()
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"profile":search_profiles,"profile":profile})
    else:
        message = "No searched items"
        return render(request,'search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def profile(request,id):
    profile=Profile.objects.all()
    try:
        user = request.user
    except ObjectDoesNotExist:
        return redirect(home)
 
    images = Post.objects.filter(user=user)


  
    return render(request, 'profile.html', {"images":images, "user":user, "profile":profile})

@login_required(login_url='/accounts/login/')
def upload(request):
   current_user = request.user
   if request.method == 'POST':
       form = NewPostForm(request.POST, request.FILES)
       if form.is_valid():
           image = form.save(commit=False)
           image.user = current_user
           image.save()
       return redirect(home)

   else:
       form = NewPostForm()
   return render(request, 'new-post.html', {"form": form})

@login_required(login_url='/accounts/login/')
def edit(request):
    current_user = request.user
    if request.method == 'POST':
      print('boom')
      form = EditProfileForm(request.POST, request.FILES)
      if form.is_valid():
          image = form.save(commit=False)
          image.user = current_user
          image.save()
          return redirect(home)
    else:
       form = EditProfileForm()
    return render(request, 'edit-post.html', {"form": form,"profile":profile})

