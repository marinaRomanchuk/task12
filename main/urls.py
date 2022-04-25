from django.urls import re_path as url
from django.urls import path

from main.views import main, result


urlpatterns = [
    path("", main),
    url(r'^results/', result),
]
