from django.urls import path, include
from . import views

urlpatterns = [
    # path("", include('blog.urls')),
    # path('', views.index), # FBV
    path('', views.PostList.as_view()),  # CBV post_list.html을 기본 템플릿으로 찾게 됩니다
    path('<int:pk>/', views.PostDetail.as_view())
]