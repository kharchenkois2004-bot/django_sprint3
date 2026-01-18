from django.contrib import admin
from .models import Category, Location, Post

# Register your models here.
admin.site.register(Category)


class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Location)
admin.site.register(Post)
