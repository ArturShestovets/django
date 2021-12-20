from django.urls import path
from .views import index, blog, login, catalogue

urlpatterns = [
    path('', index),
    path('blog/', blog),
    path('login/', login),
    path('catalogue/', catalogue),
]