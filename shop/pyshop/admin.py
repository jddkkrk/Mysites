from django.contrib import admin

from .models import Product, Review

class ProuctAdmin(admin.ModelAdmin):
    pass
    

class ReviewAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Product, ProuctAdmin)

admin.site.register(Review, ReviewAdmin)