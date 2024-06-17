from jinja2 import Environment
from django.contrib.staticfiles.storage import staticfiles_storage
from jinja2 import Environment, contextfunction
from django.urls import reverse

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
        'url': reverse,
    })
    return env


## Default Config
# from jinja2 import Environment
# from django.contrib.staticfiles.storage import staticfiles_storage
# from django.urls import reverse

# Option #1
# def environment(**options):
#     env = Environment(**options)
#     # Remove or update this line
#     # env.add_extension('jinja2.ext.with_')
#     return env

## Option #2
# def environment(**options):
#     env = Environment(**options)
#     env.globals.update({
#         'static': staticfiles_storage.url,
#         'url': reverse,
#     })
#     return env
