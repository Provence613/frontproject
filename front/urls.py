"""front URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from frontApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('deal/',views.deal),
    path('experiment/',views.experiment),
    path('throughput/',views.throughput),
    path('latency/',views.latency),
    path('detailedLatency/',views.detailedLatency),
    path('txCompletion/',views.txCompletion),
    path('testConfig/',views.testConfig),
    path('download/',views.download),
    path('load/',views.load),
]
