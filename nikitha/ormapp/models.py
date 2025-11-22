from django.db import models
from django.contrib import admin
class product(models.Model):
    productname=models.CharField(max_length=30)
    category=models.CharField(max_length=10)
    productbrand=models.CharField(max_length=20)
    Dateofpack=models.DateField()
    Dateofdeli=models.DateField()
    price=models.IntegerField()
    productID=models.CharField(primary_key=True,max_length=7)

class productadmin(admin.ModelAdmin):
    list_display=["productID","productname","category","productbrand","Dateofpack","Dateofdeli","price"]
    