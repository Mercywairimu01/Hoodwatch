from django.shortcuts import get_object_or_404, render,redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.
def index(request):
    neigh = NeighbourHood.objects.all()
    neigh =neigh[::-1]
    return render(request,'index.html',{ 'neigh':neigh})

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            # password=form.cleaned_data.get('password')

            return redirect('login')
    else:
        form=RegistrationForm()
    return render(request, 'register/registration.html',{'form':form})


def profile(request):
    if request.method == 'POST':
        u_form = UserForm(request.POST, instance=request.user)
        p_form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Account updated!')
            return redirect('profile')
    else:
        u_form = UserForm(instance=request.user)
        p_form = ProfileForm(instance=request.user.profile)
        current_profile = Profile.objects.get(user_id = request.user)
        current_post = Post.user_post(request.user)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'current_profile':current_profile,
        'current_post':current_post,
    }
    return render(request, 'register/profile.html', context)