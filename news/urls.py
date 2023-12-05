from django.urls import path
from news.views import index, details, categories


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", details, name="news-details-page"),
    path("categories", categories, name="categories-form")
]
