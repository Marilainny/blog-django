from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from posts.models import Post


# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        try:
            instance.save()
            messages.success(request, "Sucessfully Created")
            return HttpResponseRedirect(instance.get_absolute_url())
        except Exception as e:
            messages.error(request, "Not Sucessfully Created")
            form.add_error(None, e)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": instance.title,
        "instance": instance,
    }
    return render(request, "post_detail.html", context)

def post_list(request):
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        try:
            instance.save()
            messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
            return HttpResponseRedirect(instance.get_absolute_url())
        except Exception as e:
            form.add_error(None, e)

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)

def post_delete(request, id=None):
    return HttpResponse("<h1>Delete</h1>")