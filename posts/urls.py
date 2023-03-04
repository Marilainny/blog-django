from django.urls import path

from .views import post_list, post_create, post_detail, post_update, post_delete

urlpatterns = [
    path('', post_list),
    path('detail', post_detail),
    path('create', post_create),
    path('update', post_update),
    path('delete', post_delete),
]