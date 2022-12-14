# Generated by Django 4.1 on 2022-08-11 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_partner', models.CharField(db_index=True, max_length=150)),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Groups',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=False, primary_key=False,default=0, serialize=True, verbose_name='ID',null=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=150, unique=True)),
                ('date_of_birth', models.DateField()),
                ('location', models.CharField(max_length=100)),
                ('phone_no', models.SmallIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('tenor', models.IntegerField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birthday_wishes.group')),
            ],
            options={
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
