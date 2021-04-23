from django.shortcuts import render
# from django.contrib.auth.views import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import RedirectView

# Create your views here.

class LoginFormView(LoginView):
    template_name = 'login.html'

    # probar el inicio de sesión activado
    def dispatch(self,request, *args, **kwargs):
        # print(request.user)
        if request.user.is_authenticated:
            return redirect('category_list')
        
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context
