from django.utils import timezone
from .models import Post


def latest_posts(request):
    # 公開済みの記事を新しい順で5件取得
    posts = Post.objects.filter(
        published_date__lte=timezone.now()
    ).order_by('-published_date')[:5]

    return {'latest_posts': posts}
