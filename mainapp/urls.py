"""mainapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as account_views
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage.as_view(),name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls',namespace="accounts")),
    path('posts/',include('posts.urls',namespace='posts')),
    path('groups/',include('groups.urls',namespace='groups')),
    path('polls/',include('polls.urls',namespace='polls')),
    path('profile/', account_views.profile, name='profile'),
    path('writers/',include('writers.urls',namespace='writers')),
    path('blog/',include('blog.urls',namespace='blog')),


    path('password-reset/',
          auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"),
          name="password_reset"),

    path('password-reset/done/',
          auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),
          name="password_reset_done"),

    path('password-reset-confirm/<uidb64>/<token>/',
          auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm.html"),
          name="password_reset_confirm"),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),
         name="password_reset_complete"),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
