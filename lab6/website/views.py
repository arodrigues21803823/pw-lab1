from django.shortcuts import render


# Create your views here.
def home_page_view(request):
    return render(request, 'website/index.html')

def products(request):
    return render(request, 'website/products.html')

def contacts(request):
    return render(request, 'website/contacts.html')
