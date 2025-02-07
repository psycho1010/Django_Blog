from django.shortcuts import render,redirect

# Create your views here.
from .models import Post #import post model
from .forms import PostForm #import post form

def post_list(request):
    posts = Post.objects.all() #fetch all post from the database
    return render(request, 'posts/post_list.html', {'posts': posts}) #pass the posts to the template

def create_post(request):
    if request.method == 'POST' : #check if the form is submitted
        form = PostForm(request.POST) #bind submitted form data to the form
        if form.is_valid():
            form.save() #save the post data to the database
            return redirect('post_list') #redirect to home page
    else:
        form = PostForm() #create an empty form

    return render(request, 'posts/create_post.html', {'form': form}) #show form