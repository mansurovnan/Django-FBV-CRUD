from django.shortcuts import render, redirect
from .models import User

def home(request):
    pass
def user_list(request):
    users = User.objects.all()
    return render(request, "user_list.html", {"users": users})


def create_user(request):
    if request.method == "POST":
        User.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            password=request.POST.get("password"),
            is_active=True if request.POST.get("is_active") else False,
        )

        return redirect("user_list")

    return render(request, "create_user.html")
from django.shortcuts import render, redirect, get_object_or_404
from .models import User


def detail_user(request, id):
    user = get_object_or_404(User, id=id)
    return render(request, "detail_user.html", {"user": user})


def delete_user(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == "POST":
        user.delete()
        return redirect("user_list")

    return render(request, "delete_user.html", {"user": user})