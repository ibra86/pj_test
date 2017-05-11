def post_num(request):
    from .models import Post
    post_num = len(Post.objects.all().all())
    return {'post_num':post_num}

def portal_url(request):
    from django_proj.settings import PORTAL_URL
    return {'PORTAL_URL': PORTAL_URL}

def context_requests(request):
    # print 'context_processor'
    return request
