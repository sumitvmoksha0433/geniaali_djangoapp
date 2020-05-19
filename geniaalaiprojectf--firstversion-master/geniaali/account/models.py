from django.db import models
from django.conf import settings


class Currency(models.Model):
    currency_id = models.IntegerField(primary_key=True)
    currency_type = models.CharField(max_length=30)

    class Meta:
        db_table = "p_currency"

    def __str__(self):
        return self.currency

class Currency_type(models.Model):
    currency_type_id = models.IntegerField(primary_key=True)
    currency_type = models.CharField(max_length=30)
    

    class Meta:
        db_table = "p_currency_type"

    def __str__(self):
        return self.currency_type

class Company_type(models.Model):
    company_type_id = models.IntegerField(primary_key=True)
    company_type = models.CharField(max_length=30)
    

    class Meta:
        db_table = "p_company_type"

    def __str__(self):
        return self.company_type
class office(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=30)


    class Meta:
        db_table = "p_office"

    def __str__(self):
        return self.office

class business_category(models.Model):
    business_category_id = models.IntegerField(primary_key=True)
    business_category = models.CharField(max_length=30)
    
    class Meta:
        db_table = "p_business_category"

    def __str__(self):
        return self.business_category

class business_sub_category(models.Model):
    business_category_id = models.IntegerField(primary_key=True)
    business_sub_category = models.CharField(max_length=30)
    #business_category_id= models.
    
    class Meta:
        db_table = "p_business_sub_category"

    def __str__(self):
        return self.business_sub_category


class socail_site(models.Model):
    pass
    # business_category_id= models.

    class Meta:
        db_table = "p_social_sites"

#    def __str__(self):
#        return self.business_sub_category





class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=30)
    shortname = models.CharField(max_length=30)

    class Meta:
        db_table = "p_country"

    def __str__(self):
        return self.country                                                                
class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.CharField(max_length=30)

    class Meta:
        db_table = "p_state"

    def __str__(self):
        return self.state


class City(models.Model):
    # country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=30)

    class Meta:
        db_table = "p_city"

    def __str__(self):
        return self.city


class Location(models.Model):
    location_id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.CharField(max_length=30)

    class Meta:
        db_table = "p_location"

    def __str__(self):
        return self.location


class Person(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "p_person"


class Profile(models.Model):
    GENDER = (('male', 'Male'), ('female', 'Female'),)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    months = models.CharField(max_length=250)
    year = models.CharField(max_length=250)
    mobile = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    nickname = models.CharField(max_length=250)
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    nickname = models.CharField(max_length=250)
    # List of the Country
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    companytype = models.ForeignKey(Company_type, on_delete=models.CASCADE)
    website = models.URLField(max_length=250)
    street_address = models.CharField(max_length=250)
    pincode = models.CharField(max_length=250)
    twitter = models.CharField(max_length=250)
    youtube = models.CharField(max_length=250)
    msn = models.CharField(max_length=250)
    business_tag = models.CharField(max_length=250)
    company_founded_months = models.CharField(max_length=250)
    company_founded_year = models.CharField(max_length=250)
    skype = models.CharField(max_length=250)
    local_time = models.CharField(max_length=250)
    company_email = models.CharField(max_length=250)
    categories = models.CharField(max_length=250)
    Pintertest = models.CharField(max_length=250)
    language = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    annual_turn_over = models.CharField(max_length=250)
    year_of_estd = models.CharField(max_length=250)
    keywords = models.CharField(max_length=250)
    linkldn = models.CharField(max_length=250)
    sector = models.CharField(max_length=250)
    businnes_category=models.ForeignKey(business_category, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    currency_type = models.ForeignKey(Currency_type, on_delete=models.CASCADE)
    business_type = models.ForeignKey(business_type, on_delete=models.CASCADE)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
