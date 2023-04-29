from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    photo = models.ImageField(upload_to='media/authors')


class Genre(models.Model):
    name = models.CharField(max_length=32)


class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.CharField(max_length=512)
    page_count = models.IntegerField(default=0)
    public_date = models.DateField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books')
    image = models.ImageField(upload_to='media/books')


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Purchase(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class PurchaseItem(models.Model):
    purchase = models.ForeignKey(
        Purchase, on_delete=models.CASCADE, related_name='items')
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
