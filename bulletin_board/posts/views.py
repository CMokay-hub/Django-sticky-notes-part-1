# posts/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def post_list(request):
    """View to display a list of all posts.
    :param request: The HTTP request object.
    :return: A rendered template displaying the list of posts.
    """
    posts = Post.objects.all()

    # Creating a context dictionary to pass data
    # to the template
    context = {
        "posts": posts,
        "page_title": "List of Posts"
    }

    return render(request, 'posts/post_list.html', context)


def post_detail(request, pk):
    """
    View to display the details of a specific post.

    :param request: The HTTP request object.
    :param pk: The primary key of the post to be displayed.
    :return: A rendered template displaying the details of the post.
    """
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'posts/post_detail.html', post)


def post_create(request):
    """
    View to create a new post.

    :param request: The HTTP request object.
    :return: A rendered template to create a new post
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {'form': form})


def post_update(request, pk):
    """
    View to update an existing post.

    :param request: The HTTP request object.
    :param pk: The primary key of the post to be updated.
    :return: A rendered template to update the specific post.
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form})


def post_delete(request, pk):
    """
    View to delete an existing post.

    :param request: The HTTP request object.
    :param pk: The primary key of the post to be deleted.
    :return: Redirect to the post list view after deletion.
    """
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
