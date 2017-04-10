from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post
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
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    form = PostForm()
    return render(request, 'post_edit.html', {'form':form})




from django import forms
class TestForm(forms.Form):
    field1 = forms.CharField()

def test_form_submit(request):
    if request.method == "POST":
        form = TestForm(request.POST)
    else:
        form = TestForm()
    return render(request, 'test_form.html', {'form':form})
