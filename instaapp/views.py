from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post,Profile,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import NewPostForm,EditProfileForm,UpdateProfileForm,CommentForm

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

@login_required(login_url='/accounts/login/')
def comment(request,c_id):
  comments = Comment.objects.filter(image_id=c_id)
  current_user = request.user
  current_image = Post.objects.get(id=c_id)

  if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
          comment = form.save(commit=False)
          comment.image = current_image
          comment.user = current_user
          comment.save()
          return redirect(home)
  else:
      form = CommentForm()
  return render(request,'comments.html',{"form":form,'comments':comments,"image":current_image,"user":current_user})

