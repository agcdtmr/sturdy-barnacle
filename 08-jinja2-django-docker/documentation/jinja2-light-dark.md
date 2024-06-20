# Configuring Light and Dark mode using Jinja2

1. **Create a Jinja2 Environment Configuration:**
   Ensure you have a `jinja2_env.py` file set up to manage Jinja2 configurations.

   ```python
   # core/jinja2_env.py
   from jinja2 import Environment, contextfunction

   @contextfunction
   def light_or_dark_mode(context, element):
       request = context['request']
       mode = request.GET.get('mode')
       if mode == 'dark':
           return f'''
           <a href="{request.path}">Switch to Light Mode</a>
           <style>
             {element} {{
               background-color: #212F3C;
               color: #FFFFF0;
             }}
             {element} a {{
               color: #00BFFF !important;
             }}
           </style>
           '''
       else:
           return f'<a href="{request.path}?mode=dark">Switch to Dark Mode</a>'

   def environment(**options):
       env = Environment(**options)
       env.globals.update({
           'light_or_dark_mode': light_or_dark_mode,
       })
       return env
   ```

2. **Ensure the Jinja2 Environment is Configured in `settings.py`:**

   ```python
   # core/settings.py
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.jinja2.Jinja2',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'environment': 'core.jinja2_env.environment',
           },
       },
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

3. **Create the Template with the Macro Usage:**

   In your template, you can use the `light_or_dark_mode` macro. Ensure the file is saved in the `templates` directory.

   ```html
   <!-- templates/base.html -->
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Home Page</title>
   </head>
   <body>
       {% set element = 'body' %}
       {{ light_or_dark_mode(element)|safe }}
       <h1>Welcome to the Home Page</h1>
       <p>This is a simple Jinja2 template in Django.</p>
   </body>
   </html>
   ```

4. **Define the View to Render the Template:**

   ```python
   # app/views.py
   from django.shortcuts import render

   def home_view(request):
       return render(request, 'base.html')
   ```

5. **Set Up URL Patterns in `urls.py`:**

   ```python
   # core/urls.py
   from django.contrib import admin
   from django.urls import path, include
   from app.views import home_view

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', home_view, name='home'),
   ]
   ```

### Summary

1. **Create a `jinja2_env.py` file** to configure the Jinja2 environment and include the `light_or_dark_mode` macro.
2. **Configure `TEMPLATES` in `settings.py`** to use the Jinja2 environment.
3. **Create the template (`base.html`)** and use the macro within it.
4. **Define the view in `views.py`** to render the template.
5. **Set up the URL patterns** to route to the view.

