from __future__ import unicode_literals
import datetime, uuid

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Post(models.Model):

    """ Post model. """
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Published'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    body = models.TextField(null=True)
    description = models.CharField(null=True,max_length=500)
    keywords = models.CharField(null=True,max_length=500)
    tags = models.CharField(null=True,max_length=500)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    publish = models.DateTimeField(default=datetime.datetime.now)
    author = models.ForeignKey(User, null=True)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    def save(self):
        # beforeSave
        super(Post, self).save()
        self.slug = slugify(self.title)
        super(Post, self).save()

    def __str__(self):
        # Display results by title
        return self.title

    def get_absolute_url(self):
        kwargs = {'slug': self.slug}
        return reverse('view', kwargs=kwargs)