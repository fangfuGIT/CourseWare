from django.shortcuts import render

# Create your views here.


from apps.forms import UserLogin
from django.shortcuts import render
from django.contrib import auth
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username:
            return render(request, 'login.html', {'error': '用户名不能为空'})
        if not password:
            return render(request, 'login.html', {'error': '密码不能为空'})
        user = auth.authenticate(username=username, password=password)
        if user:
            return render(request, 'success.html', {'username': username})
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})


def login2(request):
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                return render(request, 'success.html', {'username': username})
            else:
                return render(request, 'login2.html', {'error': '用户名或密码错误'})
    else:
        form = UserLogin()
        return render(request, 'login2.html', {'form': form})


def about(request):
    return render(request, "about.html")


class about2(TemplateView):
    template_name = 'about.html'


class DefineLoginView(LoginView):
    template_name = 'login2.html'

    def form_valid(self, form):
        user = form.get_user()
        return render(self.request, 'success.html', {'username': user})

