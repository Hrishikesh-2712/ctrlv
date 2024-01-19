from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Clipboard(models.Model):
    user = models.OneToOneField(User, null=True, on_delete = models.CASCADE)
    topic = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True)  # description
    field = RichTextField(null=True)  # rich text field
    create_date = models.DateField(auto_now_add=True, null=True)
    expire_date = models.DateField(null=True)  # deletion date

    def __str__(self):
        return self.topic

# example below
class Reporter(models.Model):
    full_name = models.CharField(max_length=70)

    def __str__(self):
        return self.full_name


class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
