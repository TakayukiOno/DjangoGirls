from django.contrib import admin

from .models import Post #　追記 "class Post"というポストモデルを読み込む

# Register your models here.

admin.site.register(Post) # "class Post"というポストモデルを管理画面に登録