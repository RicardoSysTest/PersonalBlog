# 02 Create Your First App

1. Creatre your first app with the following commnad
```bash
py manage.py startapp core
```
2. Install the application. Go the the file `settings.py` sertch the list `INSTALLED_APPS` and add the application
```py
INSTALLED_APPS = [
    ...,
    core.apps.CoreConfig
    ...,
]
```
The command ins structures in this way. First the name of the app in this case `core` then we have the name of the files, in this case `apps` for the app.py and finally the name of the class, fort this one the name is `CoreConfig`
3.  Then we need plan to create a base template. Insde the core folder create a new folder call `temaplates` and inside create another call `core` and inside we need to create a html file call `base.html`. Inside this folder we need to edit the following content: 
```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Crash Blog</title>
    </head>
    <body>
        <h1>Welcome to my Side Project to create a blog</h1>
    </body>
    </html>
```
4. To display this html file we need open the `views.py` and to create function responsible to render the html file. 
```py
    def frontpage(request):
        return render(request, 'core/base.html')
```
Render is a shortcut to django to say render the HTML in your screen
5. Then we need to import this view in the file `urls.py` to the folder `crashblog/settings.py`:
```py
    from core.views import frontpage

    ulrpatterns = [
        path('',frontpage, name='frontapage'),
    ]
```
6. Now we need to extend the the base template to avoid to have alot of code in the html. To to this we need to create another call `frontpage.html` and from there we need to extend the content of the `base.html`. To do this we need to add in our `base.html` the code `{% block content%} {% endblock %}`:
```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{% block title %} {% endblock %} | My Personal Page</title>
    </head>
    <body>
        {% block content %} {% endblock %}
    </body>
    </html>

```

7. To extend the `frontpage.html` template from the `base.html` template we need to write in the frontpage the following code:
```html
    {% extends 'core/base.html' %}

    {% block content %}
        <h1>Hello Welcome to My Personal Blog</h1>
    {% endblock %}
```

8. And then we need to change the template that want to render. First we have `core/base.html` and we need to remplace this for `core/frontpage.html`
```py
    def frontpage(request):
        return render(request,'core/frontpage.html')
```
9. To have more clear understanding we can add the about page as excersice.

10. To finish this lection we want to customize this version. So open this [template](view-source:https://bulmatemplates.github.io/bulma-templates/templates/blog-tailsaw.html) and review the source. You can copy the tree meta tags:
```html
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
```
11. Then copy the ulr for Bulma:
```html
   <link rel="stylesheet" href="https://unpkg.com/bulma@1.0.4/css/bulma.min.css" />
```

12. Copy the style
```html
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito&display=swap');
  	body {font-family: 'Nunito', sans-serif;};
    nav.navbar {
      height: 6rem !important;
      box-shadow: 0 1px 3px 0 rgba(0, 0, 0, .1), 0 1px 2px 0 rgba(0, 0, 0, .06) !important;
    }
    ::-webkit-scrollbar{height:10px;width:10px}::-webkit-scrollbar-track{background:#efefef;border-radius:6px}::-webkit-scrollbar-thumb{background:#d5d5d5;border-radius:6px}::-webkit-scrollbar-thumb:hover{background:#c4c4c4}
  </style>
```

13. Then we need to copy the navigation bar:
```html
      <!-- START NAV -->
  <nav class="navbar">
    <div class="container">
      <div class="navbar-brand">
        <a class="navbar-item" href="../">
          <strong>Crash Blog</strong>
        </a>
        <span class="navbar-burger burger" data-target="navbarMenu">
          <span></span>
          <span></span>
          <span></span>
        </span>
      </div>
      <div id="navbarMenu" class="navbar-menu">
        <div class="navbar-end">
          <div class=" navbar-item">
            <div class="control has-icons-left">
              <input class="input is-rounded" type="email" placeholder="Search">
              <span class="icon is-left">
                <i class="fa fa-search"></i>
              </span>
            </div>
          </div>
          <a class="navbar-item is-active is-size-5 has-text-weight-semibold">
            Home
          </a>
          <a class="navbar-item is-size-5 has-text-weight-semibold">
            Examples
          </a>
          <a class="navbar-item is-size-5 has-text-weight-semibold">
            Features
          </a>
        </div>
      </div>
    </div>
  </nav>
  <!-- END NAV -->
```
14. Update format
```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />

    <title>{% block title %}{% endblock %} Blog</title>

    <link
      rel="stylesheet"
      href="https://unpkg.com/bulma@1.0.4/css/bulma.min.css"
    />
    <link
      href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
      rel="stylesheet"
      integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN"
      crossorigin="anonymous"
    />

    <style>
      @import url("https://fonts.googleapis.com/css2?family=Nunito&display=swap");
      body {
        font-family: "Nunito", sans-serif;
      }
      nav.navbar {
        height: 6rem !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1),
          0 1px 2px 0 rgba(0, 0, 0, 0.06) !important;
      }
      ::-webkit-scrollbar {
        height: 10px;
        width: 10px;
      }
      ::-webkit-scrollbar-track {
        background: #efefef;
        border-radius: 6px;
      }
      ::-webkit-scrollbar-thumb {
        background: #d5d5d5;
        border-radius: 6px;
      }
      ::-webkit-scrollbar-thumb:hover {
        background: #c4c4c4;
      }
    </style>
  </head>
  <body>
    <!-- START NAV -->
    <nav class="navbar">
      <div class="container">
        <div class="navbar-brand">
          <a class="navbar-item" href="../">
            <strong>Crash Blog</strong>
          </a>
          <span class="navbar-burger burger" data-target="navbarMenu">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </div>
        <div id="navbarMenu" class="navbar-menu">
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="control has-icons-left">
                <input
                  class="input is-rounded"
                  type="text"
                  placeholder="Search"
                />
                <span class="icon is-left">
                  <i class="fa fa-search"></i>
                </span>
              </div>
            </div>
            <a class="navbar-item is-active is-size-5 has-text-weight-semibold">
              Home
            </a>
            <a class="navbar-item is-size-5 has-text-weight-semibold">
              Examples
            </a>
            <a class="navbar-item is-size-5 has-text-weight-semibold">
              Features
            </a>
          </div>
        </div>
      </div>
    </nav>
    <!-- END NAV -->

    <section class="section">
      <div class="container">{% block content %} {% endblock %}</div>
    </section>
  </body>
</html>

```