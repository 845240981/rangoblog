from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(unique=True,max_length=128)
    view = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)

    def __unicode__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128,unique=True)
    url= models.URLField()
    views= models.IntegerField(default=0)


    def __unicode__(self):
        return self.title

