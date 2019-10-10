from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    imagen = models.ImageField(upload_to="imagenes", blank=True, null=True)
    descripcion = models.TextField()
    fecha = models.DateField(auto_now=False,auto_now_add=True)


    def __str__(self):
        return self.titulo


    class Meta:
        ordering = ["-fecha"]




class Categoria(models.Model):
    titulo = models.CharField(max_length=100,unique=True)


def create_slug(instance, new_slug=None):
    slug = slugify(instance.titulo)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug





def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)




