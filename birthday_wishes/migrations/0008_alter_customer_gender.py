# Generated by Django 4.1 on 2022-09-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes', '0007_alter_customer_erp_no_alter_customer_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[(' ', ' '), ('Male', 'Male'), ('Female', 'Female')], default=' ', max_length=10),
        ),
    ]
