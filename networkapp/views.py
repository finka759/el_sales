from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from networkapp.serializers import ProductSerializer, LinkSerializer

from networkapp.models import Product, Link
from users.permissions import IsActiveUser


class ProductCreateApiView(generics.CreateAPIView):
    """Создание продукта"""
    serializer_class = ProductSerializer
    permission_classes = [IsActiveUser]


class ProductUpdateApiView(generics.UpdateAPIView):
    """Редактирование продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class ProductListApiView(generics.ListAPIView):
    """Список продуктов"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyApiView(generics.DestroyAPIView):
    """Удаление продукта"""
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsActiveUser]


class LinkCreateApiView(generics.CreateAPIView):
    """Создание звена"""
    serializer_class = LinkSerializer
    permission_classes = [IsActiveUser]


class LinkUpdateApiView(generics.UpdateAPIView):
    """Редактирование звена"""
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]


class LinkRetrieveApiView(generics.RetrieveAPIView):
    """Просмотр звена"""
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]


class LinkListApiView(generics.ListAPIView):
    """Список звеньев"""
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]

    # фильтр по полю страна
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('contact__country',)


class LinkDestroyApiView(generics.DestroyAPIView):
    """Удаление поставщика"""
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    permission_classes = [IsActiveUser]
