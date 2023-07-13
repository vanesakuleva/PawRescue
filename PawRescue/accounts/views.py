from django.shortcuts import render


# Create your views here.
def login_user(request):
    return render(request, 'home-with-profile.html')


def register_user(request):
    pass


def details_user(request):
    pass


def edit_user(request):
    pass


def delete_user(request):
    pass
