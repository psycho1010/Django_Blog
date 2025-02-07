from django.shortcuts import render,redirect,get_object_or_404

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



def edit_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)  # Fetch post or return 404 if not found

    if request.method == 'POST':  
        form = PostForm(request.POST, instance=post)  # Bind form to existing post
        if form.is_valid():  
            form.save()  # Save updated post
            return redirect('post_list')  # Redirect to post list
    else:
        form = PostForm(instance=post)  # Pre-fill form with existing data

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'posts/delete_post.html', {'post': post})