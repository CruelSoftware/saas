from django.contrib.auth import  authenticate, get_user_model, login
from django.shortcuts import render

User = get_user_model()


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if all([username, password]):
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request=request, user=user)
                print("Login here!")
    return render(request, "auth/login.html", {})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # username_exists_qs = User.objects.filter(username__iexact=username).exists()
        # email_exists_qs = User.objects.filter(emial__iexact=email).exists()
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except:
            pass

    return render(request, "auth/register.html", {})
