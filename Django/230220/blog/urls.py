from django.urls import path, include
from . import views

# 전체 서비스에 지금 이 앱을 blog라고 부르기로 약속하는 것
app_name = "blog"
# 각 앱에 이름이 겹치는 파일 혹은, url이 겹치는 주소가 있을 수 있습니다.
# 그때 app_name : name 순으로 url을 호출해주시면
# 겹치는 파일명에도 불구하고 별개의 자리를 절대경로화해서 접근할 수 있습니다.

# blog 앱 내부 경로를 지정하는 부분
urlpatterns = [
    path('', views.BlogHome.as_view(paginate_by=5), name="home"),
    # paginate_by=개수: 속성들은 urls.py에서 호출할 때 아규먼트로 주거나 
    # views.py에서 디폴트 파라메터로 주면 됩니다.
    path('post_list/', views.PostList.as_view(), name="post_list"), # '' : blog 뒤에 달린 주소가 없음을 의미함 
    path('<int:pk>/', views.PostDetail.as_view()),
    path('about/', views.about_me, name="about_me"), # name="별명" // Alias
    path('contact/', views.contact, name="contact"),  
    # "blog" 라는 app의 "contact" 라는 별명으로 주소/blog/contact/를 호출할 수 있게 됩니다
    path('category/<str:slug>/', views.category_posts),
    path('tag/<str:slug>/', views.tag_posts, name="tag"),
    # path('index2/', views.index2)  # 주소/blog/index2
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>', views.PostUpdate.as_view()),
    path('<int:pk>/new_comment/', views.new_comment),

    path('delete_comment/<int:pk>/', views.delete_comment),
    path('update_comment/<int:pk>/', views.CommentUpdate.as_view()),
    path('search/<str:q>/', views.PostSearch.as_view()),
    
    path('logout/', views.logout, name='logout'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update')

]

