from django.urls import path

from core.erp.views.category.views import *

urlpatterns = [
    # path('category/list/', category_list, name='category_list'), llamada por función
    path('category/list/', CategoryListView.as_view(), name='category_list'), #llamada por clase
    path('category/add/', CategoryCreateView.as_view(), name='category_create'), #llamada por clase
    path('category/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'), #llamada por clase   
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'), #llamada por clase   
]