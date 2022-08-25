from django.contrib import admin
from .models import Group, Customer

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ['group_partner', 'slug']
    prepopulated_fields = {'slug': ('group_partner',)}

@admin.register(Customer)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'date_of_birth', 'erp_no','ippis_no_oracle_no_staff_id','location','phone_no', 'start_date', 'end_date', 'tenor']
    prepopulated_fields = {'slug': ('name', 'erp_no',)}
