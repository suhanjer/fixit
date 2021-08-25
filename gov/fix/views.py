from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse    
from django.urls import reverse
from django.db import IntegrityError
from .models import *
from django.contrib.auth.decorators import login_required

from django import forms

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('title', 'description', 'latitude', 'longitude', 'image_before')

    def CustomSave(self, user):
        data = self.save(commit=False)
        data.author = user
        data.status = 'N'
        data.save()
        return data

class IssueUpdateForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ('status', 'response', 'image_after')

    def CustomSave(self, user):
        data = self.save(commit=False)
        data.executor = user
        data.save()
        return data

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

#returns coordinates for index page
def points(request):
    data = Issue.objects.all()
    points = []
    for i in data:
        points.append([i.latitude, i.longitude, f'{i.title}', i.id])
    return JsonResponse(points, safe=False)

@login_required
def add_issue(request):
    if request.method == "POST":
        form = IssueForm(request.POST, request.FILES)
        
        if form.is_valid():
            value = form.CustomSave(request.user)
        else:
            print('form is invalid')
        return HttpResponseRedirect(reverse("issue_page", args=[value.id]))
    else:
        return render(request, "fix/add_issue.html", {
            "form": IssueForm(),
        })

def issue_page(request, issue_id):
    issue_data = Issue.objects.get(pk=issue_id)
    comments = issue_data.conversation.all()
    return render(request, "fix/issue_page.html", {
        "issue_data": issue_data,
        "comments": comments,
        "statuses": STATUS,
        "form": IssueUpdateForm(),
    })

def update_coordinates(request, issue_id):
    latitude = request.GET.get("latitude")
    longitude = request.GET.get("longitude")
    issue = Issue.objects.get(pk=issue_id)
    issue.latitude = latitude
    issue.longitude = longitude
    issue.save()
    return HttpResponse("success")

def remove(request, issue_id):
    issue = Issue.objects.get(pk=issue_id)
    if issue.status == 'N':
        issue.delete()
        return HttpResponse("success")
    else:
        return HttpResponse("fail")

def add_comment(request):
    if request.method == "POST":
        issue_id = request.POST["issue_id"]
        issue = Issue.objects.get(pk=issue_id)

        comment = Chat(commenter=request.user, issue=issue, comment=request.POST['new_comment'])
        comment.save()

        return HttpResponseRedirect(reverse('issue_page', args=[issue_id]))

def status_change(request):
    if request.method == "POST":
        issue_id = request.POST['issue_id']

        issue = Issue.objects.get(pk=issue_id)
        form = IssueUpdateForm(request.POST, request.FILES, instance=issue)

        form.CustomSave(request.user)

    return HttpResponseRedirect(reverse("issue_page", args=[issue_id]))

def issues_list(request):
    status = request.GET.get('status')
    if status == 'N':
        issues = Issue.objects.filter(status=status)
        return render(request, "fix/issues_list.html", {
            "issues": issues,
        })
    elif status == 'A':
        issues = Issue.objects.filter(status=status)
        return render(request, "fix/issues_list.html", {
            "issues": issues,
        })
    elif status == 'C':
        issues = Issue.objects.filter(status=status)
        return render(request, "fix/issues_list.html", {
            "issues": issues,
        })
    elif status == 'R':
        issues = Issue.objects.filter(status=status)
        return render(request, "fix/issues_list.html", {
            "issues": issues,
        })
    else:
        issues = Issue.objects.all()
        return render(request, "fix/issues_list.html", {
            "issues": issues,
        })