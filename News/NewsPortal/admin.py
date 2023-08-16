from django.contrib import admin
from .models import Post, Category, PostCategory

# admin.site.register(Post)
# admin.site.register(Category)
# admin.site.register(PostCategory)


class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [PostCategoryInline]
    list_display = ('title', 'text', 'author',
                    'categoryType', 'dateCreation', 'rating')
    list_filter = ('categoryType', 'postCategory__name')
    search_fields = ('title', 'text', 'author__name', 'postCategory__name')
    ordering = ('-dateCreation',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
