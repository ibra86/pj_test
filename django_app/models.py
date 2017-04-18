from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    # author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(blank=True,null=True)

    class Meta:
        ordering = ['pk']

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Book(models.Model):

    title = models.CharField(max_length=200)
    post = models.ManyToManyField(
        Post,
        through='BookContent',
        )

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

class BookContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __unicode__(self):
        return 'Post "%s" of Book "%s"' %(self.post, self.book)
