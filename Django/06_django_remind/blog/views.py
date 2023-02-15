# from django.shortcuts import render # FBV에서 사용하는 모듈
# from .models import Post
from django.views.generic import ListView
from django.views.generic.detail import DetailView  # 더보기 클릭시 싱글페이지 확인
from .models import Post

class PostDetail(DetailView):
    model = Post

# 2) Class Based View 방식 
class PostList(ListView):
    model = Post
    ordering = '-pk'
    # post_list.html이 default Template로 지정되고,
    # 해당 파일에 가는 객체명도 클래스 이름의 snake형(post_list)로 전달됨
    template_name = 'blog/index.html'
    
# Create your views here.
# template과 model을 합쳐서 views로 만드는 파일
# 1) Function Based View 방식
# def index(request):
#     posts = Post.objects.all()

#     return render(
#         request,
#         'blog/index.html',
#         { 'posts': posts }
#     )



