from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import CommentForm

# Create your views here.


def detail(request, slug):

    post = get_object_or_404(Post, slug=slug)
    
    #If a new form was commit
    if request.method == 'POST':
        
        #Create new instance and pass the new data
        form = CommentForm(request.POST)
        
        if form.is_valid():
            
            #To avoid issues with the Forein Key dont'send this
            comment = form.save(commit = False)
            comment.post = post

            # Save data in the DB
            comment.save()

            #Refresh the page and update one more comment
            return redirect('post_detail', slug=slug)

    else:
        form = CommentForm()

    # Make available the form in the fronend
    return render(request, 'blog/detail.html', {'post': post, 'form': form })
