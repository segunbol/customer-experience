# Generated by Django 4.1 on 2022-09-14 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_wishes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='phone_no',
            new_name='phone_no_1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='tenor',
        ),
        migrations.AddField(
            model_name='customer',
            name='erp_no',
            field=models.IntegerField(default=0000),
        ),
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[(' ', ' '), ('Male', 'Male'), ('Female', 'Female')], default=' ', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='personal_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone_no_2',
            field=models.IntegerField(default=111),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(max_length=150, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_partner',
            field=models.CharField(db_index=True, default='Lagos', max_length=150),
        ),
    ]