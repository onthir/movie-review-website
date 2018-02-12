from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify

# Create your tables here. models are the tables of database
'''
simply to create a table, we create a class
class tablename(models.Model)
'''
class Movie(models.Model):
    # here are the columns of the table
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    released_date = models.DateField(default=None)
    director = models.CharField(max_length=150)
    cast = models.CharField(max_length=250)
    image = models.URLField(max_length=1000)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.title

    # auto generating the slug
    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Movie.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    # saving the slug
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save()

# table for the movie reviews
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField(max_length=750)
    review_date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def __str__(self):
        return self.user.username