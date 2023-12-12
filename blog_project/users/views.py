from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .form import UserRegisterForm, UpdateProfileForm, UserUpdateForm
# Create your views here.


def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Your account has been created successfully {username}! , Now you can log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def Profile(request):
    if request.method == 'POST':
        try:
            p_form = UpdateProfileForm(
                request.POST, request.FILES, instance=request.user.profile)
            u_form = UserUpdateForm(request.POST, instance=request.user)
        except:
            p_form = UpdateProfileForm(request.POST, request.FILES)
            u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        else:
            messages.error(request, f'Not updated, something went wrong.!')
            return redirect('profile')
    else:
        try:
            p_form = UpdateProfileForm(instance=request.user.profile)
            u_form = UserUpdateForm(instance=request.user)
        except:
            p_form = UpdateProfileForm()
            u_form = UserUpdateForm(instance=request.user)

    context = {
        'p_form': p_form,
        'u_form': u_form
    }
    return render(request, 'registration/profile.html', context)
