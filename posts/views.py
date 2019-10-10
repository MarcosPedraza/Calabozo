from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse,HttpResponseRedirect, Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from posts.models import Post
from posts.forms import PostForm
from django.utils import timezone
from django.db.models import Q

# Create your views here.

def crear_post(request):

    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        intance = form.save(commit=False)
        intance.save()
        messages.success(request, "El Post se creo bien mi pequeño padawan")
        post = Post.objects.all()
        contexto = {'posts':post}
        return render(request,"post_list.html",context=contexto)
    contexto = {
        "form": form,
    }
    return render(request, "post_form.html", contexto)

def detalle_post(request, id):
    instancia = get_object_or_404(Post, id=id)
    contexto = {
        "titulo":instancia.titulo,
        "obj":instancia,
    }
    return render(request, "form_detalle.html",context=contexto)

def home_render(request):
    return render(request, "bienvenida.html")

def about_render(request):
    return render(request, "about.html")

def contacto_view(request):
    return render(request,"contacto.html")


def post_list(request):
    #hoy = timezone.now().date()
    queryset_list = Post.objects.all().order_by("-fecha")
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
            Q(titulo__icontains=query) |
            Q(descripcion__icontains=query)
        ).distinct()
    paginator = Paginator(queryset_list, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    #post = Post.objects.all()#.order_by("-fecha")
    contexto = {
        "object_list": queryset,
        "page_request_var": page_request_var,
    }

    return render(request,"post_list.html", context=contexto)

    #return HttpResponse("<h1>lista post</h1>")

def categoria_view(request):
    return render(request,"categorias.html")

def cat_fisico(request):
    filtro_post = Post.objects.filter(categoria="fisico")

    #queryset_list = Post.objects.all().order_by("-fecha")

    paginator = Paginator(filtro_post, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    contexto = {
        "object_list": queryset,
        "page_request_var": page_request_var,
    }

    return render(request,"post_list.html",context=contexto)

def cat_online(request):
    filtro_post = Post.objects.filter(categoria="online")

    #queryset_list = Post.objects.all().order_by("-fecha")

    paginator = Paginator(filtro_post, 5)
    page_request_var = "page"
    page = request.GET.get(page_request_var)

    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    contexto = {
        "object_list": queryset,
        "page_request_var": page_request_var,
    }

    return render(request,"post_list.html",context=contexto)

def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)
