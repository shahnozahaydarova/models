from django.contrib import admin
from .models import Post,Colors,Narx

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name',)



admin.site.register(Colors)
admin.site.register(Narx)