from django.contrib import admin
from blogs.models import Category,Post
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # list_display=['Category_id','title','description','urls','image','date']
    search_fields=('title',)

class PostAdmin(admin.ModelAdmin):
    # list_display=['Post_id','title','content','urls','Category','image','date']
    search_fields=('title',)

    
    class Media:
        js=('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)


admin.site.register(Category,CategoryAdmin)

admin.site.register(Post,PostAdmin)




