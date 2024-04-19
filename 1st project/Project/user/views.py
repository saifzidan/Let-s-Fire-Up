from django.shortcuts import render, redirect
from .forms import CreateUserForm, UpdateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account has been created for {username}. continue to login"
            )
            return redirect("user:login")
    else:
        form = CreateUserForm()
    context = {"form": form}
    return render(request, "user/register.html", context)


def User_Update(request):
    if request.method == "POST":
        form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid:
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Account has been updated for {username}. continue to login"
            )
            return redirect("user:index")
    else:
        form = UpdateUserForm(instance=request.user)
    context = {"form": form}
    return render(request, "user/update.html", context)


@login_required
def index(request):
    return render(request, "user/index.html")