from django import forms

class LoginForm(forms.Form):
    id = forms.CharField(label="ID", max_length=12)
    password = forms.CharField(label="PASSWORD", max_length=12)

class JoinForm(forms.Form):
    id = forms.CharField(label="ID", min_length=4, max_length=12, required=True)
    password = forms.CharField(label="PASSWORD", min_length=6, max_length=12, required=True,
                               widget=forms.PasswordInput, error_messages={'min_length': '최소 %(limit_value)d자 이상 입력해 주세요! (현재 %(show_value)d자)'})
    password_check = forms.CharField(label="PASSWORD(again)", min_length=6, max_length=12, required=True,
                                     widget=forms.PasswordInput, error_messages={'min_length': '최소 %(limit_value)d자 이상 입력해 주세요! (현재 %(show_value)d자)'})
