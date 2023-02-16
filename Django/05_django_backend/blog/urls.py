from django.urls import path, include
from . import views

# blog 앱 내부 경로를 지정하는 부분
urlpatterns = [
    # paginate_by=개수
    path('', views.PostList.as_view(paginate_by=5)), # '' : blog 뒤에 달린 주소가 없음을 의미함 
    path('<int:pk>/', views.PostDetail.as_view()),
    # path('index2/', views.index2)  # 주소/blog/index2
]

