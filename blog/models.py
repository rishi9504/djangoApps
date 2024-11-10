from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse("post_detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created_on"]

    def get_absolute_url(self):

        return reverse("post_detail", kwargs={"pk": self.pk})

    def get_edit_url(self):

        return reverse("post_edit", kwargs={"pk": self.pk})

    def get_delete_url(self):

        return reverse("post_delete", kwargs={"pk": self.pk})


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
