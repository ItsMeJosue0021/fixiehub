from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/list/', views.item_list, name='item_list'),
    path('items/create/', views.item_create, name='item_create'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

]