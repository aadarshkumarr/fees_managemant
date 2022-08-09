"""feesmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
from django.urls import path
from feesm import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
                  path('', views.home, name='home'),
                  path('fee_manage/', views.fee_manage, name='fee_manage'),
                  path('add_student/', views.add_student, name='add_student'),
                  path('admin/', admin.site.urls),
                  path('invoice/<str:pk>/', views.invoice, name='invoice'),
                  path('accounts/', include('registration.backends.default.urls')),
                  path('update_fee/<str:pk>/', views.update_fee, name="update_fee"),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
