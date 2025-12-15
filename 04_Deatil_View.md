# Display a detail view of the Post.

1. Go to the `blog/views.py` and here we gone a integrate a new view:
```py
    from django.shortcuts import get_object_or_404, render
    from .models import Post

    def detail(request, slug):
        post = get_object_or_404(Post,slug=slug)
        return render(request, 'blog/detail.html',{'post':post})

```
The slug will be the addres for the blog post. To get the url base on the slug we use the `post = get_obejct_or_404(Post,slug=slug)`

2. In the blog app we need to create a new folder `templates/blog` and inside create the file `detail.html`:
```html
    {% extends 'core/base.html' %}
    
    {% block title %}{{post.title}} | {% endblock %}

    {% block content %}
        <h1>{{ post.title }}</h1>
    {% endblock %}
```

3. Then in the blog we need to create a new url file. And we need to mport:
```py
    from django.urls import path
    from . import views

    #slug -> we are expecting a slug, second slug is the name of the
    #paramether define define in the view
    urlpatterns =[
        path('<slug:slug>/',views.detail, name='post_detail'),
    ] 
```
4. Finally we need to import the ulrs file into to `crashblog/urls.py`:
```py
"""
URL configuration for crashblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',frontpage, name='frontpage'),
    path('',include('blog.urls')),
    path('about/',about, name='about'),
]

```
5. Then let go to the `frontpage.html` file and add a link:
```html
{% extends 'core/base.html' %} {% block content %}
<section class="hero">
  <div class="hero-body">
    <div class="container">
      <section class="hero">
        <div class="columns">
          <div class="column is-8 is-offset-2">
            {% for post in posts %}
            <div class ="content is medium">
                <a href="{% url 'post_detail' post.slug %}">
                <h2 class="subtitle is-4">{{post.created_at | date:'M-d-Y'}}</h2>
                <h1 class="title">{{ post.title }}</h1>
                <p>{{ post.intro }}</p>
                </a>
            </div>
            {% endfor %}
          </div>
        </div>
      </section>
    </div>
  </div>
</section>
{% endblock %}

```