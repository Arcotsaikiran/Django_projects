from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "index.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "bloghome.html")

def blogpost(request, slug):
    return HttpResponse(f"This is blogpost page {slug}" )

def base(request):
    return render(request, "base.html")

def search(request):
    return render(request, "search.html")