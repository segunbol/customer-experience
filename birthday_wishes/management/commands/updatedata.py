from django.core.management.base import BaseCommand
import pandas as pd
from birthday_wishes.models import Customer, Group


class Command(BaseCommand):
    help = 'import booms'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        df= pd.read_csv('Update_Data_Router.csv')
        for  ERP_NO, NAME,  PHONE_NO_1, PHONE_NO_2, EMAIL_PERSONAL, SLUG, GROUP_ID, DATE_OF_BIRTH,  GENDER, LOCATION in zip( df.Erp_no, df.Name, df.Phone_No_1,df.Phone_No_2, df.Email_personal,df.Slug, df.Group_id, df.Date_of_birth, df.Gender, df.Location):
            models=Customer( name=NAME, gender=GENDER, slug=SLUG, erp_no=ERP_NO, personal_email=EMAIL_PERSONAL, group_id=GROUP_ID, phone_no_1=PHONE_NO_1,phone_no_2=PHONE_NO_2, location=LOCATION, date_of_birth=DATE_OF_BIRTH)
            models.save()