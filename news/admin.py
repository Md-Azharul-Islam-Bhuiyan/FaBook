from django.contrib import admin
from .models import News, NewsCategory

class NewsCategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug': ('name',), }

admin.site.register(News)
admin.site.register(NewsCategory, NewsCategoryAdmin)
