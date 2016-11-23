from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # 同じアプリケーション内のclass Postを呼び出し


# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') # 公開済みのものを公開日で並べ替えしてpostsに代入
    return render(request, 'blog/post_list.html', {'posts': posts}) # 引数 request を 'blog/post_list.html' に渡して返す
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # getobject_or_404 記事がない場合エラー404を出してくれる
    return render(request, 'blog/post_detail.html', {'post': post})