from django.contrib import admin
from django.utils.html import format_html

from networkapp.models import Product, Link, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'model', 'release_data',)
    list_filter = ('title',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'country', 'city', 'street', 'house_number',)
    list_filter = ('city',)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'supplier', 'supplier_debt', 'contact', 'view_link', 'contact_city_fnc')
    list_filter = ('contact__city',)
    actions = ['debt_delete']

    def contact_city_fnc(self, obj):
        return obj.contact.city
    def view_link(self, obj):
        """Ссылка на поставщика"""
        return format_html('<a href="{}">просмотр поставщика</a>', obj.get_absolute_url())

    view_link.allow_tags = True
    view_link.short_description = 'cсылка на поставщика'

    @admin.action(description='удалить задолженность поставщика')
    def debt_delete(self, request, queryset):
        """Удаление задолженности поставщика"""
        selected_objects = queryset.update(supplier_debt=0)
