from django.contrib import admin
from .models import Group, Customer

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_partner', 'slug']
    prepopulated_fields = {'slug': ('group_partner',)}

@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','group', 'slug', 'gender','date_of_birth', 'erp_no','location','phone_no_1','phone_no_2','personal_email',]
    prepopulated_fields = {'slug': ('name', 'erp_no',)}
