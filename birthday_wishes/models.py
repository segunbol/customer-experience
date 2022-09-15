from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.urls import reverse

GENDER_CHOICES = (
    (' ',' '),
    ('Male','Male'), 
    ('Female','Female'),
    )

class Group(models.Model):
    group_partner = models.CharField(max_length=150, db_index=True, default="Lagos")
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.group_partner


class Customer(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField( max_length=255,unique=False)
    slug = models.SlugField(max_length=150, unique=False, primary_key=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, default=" ")
    erp_no = models.IntegerField(default= " ", blank=False, unique=False)
    personal_email = models.EmailField(blank=True)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=100)
    phone_no_1 = models.SmallIntegerField()
    phone_no_2 = models.IntegerField()
   

    class Meta:
        verbose_name_plural = "Customers"

    def get_absolute_url(self):
        return reverse("birthday_wishes:customer_page", args=[self.slug])
    

    def __str__(self):
        return self.name

    

