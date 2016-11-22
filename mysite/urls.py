from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')), # これでDjangoは'http://127.0.0.1:8000/'に来たリクエストは`blog.urls`へリダイレクトするようになり、それ以降はそちらを参照するようになります。
]
