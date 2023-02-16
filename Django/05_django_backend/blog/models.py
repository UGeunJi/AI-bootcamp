from django.db import models

# Create your models here. 
# DB의 테이블을 좀더 쉽게 꺼내오기 위해 클래스 형식으로 바꿔주는 기능
class Post(models.Model):
    # 게시글에 필요한 필드: Primary Key, 제목, 내용, 작성일, 수정일, 작성자
    title = models.CharField(max_length=50)
    content = models.TextField()

    # upload_to= 경로
    # 어딘가 똑같은 폴더에 저장해주면 좋겠습니다
    # warm cold - 출신/년/월/일 경로로 처음에 지정을 해줄게요
    # blank=True : SQL 쿼리문으로 변환시 Null 가능(Nullable)한 필드를 만드는 옵션
    header_img = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True)  # 아예 값 자체가 지금 시간으로 입력되어 들어감(우리가 변경할 필요 없음)
    updated_at = models.DateTimeField(auto_now=True)  # 값을 변경할 수 있음. default 값으로 현재시간이 찍혀있음 
    # 작성자는 추후 작성 예정

    def __str__(self):
        return f'[[{self.pk}] {self.title}]'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

   # 1. 모델에 함수를 추가해서 그 함수로 ORM을 뽑아낸다
   # 우리 의도: 전체 객체를 불러와서 그 중에 가장 최신글의 제목 뽑아내기
    def first_post_query(self):
        return Post.objects.all().last().title