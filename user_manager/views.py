from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.contrib import auth
from django.contrib.auth.models import User
from .form import LoginForm, JoinForm

def login_api(request):
    template = get_template('login_form.html')
    context = {'login_form': LoginForm()}
    context.update(csrf(request))

    return HttpResponse(template.render(context))

def login_validate_api(request):
    login_form_data = LoginForm(request.POST)

    if login_form_data.is_valid():
        user = auth.authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])

        if user is not None:
            if user.is_active:
                auth.login(request, user)

                return redirect('/board/')
        else:
            return HttpResponse('There is no user or the wrong password was pressed.')
    else:
        return HttpResponse('The login form is abnormal.')


    return HttpResponse('This is an unknown error.')


def join_api(request):
    # POST로 넘어온 데이터에 대해서는 회원 가입 로직을 처리
    if request.method == 'POST':
        form_data = JoinForm(request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            return redirect('/user/login/')
    else:
        #GET 요청이면 빈 Form을 만듬.
        form_data = JoinForm()

    template = get_template('join_page.html')

    context = {'join_form': form_data}
    context.update(csrf(request))

    return HttpResponse(template.render(context))
