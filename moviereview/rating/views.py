from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie, Review
from .forms import MovieAddForm, RegistrationForm, PostForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.
def home(request):
    # getting objects from the database
    movies = Movie.objects.all()

    # search query
    query = request.GET.get('q')
    if query:
        movies = Movie.objects.filter(title__icontains=query)

    context = {
        'movies':movies
    }
    return render(request, 'rating/index.html', context)
# details
def details(request, slug):
    movie = Movie.objects.get(slug=slug)
    # getting the user reviews
    reviews = Review.objects.filter(movie=movie)
    context = {
        'movie': movie,
        'reviews': reviews,
    }
    return render(request, 'rating/details.html', context)

# function to add movie from the html forms
def add_movies(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = MovieAddForm(request.POST or None)
            if form.is_valid():
                form.save()
                # after saving the form
                return redirect("home")
        else:
            form = MovieAddForm(request.POST or None)
        return render(request, 'rating/add-movies.html', {'form': form})
    else:
        return redirect("home")

# updating the movie details
def update_movie(request, slug):
    if request.user.is_superuser:
        movies = Movie.objects.get(slug=slug)
        if request.method == 'POST':
            form = MovieAddForm(request.POST, instance=movies)
            if form.is_valid():
                detail = form.save()
                return redirect("home")
        else:
            form = MovieAddForm(instance=movies)
        return render(request, 'rating/update-movies.html', {'form': form})
    else:
        return redirect("home")

# deleting the movie
def delete_movie(request, slug):
    if request.user.is_superuser:
        movie  = Movie.objects.get(slug=slug)
        movie.delete()
        return redirect("home")
    else:
        return redirect("home")

# registering the user
def register(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST or None)
            if form.is_valid():
                form.save()
                return redirect("home")
        else:
            form = RegistrationForm(request.POST or None)
        return render(request, 'rating/register.html', {'form': form})

# log in 
def login_user(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        if request.method == 'POST':
            # now we get the data from html templates
            username = request.POST.get('username')
            password = request.POST.get('password')

            # authenticating the credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                print("User is notNone") #meaning that the credentials are correct
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    return render(request, 'rating/login.html', {'error-message': 'Your account has been banned.'})
            else:
                return render(request, 'rating/login.html', {'error-message': 'Invalid Username or Password'})
        return render(request, 'rating/login.html')

# logout
def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("home")
    else:
        return redirect("login_user")

# add reviews
def add_review(request, slug):
    if request.user.is_authenticated:
        movie = Movie.objects.get(slug=slug)
        if request.method == 'POST':
            form = PostForm(request.POST or None)
            if form.is_valid():
                rev = form.save(commit=False)
                rev.movie = movie
                rev.user = request.user
                rev.save()
                return redirect("home")
        else:
            form = PostForm(request.POST or None)
        return render(request, 'rating/add-review.html', {'form': form})
    else:
        return redirect("login_user")
# edit the reviews
def edit_review(request, slug, id):
    # permissions are granted to the users who posted the review
    if request.user.is_authenticated:
        movie = Movie.objects.get(slug=slug)
        review = Review.objects.get(movie=movie, id=id)
        if request.user == review.user:
            if request.method == 'POST':
                form = PostForm(request.POST, instance=review)
                if form.is_valid():
                    form.save()
                    return redirect("home")
            else:
                form = PostForm(instance=review)
            return render(request, 'rating/add-review.html', {'form': form})
        else:
            return redirect("home")

    else:
        return redirect("home")

# delete review
def delete_review(request, slug, id):
    if request.user.is_authenticated:
        movie = Movie.objects.get(slug=slug)
        review = Review.objects.get(movie=movie, id=id)
        if request.user == review.user:
            review.delete()
            print("Deleted successfully")
            return redirect("home")
        else:
            return redirect("home")
    else:
        return redirect("login_user")

# creating the user profile
def profile(request, user):
    # get the contents by that user
    username = User.objects.get(username=user)
    
    reviews = Review.objects.filter(user=username)
    context = {
        'reviews':reviews,
        'username': username
    }
    return render(request, 'rating/profile.html', context)