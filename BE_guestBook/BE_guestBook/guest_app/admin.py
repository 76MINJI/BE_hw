from django.contrib import admin
from .models import GuestBook

# Register your models here.
# admin.site.register(GuestBook)
class GuestBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'datetime')

admin.site.register(GuestBook, GuestBookAdmin)