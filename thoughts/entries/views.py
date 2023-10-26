from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from .models import User, DiaryEntry
from .forms import DiaryEntryForm


def index(request):
    if request.user.is_authenticated:
        entries = DiaryEntry.objects.filter(user=request.user)
        return render(request, "entries/index.html", {'entries': entries})
    else:
        return HttpResponseRedirect(reverse("login"))

@login_required
def diary_list(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'entries/diary_list.html', {'entries': entries})

@login_required
def create_diary_entry(request):
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm()
    return render(request, 'entries/diary_entry_form.html', {'form': form})

@login_required
def edit_diary_entry(request, pk):
    entry = DiaryEntry.objects.get(pk=pk)
    if entry.user != request.user:
        return redirect('diary_list')

    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('diary_list')
    else:
        form = DiaryEntryForm(instance=entry)
    return render(request, 'entries/diary_entry_form.html', {'form': form}) 

@login_required
def delete_diary_entry(request, pk):
    entry = DiaryEntry.objects.get(pk=pk)
    if entry.user != request.user:
        return redirect('diary_list')
    entry.delete()
    return redirect('diary_list')   

def favorite_add(request, pk):
    entry = DiaryEntry.objects.get(pk=pk)
    if entry.favorites.filter(pk=request.user.pk).exists():
        entry.favorites.remove(request.user)
    else:
        entry.favorites.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def favorite_list(request):
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'entries/favorite_list.html', {'entries': entries})


def login_view(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
    
    elif request.method == "POST":
        
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "entries/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "entries/login.html")
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("index"))
    
    elif request.method == "POST":
        
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "entries/register.html", {
                "message" : "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "entries/register.html", {
                "message" : "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "entries/register.html")
