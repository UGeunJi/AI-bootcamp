from django.contrib import admin
from .models import Post, Category, Tag, Comment  # 현재 경로의 models.py 안에 있는 Post를 가져다 쓰겠음 
from markdownx.admin import MarkdownxModelAdmin


# Register your models here.
admin.site.register(Post, MarkdownxModelAdmin)

# 왜 Comment는 Post와 함께 관리되지 않을까요 
admin.site.register(Comment)
# prepopulated_fields 
# categoryName input 필드에 들어오는 값을 slug 필드에 URL에서 사용할 수 있는 방식으로 옮겨서 넣어줘서 필터링해주는 파라미터
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categoryName', )}

admin.site.register(Category, CategoryAdmin)
# admin.site.register(Category)

# 최종적으로 admin에서 Tags 항목을 우리가 손볼 수 있어야 할 거고요 
# 그래서 나온 태그를 post_detail.html에서 출력되도록 만들어주세요

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('tagName', )}


admin.site.register(Tag, TagAdmin)