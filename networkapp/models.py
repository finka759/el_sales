from django.db import models
from django.urls import reverse

NULLABLE = {'null': True, 'blank': True}


class Product(models.Model):
    """Модель продукта"""
    title = models.TextField(
        max_length=200,
        verbose_name='название'
    )
    model = models.TextField(
        unique=True,
        max_length=200,
        verbose_name='модель'
    )
    release_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата выхода продукта на рынок'
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return f'продукт:{self.title}, модель:{self.model}'


class Contact(models.Model):
    """Модель контактов организации, и ее тип"""
    link_types = (
        ("0", "завод",),
        ("1", "розничная сеть"),
        ("2", "индивидуальный предприниматель"),
    )
    email = models.EmailField(
        unique=True,
        verbose_name='электронная почта',
    )
    country = models.TextField(
        max_length=200,
        verbose_name='страна',
    )
    city = models.TextField(
        max_length=200,
        verbose_name='город',
    )
    street = models.TextField(
        max_length=200,
        verbose_name='улица',
    )
    house_number = models.TextField(
        max_length=8,
        verbose_name='номер дома',
    )
    link_type = models.CharField(
        choices=link_types,
        max_length=1,
        default="0",
        verbose_name='тип организации',
    )

    def __str__(self):
        return f'страна:{self.country}, город:{self.city}, улица:{self.street}, дом:{self.house_number},'

    class Meta:
        verbose_name = 'контакт'
        verbose_name_plural = 'контакты'


class Link(models.Model):
    """Модель звена(связи)"""
    title = models.CharField(
        max_length=200,
        verbose_name="название",
        unique=True,
    )
    supplier = models.ForeignKey(
        'self',
        on_delete=models.PROTECT,
        verbose_name="поставщик",
        **NULLABLE,
    )
    supplier_debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="задолженность перед поставщиком",
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        verbose_name="контакты"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата, время создания связи'
    )
    products = models.ManyToManyField(
        Product,
        verbose_name='продукты',
    )

    def __str__(self):
        return f'название:{self.title}, город:{self.contact.city} задолженность {self.supplier_debt}'

    def get_absolute_url(self):
        if self.supplier_id:
            return reverse('networkapp:link_retrieve', args=[str(self.supplier_id)])

    class Meta:
        verbose_name = 'связь'
        verbose_name_plural = 'связи'
