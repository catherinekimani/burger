from django.contrib import admin
from .models import Profile,Product
from django.utils.html import format_html
# product admin
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price']
    
    def image_tag(self, obj):
        return format_html('<img src="{}"  height="380px" />'.format(obj.image.url))
    image_tag.short_description = 'Product Image Preview'
    readonly_fields = ['image_tag']
# Register your models here.
admin.site.register(Profile)
admin.site.register(Product,ProductAdmin)