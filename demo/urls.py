"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import include, path

from demo.demo_app.forms import Article, ArticleForm


def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()
    upload_permission = getattr(settings, "KINDEDITOR_UPLOAD_PERMISSION", None)
    data = {"form": form, "upload_permission": upload_permission}
    return render(request, "index.html", data)


def article_detail(request, pk):
    obj = get_object_or_404(Article, pk=pk)
    return render(request, "detail.html", {"object": obj})


urlpatterns = [
    path("", index, name="index"),
    path("<int:pk>", article_detail, name="article-detail"),
    path("admin/", admin.site.urls),
    path("kindeditor/", include("kindeditor.urls")),
    path("accounts/", include("allauth.urls")),
]

if settings.DEBUG:
    # static and media
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
