from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Articles
from .forms import ArticlesForm

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

def create(request):
    submitted = False
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.date = timezone.now()
            article.save()
            return HttpResponseRedirect(f'/news/success/{article.id}')
    else:
        form = ArticlesForm
        if 'submitted' in request.GET:
            submitted = True
    form = ArticlesForm
    return render(request, "news/pages/submit.html", {'form': form, 'submitted': submitted})