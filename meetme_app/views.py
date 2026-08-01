from django.shortcuts import render, redirect, get_object_or_404
from .models import Celebrity, Package, WebsiteSettings
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

def admin_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("website_settings", permanent=True)
        else:
            return render(request, "admins/admin_login.html", {"error": "Invalid username or password."})

    return render(request, "admins/admin_login.html")

@login_required
def website_settings(request):
    # if not request.user.is_superuser:
    #     return redirect("admin_login")

    settings = WebsiteSettings.objects.first()

    if request.method == "POST":
        settings.support_link = request.POST.get("support_link")
        settings.support_text = request.POST.get("support_text")
        settings.save()

        return redirect("website_settings")
    return render(request, "admins/settings.html",{
        "settings": settings
    })

@login_required
def change_password(request):

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            return redirect("website_settings")

    else:

        form = PasswordChangeForm(request.user)

    return render(
        request,
        "admins/change_password.html",
        {
            "form": form
        })
    

def admin_logout(request):
    logout(request)
    return redirect("admin_login", permanent=True)

# def dashboard(request):
#     celebrities = Celebrity.objects.all()

#     context = {
#         "celebrities": celebrities,
#     }
    
#     return render(request, "dashboard/dashboard.html", context)

def celebrities(request):
    celebrities = Celebrity.objects.all()

    context = {
        "celebrities": celebrities,
    }
    return render(request, "admins/celebrities.html", context)

def add_celebrity(request):
    if request.method =="POST":
        name = request.POST.get("name")
        venue = request.POST.get("venue")
        photo = request.FILES.get("photo")
        free_text = request.POST.get("free_text")
        date = request.POST.get("date") or None
        time = request.POST.get("time") or None
        Celebrity.objects.create(
            name=name,
            venue=venue,
            photo=photo,
            free_text=free_text,
            date=date,
            time=time
        )
        return redirect("celebrities")
    return render(request, "admins/add_celebrity.html")

def edit_celebrity(request, id):

    celebrity = get_object_or_404(Celebrity, id=id)
    
    if request.method == "POST":
        celebrity.name = request.POST.get("name")
        celebrity.venue = request.POST.get("venue")
        celebrity.free_text = request.POST.get("free_text")
        celebrity.date = request.POST.get("date")
        celebrity.time = request.POST.get("time")

        if request.FILES.get("photo"):
            celebrity.photo = request.FILES.get("c_photo")

        celebrity.save()

        return redirect("celebrities")
    return render(request, "admins/edit_celebrity.html", 
    {
            "celebrity": celebrity
        }
    )

def delete_celebrity(request, id):
    celebrity = Celebrity.objects.get(id=id)
    celebrity.delete()
    return redirect("celebrities")

def packages(request):
    packages = Package.objects.all()

    context = {
        "packages": packages,
    }
    return render(request, "admins/packages.html", context)

def add_package(request):
    celebrities = Celebrity.objects.all()
    if request.method == "POST":
        celebrity = Celebrity.objects.get(
            id=request.POST.get("celebrity")
        )
        Package.objects.create(
            celebrity=celebrity,
            photo = request.FILES.get("photo"),
            package_name=request.POST.get("package_name"),
            price=request.POST.get("price"),
            benefits=request.POST.get("benefits")
        )

        return redirect("packages")

    context = {
        "celebrities": celebrities
    }

    return render(request, "admins/add_package.html", context)

def edit_package(request, id):

    package = get_object_or_404(Package, id=id)
    celebrities = Celebrity.objects.all()
    
    if request.method == "POST":
        package.celebrity_id = request.POST.get("celebrity")
        package.package_name = request.POST.get("package_name")
        package.price = request.POST.get("price")
        package.benefits = request.POST.get("benefits")

        if request.FILES.get("photo"):
            package.photo = request.FILES.get("photo")

        package.save()


        return redirect("packages")
    return render(request, "admins/edit_package.html", 
    {
            "package": package,
            "celebrities": celebrities,
        }
    )

def delete_package(request, id):
    package = Package.objects.get(id=id)
    package.delete()
    return redirect("packages")


# website views

def home(request):
    celebrities = Celebrity.objects.all()

    context = {
        "celebrities": celebrities,
    }
    return render(request, "website/home.html", context)

def celebrity_packages(request, id):
    celebrity = get_object_or_404(Celebrity, id=id)
    packages = celebrity.packages.all()
    return render(request, "website/celebrity_packages.html", 
    {
            "celebrity": celebrity,
            "packages": packages,
        }
    )

def package_detail(request, package_id):
    package = get_object_or_404(Package, id=package_id)
    settings = WebsiteSettings.objects.first()

    return render(
        request,
        "website/package_detail.html",
        {
            "package": package,
            "celebrity": package.celebrity,
            "settings": settings,
        }
    )
