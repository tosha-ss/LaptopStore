from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProFileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']




from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import RegisterForm, ProFileForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('laptop_list')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})



def user_login(request):
    from allauth.socialaccount.models import SocialApp
    google_enabled = SocialApp.objects.filter(provider='google').exists()

    next_url = request.POST.get('next') or request.GET.get('next') or ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(next_url or 'laptop_list')
        else:
            return render(request, 'shop/login.html', {
                'error': 'Неверные имя пользователя или пароль',
                'google_enabled': google_enabled,
                'next': next_url,
            })
    return render(request, 'shop/login.html', {'google_enabled': google_enabled, 'next': next_url})







def user_logout(request):
    logout(request)
    return redirect('laptop_list')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProFileForm(request.POST, request.FILES, instance=request.user.proFile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProFileForm(instance=request.user.proFile)
    return render(request, 'shop/profile.html', {'form': form})







