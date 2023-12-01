from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()
    img = models.ImageField(upload_to='image/%Y')


    def get_absolute_url(self):
        return ('/')


    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts'


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    text_comments = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comments'
        verbose_name_plural = 'Comments'
