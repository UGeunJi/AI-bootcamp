from .models import Comment
from django import forms
from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User # 이렇게 직접적으로 참고할수는 있으나 권장하지 않는 방법임
from django.contrib.auth import get_user_model


class CommentForm(forms.ModelForm): # 우리가 임의로 만들고 있는 모델 
    
    # 따로 상속받은 CreateView가 아니라 Form을 우리가 만들어서 사용하고 있기 때문에
    # 해당 Form에 대한 데이터를 메타클래스에 심어줍니다 
    class Meta:
        model = Comment
        fields = ('content', )


class CustomUserChangeForm(UserChangeForm) :
    
    class Meta :
        # model = User
        model = get_user_model()
        fields = ('email', 'password')