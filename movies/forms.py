from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):  # ModelForm 상속
    class Meta:  # Meta 클래스에 작성할거야
        model = Movie  # 대상 모델을 등록
        fields = '__all__'  # 모델의 필드 중 뭘 활용할건지