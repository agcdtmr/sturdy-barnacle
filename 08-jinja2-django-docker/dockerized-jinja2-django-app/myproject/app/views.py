from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from datetime import datetime

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

def current_datetime(request):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render(request, 'current_datetime.html', {'now': now})

def shop(request):
    products = [
        {"name": "Product A", "price": 100, "in_stock": True},
        {"name": "Product B", "price": 80, "in_stock": False},
        {"name": "Product C", "price": 120, "in_stock": True},
        {"name": "Product D", "price": 190, "in_stock": False},
    ]
    return render(request, 'shop.html', {'products': products})
