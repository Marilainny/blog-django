from django.urls import path

from .views import post_list, post_create, post_detail, post_update, post_delete

urlpatterns = [
    path('', post_list),
    path('create/', post_create),
    path('update/<int:id>/', post_update),
    path('delete/<int:id>/', post_delete),
    path('detail/<int:id>/', post_detail, name='detail'),

]