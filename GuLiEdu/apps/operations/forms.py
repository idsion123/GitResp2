from django import forms
from . import models
import re
class UserAskForm(forms.ModelForm):
    class Meta:
        model=models.UserAsk
        fields='__all__'
        exclude=['add_time']
    def clean_phone(self):
        phone=self.cleaned_data['phone']
        com =re.compile('^1(3[0-9]|4[01456879]|5[0-35-9]|6[2567]|7[0-8]|8[0-9]|9[0-35-9])\d{8}$')
        if com.match(phone):
            return phone
        else:
            raise forms.ValidationError('手机号码不正确')
    # def clean_course(self):
    #     course=self.cleaned_data['course']
class UserCommentForm(forms.Form):
    comment_course=forms.IntegerField(required=True)
    comment_content=forms.CharField(required=True,min_length=1,max_length=300)




