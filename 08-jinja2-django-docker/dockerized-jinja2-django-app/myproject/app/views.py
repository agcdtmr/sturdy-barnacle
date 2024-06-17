from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template


# Sample
# def citizen_kane(request):
#     content = """{{movie}} was released in {{year}}"""
#     template = Template(content)
#     context = Context({"movie": "Citizen Kane", "year": 1941})

#     result = template.render(context)
#     return HttpResponse(result)



def base_view(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')