from django.db import models
from django.utils.text import slugify

# Create your models here.
# title - content - publish_at - img - category


class News(models.Model):
    title = models.CharField(max_length=50, primary_key=True)
    content = models.TextField()
    img = models.ImageField(upload_to='news_img/' , default='news_img/')
    publish_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(News,self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name


