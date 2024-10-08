from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from mysite.core.models import Post


# Create your views here.
def home(request):
    count = User.objects.count()
    return render(request, 'home.html',{
        'count': count,
    })

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
    })

@login_required
def secret_page(request):
    return render(request, 'secret_page.html')

class SecretPage(LoginRequiredMixin, TemplateView):
    template_name = 'secret_page.html'

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def friends(request):
    return render(request, 'friends.html')

def profile(request):
    return HttpResponse("My Profile")




