from django.db import models
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField
from markdownx.utils import markdown

# Category 클래스 구현
# unique=True 전체 테이블에 해당 categoryName은 딱 1개만 만들어지도록 구현됩니다
# slugField : url로 통신하는 Django의 통신방식에 걸맞게 입력한 값이 URL화 되도록 자동으로 변경해줍니다
# 특수문자 에러처리, allow_unicode=True를 걸어두면 한국어 등 영어 외 언어도 사용 가능
class Category(models.Model):
    categoryName = models.CharField(max_length=30, unique=True) 
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.categoryName

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    # class Meta - 이 클래스를 사용하기 위한 간단한 지시나 설명을 넣어주는 class
    # 데이터의 '메타' 데이터와 같은 뜻입니다.
    class Meta:
        verbose_name_plural = 'categories'


class Tag(models.Model):
    tagName = models.CharField(max_length=30, unique=True) 
    slug = models.SlugField(max_length=30, unique=True, allow_unicode=True)

    def __str__(self):
        return self.tagName

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'


# Create your models here. 
# DB의 테이블을 좀더 쉽게 꺼내오기 위해 클래스 형식으로 바꿔주는 기능
class Post(models.Model):
    # 게시글에 필요한 필드: Primary Key, 제목, 내용, 작성일, 수정일, 작성자
    title = models.CharField(max_length=50)
    content = MarkdownxField()

    # upload_to= 경로
    # 어딘가 똑같은 폴더에 저장해주면 좋겠습니다
    # warm cold - 출신/년/월/일 경로로 처음에 지정을 해줄게요
    # blank=True : SQL 쿼리문으로 변환시 Null 가능(Nullable)한 필드를 만드는 옵션
    header_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now=True)  # 값을 변경할 수 있음. default 값으로 현재시간이 찍혀있음 
    
    # 작성자 - 외래키로 참조
    # CASCADE : User를 삭제하면 관련있는 모든 현재 테이블의 데이터 삭제
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # blank=True 글작성시 옵서녈 필드
    #  on_delete=models.SET_NULL, null=True 해당 필드와 걸려있는 다른 테이블의 키가 삭제될 때 None을 넣어줘
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) 
    # 다대다 관계는 ManyToManyField를 통해 관계를 맺어줍니다
    tag = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f'[[{self.pk}] {self.title}            by {self.author}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_extension(self):
        return f'{self.file_upload}'.split('.')[-1]

    def get_content_markdown(self):
        return markdown(self.content)

   # 1. 모델에 함수를 추가해서 그 함수로 ORM을 뽑아낸다
   # 우리 의도: 전체 객체를 불러와서 그 중에 가장 최신글의 제목 뽑아내기
    def first_post_query(self):
        return Post.objects.all().last().title

# M - Comment  
class Comment(models.Model):
    # 게시글에 필요한 필드: Primary Key, 제목, 내용, 작성일, 수정일, 작성자
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now=True)  # 값을 변경할 수 있음. default 값으로 현재시간이 찍혀있음 
    # 글이 삭제되었을 때 댓글은 어떻게 남아있어야 할까 - CASCADE
    # CASCADE : User를 삭제하면 관련있는 모든 현재 테이블의 데이터 삭제
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 사용자가 탈퇴했을 때 댓글은 어떻게 남아있어야 할 것이냐 - CASCADE
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.author} / {self.content}]'

    def get_absolute_url(self):
        return f'{self.post.get_absolute_url()}#comment-{self.pk}' # #을 단 이유 : html에서 id를 의미하기 때문

    def get_avatar_url(self):
        if self.author.socialaccount_set.exists():
            return self.author.socialaccount_set.first().get_avatar_url()
        else:
            return f'https://picsum.photos/50/50/'