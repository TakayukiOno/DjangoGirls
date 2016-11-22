from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list), # ^$というパターンのURLをpost_listというビューに割り当てた。
]