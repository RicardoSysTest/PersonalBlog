# Add New Functions

1. Create a new application call blog 
```bash
	py manage.py starapp blog
```

2. Then install this app in the  settings

```py
	INSTALLED_APPS = [
         ...,
         'blog.apps.BlogConfig'
         ...,
        ]
```
3. Then we need to open the `modesl.py` to create or first Django Model inside this new application (`blog/models.py`). 
Inside we need to create a new class `class Post():` that inherence from `model.Model`:
```py
	from django.db impor models
	class Post(model.Model):

                #Char Fiel for the Title of the Post
		title = models.CharField(max_length=255)

                slug = models.SlugField()


                intro = models.TextField()


                body = models.TextField()

                created_at = models.DateTimeField(auto_now_add=True)
``` 

4. Then we need to update the DB with the followin commands:
```bash
        py manage.py makemigrations 
```

5. Then we need to execute the update instrucion of the DB with the followin commands:
```bash
        py manage.py migrate 
```

6. After we need to open the file `blog/admin.py` and update the file with the models:
```py
from .models import Post

admin.site.regiester(Post)
```

7. At this point we are ready to go the the admin site and we can add some post to confirm that every still working.

8. Go to the file `core/views.py`. Here we need to import the data model Post from blog. Then request all the data from models to add in the content in the fronpage view
```py 

from blog.models import Post

def fronpage(request);
        posts = Post.objects.all()
        return render(request, 'core/frontpage.html',{'posts':posts})
```
9. Then we need to update the HTML with the conten that we gone pass trougth the dicciontary with the key posts.
```html
   {% extends 'core/base.html' %} 
   
   {% block content %}
        <section class="hero">
                <div class="hero-body">
                        <div class="container">
                                <section class="hero">
                                        <div class="columns">
                                                <div class="column is-8 is-offset-2">
                                                        {% for post in posts %}
                                                        <h2 class="subtitle is-4"> {{post.created_at|date:'M-d-Y'}} </h2>
                                                        <h1 class="title">{{ post.title }}</h1>
                                                        <p>{{ posti.intro }}</p>
                                                        {% endfor %}
                                                </div>
                                        </div>
                                </section>
                        </div>
                </div>
        </section>
   {% endblock %}
     
```

10. Then we need change the order in which the data are display  editing the models:
```py
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
```