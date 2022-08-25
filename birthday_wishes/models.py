from tabnanny import verbose
from tkinter import CASCADE
from django.db import models
from django.urls import reverse



class Group(models.Model):
    group_partner = models.CharField(max_length=150, db_index=True, default="Lagos")
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        verbose_name_plural = "Groups"

    def __str__(self):
        return self.group_partner


class Customer(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    name = models.CharField(('name'),max_length=255)
    slug = models.SlugField((''),max_length=150, unique=True)
    gender = models.CharField(max_length=10, default=" ")
    erp_no = models.IntegerField(default= " ", blank=False, unique=True)
    ippis_no_oracle_no_staff_id = models.CharField(max_length=10,default=" ",blank=False, unique=True)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=100)
    phone_no = models.SmallIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    tenor = models.IntegerField()

    class Meta:
        verbose_name_plural = "Customers"

    def get_absolute_url(self):
        return reverse("birthday_wishes:customer_page", args=[self.slug])
    

    def __str__(self):
        return self.name

    

