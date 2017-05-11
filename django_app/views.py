from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Post, RequestStat
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_list.html',{'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail_tagged.html',{'post':post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            if request.is_ajax():
                print 'was ajax_request'
                from .models import Post
                post_num = len(Post.objects.all().all())
                print post_num
                # return HttpResponseRedirect('')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    form = PostForm()
    return render(request, 'post_edit.html', {'form':form})

def requests(request):
    requests = RequestStat.objects.all().order_by('-id')[:10]
    # print 'is_ajax?'
    if request.is_ajax():
        from django.http import JsonResponse
        from django.utils import timezone
        # print '--AJAX at ', timezone.now().strftime("%H:%M:%S")
        # for f in requests:
        #     print f
        #     if 'is_new: True' in str(f):
        #         print 'Yes'
        new_req_num = len(RequestStat.objects.filter(is_new=True))
        req_stat = [str(k) for k in requests]
        RequestStat.objects.filter(is_new=True).update(is_new=False);

        return JsonResponse({'new_req_num':new_req_num, 'req_stat':req_stat})
    # print 'not ajax'
    return render(request, 'requests.html',{'requests':requests})



from django import forms
class TestForm(forms.Form):
    test_field = forms.CharField()

from django.template import RequestContext, loader
def test_form_submit(request):
    if request.method=="POST":
        form = TestForm(request.POST)
        print 'request post_1'
        if request.is_ajax():
            print 'request is_ajax'
            print request.POST.get('test_field')
    else:
        form = TestForm()
    return render(request, 'test_form.html', {'form':form})
