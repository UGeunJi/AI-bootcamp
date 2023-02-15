# from django.shortcuts import render  # Function Based View 를 사용했습니다
from .models import Post
from django.views.generic import ListView # 게시판형으로 데이터를 가지고 오는 클래스 
from django.views.generic.detail import DetailView

class PostList(ListView):  # post_list 라고 생긴 template과 model을 조합합니다. 
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):  # post_detail 라고 생긴 template과 model을 조합합니다. 
    model = Post

# Create your views here.
# V (view) - 화면에 출력되는 부분을 책임집니다. 
# def index(request):
#     return render(
#         request, 
#         'blog/index.html'
#     )

# def index2(request):
#     return render(
#         request, 
#         'index2.html'
#     )

