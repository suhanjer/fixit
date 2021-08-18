from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from django.core.files.storage import FileSystemStorage

from django import forms

class IssueForm(forms.ModelForm):
    author = forms.IntegerField(label="Author")
    title = forms.CharField(label="Title")
    description = forms.CharField(label="Description")
    latitude = forms.FloatField(label="latitude")
    longitude = forms.FloatField(label="longitude")

    class Meta:
        model = Issue
        fields = ('author', 'title', 'description', 'image')

# Create your views here.
def index(request):
    return render(request, "fix/index.html")

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "fix/login.html", {
                "message": "Invalid username and/or password"
            })

    else:
        return render(request, "fix/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        if password != confirmation:
            return render(request, "fix/registration.html", {
                "message": "passwords don't match"
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "fix/register.html", {
                "message": "Username is already taken."
            })

        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "fix/register.html")

def points(request):
    data = Issue.objects.all()
    points = []
    for i in data:
        points.append([i.latitude, i.longitude, f'{i.title}'])
    return JsonResponse(points, safe=False)

def add_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        if form.is_valid():
            #title = form.cleaned_data["title"]
            #description = form.cleaned_data["description"]
            #latitude = float(form.cleaned_data["latitude"])
            #longitude = float(form.cleaned_data["longitude"])


            form.cleaned_data["author"] = request.user
            print('befor save')
            form.save()
            print('after save')
            img_object = form.instance
            print('img_object')

        #issue = Issue(author=request.user, title=title, description=description, status='N', latitude=latitude, longitude=longitude)
        #issue.save()
        return HttpResponseRedirect(reverse("issue_page", args=[issue.id]))
    else:
        return render(request, "fix/add_issue.html", {
            "form": IssueForm(),
        })

def issue_page(request, issue_id):
    issue_data = Issue.objects.get(pk=issue_id)
    print(issue_data.image)
    return render(request, "fix/issue_page.html", {
        "issue_data": issue_data,
    })
