from django.urls import path
from . import views
from .views import CortarUrlAjax


urlpatterns = [
    path("", views.home, name="home"),
    path("cortar_url_ajax/", CortarUrlAjax.as_view(), name="cortar_url_ajax"),
]