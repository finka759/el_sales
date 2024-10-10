from django.urls import path

from networkapp.apps import NetworkappConfig
from networkapp.views import ProductCreateApiView, ProductUpdateApiView, ProductRetrieveApiView, ProductListApiView, \
    ProductDestroyApiView, LinkCreateApiView, LinkRetrieveApiView, LinkListApiView, LinkDestroyApiView, \
    LinkUpdateApiView

app_name = NetworkappConfig.name

urlpatterns = [
    path('product/create/', ProductCreateApiView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateApiView.as_view(), name='product_update'),
    path('product/retrieve/<int:pk>/', ProductRetrieveApiView.as_view(), name='product_retrieve'),
    path('product/destroy/<int:pk>/', ProductDestroyApiView.as_view(), name='product_destroy'),
    path('product/list/', ProductListApiView.as_view(), name='product_list'),

    path('link/create/', LinkCreateApiView.as_view(), name='link_create'),
    path('link/update/<int:pk>/', LinkUpdateApiView.as_view(), name='link_update'),
    path('link/retrieve/<int:pk>/', LinkRetrieveApiView.as_view(), name='link_retrieve'),
    path('link/destroy/<int:pk>/', LinkDestroyApiView.as_view(), name='link_destroy'),
    path('link/list/', LinkListApiView.as_view(), name='link_list'),
]
