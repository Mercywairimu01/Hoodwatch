from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib import messages
from django.views.generic import TemplateView,UpdateView,DeleteView

# Create your views here.
def index(request):
    hood = NeighbourHood.objects.all()
    hood =hood[::-1]
    return render(request,'index.html',{ 'hood':hood})

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

def user_profile(request, id):
   try:
     user_detail = Profile.objects.get(id=id)
     current_post = Post.user_post(user_detail.username)
     if request.user.username == str(user_detail.username):
       return redirect('profile')
     else:
       return render(request, 'userprofile.html', {'userdetail':user_detail, ' current_post': current_post})
   except Profile.DoesNotExist:
      return HttpResponseRedirect(" Sorry the Page You Looking For Doesn't Exist.")
  
def create_post(request):
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form=PostForm()
    return render(request,'post_form.html',{'form':form})

def display_post(request):
    posts=Post.objects.all()
    return render(request, 'single_hood.html',{'posts':posts})

def business(request):
    if request.method == 'POST':
        form=BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    
    else:
        form=BusinessForm()
    return render(request,'business_form.html',{'form':form})

def business_details(request):
    business=Business.objects.all()
    return render(request, 'single_hood.html',{'business':business})

def create_neighborhood(request):
    if request.method == 'POST':
        form=NeighborhoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood=form.save(commit=False)
            hood.admin=request.user.profile
            hood.save()
            return redirect('index')
    
    else:
        form=NeighborhoodForm()
    return render(request,'hood.html',{'form':form})


def display_hood(request,hood_id):
    hood=NeighbourHood.objects.get(id=hood_id)
    business=Business.objects.filter(neighbourhood=hood)
    posts=Post.objects.filter(hood_id=hood)
    posts = posts[::-1]
    params = {
        'hood': hood,
        'business': business,
        'posts': posts
    }
    return render(request, 'single_hood.html', params)

class UpdateHood(UpdateView):
    template_name='update.html'
    model=NeighbourHood
    fields ='__all__'
    success_url =reverse_lazy('all')
    
class DeleteHood(DeleteView):
    template_name='delete.html'
    model=NeighbourHood
    fields='__all__'
    success_url=reverse_lazy('index')    

 
def search_business(request):
    if 'search' in request.GET and request.GET['search']:
        search_name=request.GET.get('search')
        search_results=Business.search_business(search_name)
        return render(request, 'search.html', {'search_results': search_results,'search_name': search_name})

    else:
        return redirect('index')
    
