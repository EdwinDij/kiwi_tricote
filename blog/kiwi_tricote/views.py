from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from kiwi_tricote.models import Articles
# Create your views here.
def index(request):
    articles = Articles.objects.all()
    return render(request, 
                  "blog/index.html", 
                  {"articles":articles})
    
def one_article(request, slug):
    article = get_object_or_404(Articles, slug=slug)
    return render(request, 'blog/article.html', context={'articles': article})