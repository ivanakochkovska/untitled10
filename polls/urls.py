from django.urls import  path

from . import views

urlpatterns = [

    path('/basic', views.basic_seir_model),
    path('/s', views.seir_model_wth_social_distancing),
    path('/net', views.network),
    path('/dist', views.network_with_social_distancing),
    path('/index', views.redirect)
]