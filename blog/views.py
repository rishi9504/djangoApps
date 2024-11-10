from django.shortcuts import render
from blog.models import Post, Comment

# Create your views here.


def blog_index(request):
    """
    This function renders the main blog page, which displays a list
    of all the blog posts in reverse chronological order.
    """
    # Get all the posts from the database and order them by the
    # timestamp of when they were created, in descending order (newest
    # first). This is an example of how to use Django's ORM.
    posts = Post.objects.all().order_by("-created_on")

    # Create a context dictionary that will be passed to the
    # template, which will then display the posts. The key is a
    # string that will be used in the template to access the value.
    context = {
        "posts": posts,
    }

    # Use Django's built-in render shortcut to render the
    # blog_index.html template with the posts context dictionary.
    return render(request, "blog/index.html", context)


def blog_category(request, category):
    """
    This function renders the blog page, which displays a list
    of all the blog posts in reverse chronological order.
    """
    # Get all the posts from the database and order them by the
    # timestamp of when they were created, in descending order (newest
    # first). This is an example of how to use Django's ORM.
    posts = Post.objects.filter(categories__name_contains=category).order_by(
        "-created_on"
    )

    # Create a context dictionary that will be passed to the
    # template, which will then display the posts. The key is a
    # string that will be used in the template to access the value.
    context = {
        "category": category,
        "posts": posts,
    }

    # Use Django's built-in render shortcut to render the
    # blog_index.html template with the posts context dictionary.
    return render(request, "blog/category.html", context)


def blog_detail(request, pk):
    # Retrieve a single post from the database using its primary key (pk).
    # This returns an instance of the Post model.
    post = Post.objects.get(pk=pk)

    # Retrieve all comments related to the specific post.
    # This returns a QuerySet of Comment instances.
    comments = Comment.objects.filter(post=post)

    # Create a context dictionary that will be passed to the template.
    # The dictionary contains the post and its related comments.
    context = {
        "post": post,
        "comments": comments,
    }

    # Render the 'blog/detail.html' template with the context dictionary.
    # The template is responsible for displaying the post and its comments.
    return render(request, "blog/detail.html", context)
