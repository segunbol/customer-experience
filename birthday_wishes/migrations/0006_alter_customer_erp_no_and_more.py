# Generated by Django 4.1 on 2022-08-25 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes', '0005_alter_customer_erp_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='erp_no',
            field=models.IntegerField(default=' ', max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='ippis_no_oracle_no_staff_id',
            field=models.CharField(default=' ', max_length=10, unique=True),
        ),
    ]
