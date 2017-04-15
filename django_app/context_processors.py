def post_num(request):
    from .models import Post
    post_num = len(Post.objects.all().all())
    return {'post_num':post_num}
