from django.db import models

# Create your models here.
# Post라는 class를 만들고, 속성으로 제목, 내용, 작성일, 수정일
# Object Related Mapping (ORM) - 대부분의 웹 프레임워크가 제공하는 기능 
# 모델에 class 형태로 데이터의 구조를 집어넣으면 
# 중간에서 table 형태(SQL 쿼리로 변환해서)로 저장해주는 것
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    # 둘 다 한번 올라가면 static 파일이니까 하나의 경로에 관리하고 싶어요
    # 보통 날짜, 시간을 폴더경로로 많이 씀 년/월/일
    # blog/images/년/월/일
    # blog/field/년/월/일
    # blank=True - 쿼리로 변환될 때 Null 허용
    header_img = models.ImageField(upload_to='blog/images/%Y/%m/%d', blank=True)
    file_upload = models.FileField(upload_to='blog/images/%Y/%m/%d', blank=True)
    # 처음 만들어진 시간
    created_at = models.DateTimeField(auto_now_add=True) # , auto_now_add=False,
    # update가 된 시간으로 계속 갱신됨
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return  f'[{self.pk}] {self.title}'

    # 실행할 때마다 해당 경로의 절대경로를 만드는 함수 생성
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'