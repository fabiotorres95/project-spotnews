from django.shortcuts import render
from news.models import News


def index(request):
    news_data = News.objects.all()
    news_list = []
    for data in news_data:
        parts = str(data.created_at).split('-')
        converted = f"{parts[2]}/{parts[1]}/{parts[0]}"
        news_list.append(
            {
                "title": data.title,
                "content": data.content,
                "author": data.author,
                "created_at": converted,
                "image": data.image,
                "categories": data.categories,
            }
        )

    data = {
        "news_list": news_list,
    }

    return render(request, 'home.html', data)
