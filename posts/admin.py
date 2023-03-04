from django.contrib import admin

# Register your models here.
from posts.models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"] #títulos do menu
    list_editable = ["title"] #editar a linha title
    list_display_links = ["updated"] #link data (updated)
    list_filter = ["updated", "timestamp"] #menu lateral
    search_fields = ["title", "content"] #pesquisa
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)