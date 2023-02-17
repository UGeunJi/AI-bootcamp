from django.shortcuts import render  # Function Based View 를 사용했습니다
from .models import Post, Category
from django.views.generic import ListView # 게시판형으로 데이터를 가지고 오는 클래스 
from django.views.generic.detail import DetailView
from django.views.generic import CreateView

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'header_img', 'file_upload', 'category']
    # tag -> #카지노 #카지노_행님_20만원만 unique=True : 여러개 달았을 때 이미 있는 해시태그는 더 등록되지 않도록 
    # author -> 로그인 하는 순간부터 author 는 남아있기 때문에
    # created_at -> 작성되는 순간 자동 등록  
    # updated_at -> 수정되는 순간 자동 등록

class BlogHome(ListView):
    model = Post
    ordering = '-pk' 
    template_name = 'blog/blog_home.html'
    context_object_name = 'posts'

    # ListView를 상속받으면서 전달받은 get_context_data라는 함수를 오버라이딩합니다
    def get_context_data(self, **kwargs): # 함수의 파라미터를 개수 안 정해서 k-v 순으로 만들어 보내겠다
        # 속성명 = 값 -> 파이썬의 namespace에서는 키:밸류 순으로 관리됩니다
        context = super(BlogHome, self).get_context_data(**kwargs)
        context['first_post'] = Post.objects.all().last() # first_post라는 이름으로 하나 더 값을 만들어서 전달할게요
        # 필요한 값들을 ORM으로 뽑아서 가져올 수 있습니다.
        return context


class PostList(ListView):  # post_list 라고 생긴 template과 model을 조합합니다. 
    model = Post
    ordering = '-pk' 
    paginate_by = 5 # n개씩 잘라서 data(record)를 전송해주는 속성. views.py에서도, urls.py도 줄 수 있습니다
    paginate_orphans = 3 # 자투리 101개 있음 -> 5개씩 값을 꺼내오면 마지막 남는 1개(orphan)가 있음...
                        # 디자인 깨지지 않게 5개씩 꺼내올 때 값이 2개 이하이면 마지막 페이지에 걍 붙여버려

    # post_list에 전달할 전체 객체명을 바꿔줍니다.
    context_object_name = 'posts'

    # ListView를 상속받으면서 전달받은 get_context_data라는 함수를 오버라이딩합니다
    def get_context_data(self, **kwargs): # 함수의 파라미터를 개수 안 정해서 k-v 순으로 만들어 보내겠다
        # 속성명 = 값 -> 파이썬의 namespace에서는 키:밸류 순으로 관리됩니다
        context = super(PostList, self).get_context_data(**kwargs)
        context['first_post'] = Post.objects.all().last() # first_post라는 이름으로 하나 더 값을 만들어서 전달할게요
        context['categories'] = Category.objects.all()
        # 그냥 post_list.html에서 미분류의 개수를 세서 숫자를 표기해주기 위한 ORM 쿼리
        context['no_category_post_count'] = Post.objects.filter(category=None).count() 
        # 필요한 값들을 ORM으로 뽑아서 가져올 수 있습니다.
        return context

    
# blog 폴더(앱)에서 post_detail.html로 가고 있는 객체를 posts라고 이름을 변경해보세요
# 해당 변수명으로 받은 객체들에 더해 subject 라는 이름으로 제목 데이터만 전달하는 추가 변수를 달아주세요

class PostDetail(DetailView):  # post_detail 라고 생긴 template과 model을 조합합니다. 
    model = Post
    # context_object_name = 'posts'

    def get_context_data(self, **kwargs): # 함수의 파라미터를 개수 안 정해서 k-v 순으로 만들어 보내겠다
        # 속성명 = 값 -> 파이썬의 namespace에서는 키:밸류 순으로 관리됩니다
        context = super(PostDetail, self).get_context_data(**kwargs)
        # print(context['object']) # 뭐가 들어있나 확인해보세요
        context['subject'] = context['object'].title 
        # 필요한 값들을 ORM으로 뽑아서 가져올 수 있습니다.
        return context

def category_posts(request, slug):
    # 조건문을 완성해주세요 
    # 카테고리가 있으면 아래와 같이 
    if slug == "no_category":
        posts = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        posts = Post.objects.filter(category=category)

    # 카테고리가 없으면 None을 가지고 있는 값을 보냅니다.
    return render(
        request,
        'blog/post_list.html',
        {
            'posts' : posts,
            'categories' : Category.objects.all(),
            'no_category_post_count' : Post.objects.filter(category=None).count()
            # 카테고리 위젯을 잘 완성시키기 위해 만들어야 되는 변수들
            # no_category 글의 개수 세기기 count()
            # Post.objects.filter(category=None)를 호출하도록 urls도 변경해야 할겁니다

        }

    )


def about_me(request):
    return render(
        request,
        'blog/about.html'
    )

def contact(request):
    return render(
        request,
        'blog/contact.html'
    )
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

