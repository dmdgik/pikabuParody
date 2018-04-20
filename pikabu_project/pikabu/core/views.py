from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import login, logout
from core.models import User


# Create your views here.

def main_page(request):

    status = request.user.is_anonymous
    return render(request, 'core/main.html', {'status': status})

class BaseUserCreate(UserCreationForm):

    class Meta:

        model = User
        fields = 'username', 'password1', 'password2'

class RegistrationFormView(FormView):

    form_class = BaseUserCreate
    success_url = reverse_lazy('core:login_page')
    template_name = 'core/registration.html'

    def form_valid(self, form):
        form.save(commit=True)
        return super(RegistrationFormView, self).form_valid(form)






def profile_page(request, name_of_user):

    return render(request, 'core/user.html')

def users_list_page(request):

    return render(request, 'core/user_list.html')

def home_page(request):

    return render(request, 'core/home.html')

class LoginFormView(FormView):

    form_class = AuthenticationForm
    template_name = "core/login.html"
    success_url = "core:main_page"

    def form_valid(self, form):

        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):

    def get(self, request):

        logout(request)
        return HttpResponseRedirect("core:post_best_list")




