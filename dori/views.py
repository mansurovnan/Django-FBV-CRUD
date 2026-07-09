from django.shortcuts import render, redirect, get_object_or_404
from .models import Drug


def home(request):
    return render(request, "index.html")


def drug_list(request):
    drugs = Drug.objects.all()
    return render(request, "list_drug.html", {"drugs": drugs})


def create_drug(request):
    if request.method == "POST":

        Drug.objects.create(
            name=request.POST.get("name"),
            desc=request.POST.get("desc"),
            price=request.POST.get("price"),
            fabric=request.POST.get("fabric"),
            is_active=True if request.POST.get("is_active") else False,
        )

        return redirect("drug_list")

    return render(request, "create_drug.html")


def detail_drug(request, id):
    drug = get_object_or_404(Drug, id=id)
    return render(request, "detail_drug.html", {"drug": drug})


def delete_drug(request, id):
    drug = get_object_or_404(Drug, id=id)

    if request.method == "POST":
        drug.delete()
        return redirect("drug_list")

    return render(request, "delete_drug.html", {"drug": drug})

