from django.shortcuts import render
from news.models import News


def index(request):
    news_data = News.objects.all()
    news_titles = [news.title for news in news_data]
    data = {
        "news_titles": news_titles
    }

    return render(request, 'home.html', data)
