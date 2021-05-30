from django.db import models
from django.contrib.auth.models import User

class Promotion(models.Model):
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    # form = models.TimeField()
    # to = models.TimeField()
    apply = models.CharField(max_length=45)
    value = models.IntegerField()
    atlest = models.IntegerField(blank=True, null=True)
    by = models.CharField(max_length=100)
    #product
    def __str__(self):
        return self.name
class History_promotion(models.Model):
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    # form = models.TimeField()
    # to = models.TimeField()
    apply = models.CharField(max_length=45)
    value = models.IntegerField(blank=True, null=True)
    atlest = models.IntegerField(blank=True, null=True)
    by = models.CharField(max_length=100)
    #product
    def __str__(self):
        return self.name

class Item_in_promotion(models.Model):
    id_history = models.IntegerField()
    Barcode_ID = models.CharField(max_length=13)
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=45)
    Color = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Cost = models.CharField(max_length=45)
    Price = models.CharField(max_length=45)
    VAT = models.CharField(max_length=45)
    Excluding_VAT = models.CharField(max_length=45)

class List_product(models.Model):
    id_promotion = models.IntegerField()
    id_product = models.IntegerField()
    Xory = models.CharField(max_length=1)

class Employee(models.Model):
    id_user = models.IntegerField()
    IDcard = models.CharField(max_length=13)
    Title_Name = models.CharField(max_length=10)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Email = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=10)
    Blood_Type = models.CharField(max_length=5)
    Birthday = models.DateField()
    Ethnicity = models.CharField(max_length=45)
    Nationality = models.CharField(max_length=45)
    Religion = models.CharField(max_length=45)
    Address = models.CharField(max_length=200)
    Maritial_Status = models.CharField(max_length=45)
    Education_Level = models.CharField(max_length=100)
    Emergency_Tel = models.CharField(max_length=10)
    Relationship = models.CharField(max_length=45)
    Father_Name = models.CharField(max_length=45)
    Father_Lastname = models.CharField(max_length=45)
    Father_Career = models.CharField(max_length=45,blank=True, null=True)
    Father_Tel = models.CharField(max_length=45,blank=True, null=True)
    Father_Ethnicty = models.CharField(max_length=45,blank=True, null=True)
    Father_Nationallity = models.CharField(max_length=45,blank=True, null=True)
    Father_Religion = models.CharField(max_length=45,blank=True, null=True)
    Father_Address = models.CharField(max_length=45,blank=True, null=True)
    Mother_Title = models.CharField(max_length=45)
    Mother_Name = models.CharField(max_length=45)
    Mother_Lastname = models.CharField(max_length=45)
    Mother_Career = models.CharField(max_length=45,blank=True, null=True)
    Mother_Tel = models.CharField(max_length=45,blank=True, null=True)
    Mother_Ethnicty = models.CharField(max_length=45,blank=True, null=True)
    Mother_Nationallity = models.CharField(max_length=45,blank=True, null=True)
    Mother_Religion = models.CharField(max_length=45,blank=True, null=True)
    Mother_Address = models.CharField(max_length=45,blank=True, null=True)
    Mother_Nationallity = models.CharField(max_length=45,blank=True, null=True)
    Role = models.CharField(max_length=45)
    status = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    Barcode_ID = models.CharField(max_length=13)
    Name = models.CharField(max_length=100)
    Size = models.CharField(max_length=45)
    Color = models.CharField(max_length=45)
    Type = models.CharField(max_length=45)
    Model = models.CharField(max_length=45)
    Cost = models.IntegerField()
    Price = models.IntegerField()
    VAT = models.IntegerField()
    Excluding_VAT = models.IntegerField()
    id_Promotion = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.name
    
class Member(models.Model):
    Member_ID = models.IntegerField(primary_key=True)
    IDcard = models.CharField(max_length=13)
    Title_Name = models.CharField(max_length=10)
    Firstname = models.CharField(max_length=100)
    Lastname = models.CharField(max_length=100)
    Age = models.CharField(max_length=100)
    Gender = models.CharField(max_length=10)
    Email = models.CharField(max_length=100)
    Phonenumber = models.CharField(max_length=10)
    Birthday = models.DateField()
    Address = models.CharField(max_length=200,blank=True, null=True)
    Point = models.IntegerField()
    status = models.IntegerField()
    
class Product_order(models.Model):
    Date = models.DateField()
    Product_id = models.IntegerField(blank=True, null=True)
    Bill_id = models.IntegerField(blank=True, null=True)
    Employee_id = models.IntegerField(blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Unit_price = models.IntegerField(blank=True, null=True)
    Unit_Cost = models.IntegerField(blank=True, null=True)
    Unit_Tax = models.IntegerField(blank=True, null=True)
    
class Bill(models.Model):
    Date = models.DateField()
    Time = models.TimeField()
    Member_id = models.IntegerField(blank=True, null=True)
    Total = models.IntegerField(blank=True, null=True)
    Quantity = models.IntegerField(blank=True, null=True)
    Employee_name = models.CharField(max_length=100)
    Employee_role = models.CharField(max_length=100)
    Discount = models.IntegerField(blank=True, null=True)
    Receive = models.IntegerField(blank=True, null=True)
    Tax = models.IntegerField(blank=True, null=True)
    Profit = models.IntegerField(blank=True, null=True)
    
class Subscription_fee(models.Model):
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    old_rate = models.IntegerField(blank=True, null=True)
    new_rate = models.IntegerField(blank=True, null=True)
    start_point = models.IntegerField(blank=True, null=True)
    by = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Member_point(models.Model):
    Pay_new = models.IntegerField(blank=True, null=True)
    Is_new = models.IntegerField(blank=True, null=True)
    Use_new = models.IntegerField(blank=True, null=True)
    discout_new = models.IntegerField(blank=True, null=True)
    Pay_old = models.IntegerField(blank=True, null=True)
    Is_old = models.IntegerField(blank=True, null=True)
    Use_old = models.IntegerField(blank=True, null=True)
    discout_old = models.IntegerField(blank=True, null=True)
    by = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Promotion_member(models.Model):
    name = models.CharField(max_length=100)
    types = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    form = models.TimeField()
    to = models.TimeField()
    value = models.IntegerField(blank=True, null=True)
    atlest = models.IntegerField(blank=True, null=True)
    by = models.CharField(max_length=100)
    condition  = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

class Sale(models.Model):
    January = models.IntegerField( null=True)
    February = models.IntegerField( null=True)
    March = models.IntegerField( null=True)
    April = models.IntegerField( null=True)
    May = models.IntegerField(null=True)
    June = models.IntegerField( null=True)
    July = models.IntegerField( null=True)
    August = models.IntegerField( null=True)
    September = models.IntegerField( null=True)
    October = models.IntegerField( null=True)
    November = models.IntegerField( null=True)
    December = models.IntegerField( null=True)



class Profit(models.Model):
    January = models.IntegerField( null=True)
    February = models.IntegerField(null=True)
    March = models.IntegerField(null=True)
    April = models.IntegerField( null=True)
    May = models.IntegerField(null=True)
    June = models.IntegerField(null=True)
    July = models.IntegerField(null=True)
    August = models.IntegerField(null=True)
    September = models.IntegerField(null=True)
    October = models.IntegerField(null=True)
    November = models.IntegerField(null=True)
    December = models.IntegerField(null=True)

    def __str__(self):
        return self.name
