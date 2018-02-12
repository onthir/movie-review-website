from django.contrib import admin
from .models import Movie, Review

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'released_date', 'director')
    list_filter = ('released_date', 'director')
    search_fields = ('title', 'director')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'review_date')
    list_filter = ('movie', 'review_date')
    search_fields = ['user__username', 'movie__title']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)