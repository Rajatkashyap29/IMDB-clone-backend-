from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User


class StreamPlateform(models.Model):
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=150)
    website=models.URLField(max_length=100)
    
    
    def __str__(self):
        return   self.name

class WactchList(models.Model):
    title=models.CharField(max_length=100)
    storyline=models.CharField(max_length=100)
    plateform=models.ForeignKey(StreamPlateform,on_delete=models.CASCADE,related_name="watchlist",null=True, blank=True)
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return   self.title
    
class Review(models.Model):
    review_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    description=models.CharField(max_length=200)
    wactchList=models.ForeignKey(WactchList,on_delete=models.CASCADE,related_name='reviews')
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return str(self.rating)+"   "+ self.wactchList.title
    
    
    
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField() 
    description=models.CharField(max_length=140)
    
    def __str__(self):
        return self.product_name  
    
    
    
    
class DogCategory(models.Model):
    breed=models.CharField(max_length=50)
    about=models.CharField(max_length=150)
    
    def __str__(self):
        return self.breed    
    