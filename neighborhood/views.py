from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from . models import *
from django.views import generic

@login_required(login_url='/accounts/login/')
def home(request):
    mylocs = Myloc.objects.all()
    return render(request, 'home.html',{"mylocs":mylocs,})

@login_required(login_url='accounts/login/')
def add_profile(request):
    current_user = request.user
    profile = Profile.objects.filter(id = current_user.id)
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            caption = form.save(commit=False)
            caption.user = current_user
            caption.save()
            return redirect('myprofile')
    else:
        form = NewProfileForm()
    return render(request, 'edit.html', {"form":form})    

