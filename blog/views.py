from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
  #postsの中には今まで投稿したデータ（記事）が投稿順に保持されている状態。
  posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
  #橋渡しの部分、DB（クエリセット）の情報をテンプレートに受け渡す。
  return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
  post = get_object_or_404(Post, pk=pk)
  return render(request, 'blog/post_detail.html', {'post':post})
