from django.shortcuts import render
from kiwi_tricote.models import Articles
# Create your views here.
def index(request):
    articles = Articles.objects.all()
    return render(request, 
                  "index.html", 
                  {"articles":articles})