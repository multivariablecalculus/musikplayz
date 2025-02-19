from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Song, Request
from .forms import SongForm, RequestForm
from django.contrib.auth.forms import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log in the new user automatically after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')  # Redirect to home after registration
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

@login_required
def home(request):
    songs = Song.objects.all()  # Retrieve all uploaded songs
    if request.user.is_superuser:
        # Render admin-specific home page with delete option
        return render(request, 'music/home_admin.html', {'songs': songs})
    else:
        # Render regular user home page without delete option
        return render(request, 'music/home_user.html', {'songs': songs})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after successful login
        else:
            error = "Invalid username or password"
            return render(request, 'music/login.html', {'error': error})
    else:
        return redirect('register')

    # Logout every time someone accesses the login page
    logout(request)
    return render(request, 'templates/registration/login.html')

@login_required
def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'music/upload_song.html', {'form': form})

def make_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RequestForm()
    return render(request, 'music/make_request.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser)  # Restrict access to superusers
def view_requests(request):
    requests = Request.objects.all()
    return render(request, 'music/view_requests.html', {'requests': requests})

@login_required
@user_passes_test(lambda u: u.is_superuser)  # Restrict access to superusers
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    if request.method == 'POST':
        song.delete()
        return redirect('home')
    return render(request, 'music/confirm_delete.html', {'song': song})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

@login_required
def profile_view(request):
    # Logic to retrieve and display user profile information
    return render(request, 'accounts/profile.html')