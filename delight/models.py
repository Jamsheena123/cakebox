from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address=models.CharField(max_length=200,unique=True)
    phone=models.CharField(max_length=200)


class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.name


class cakes(models.Model):
    name=models.CharField(max_length=200)
    category=models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    options=(
        ("chocolate","chocolate"),
        ("vanilla","vanilla"),
        ("pistachio","pistachio"),
        ("tropical rum","tropical rum"),
        ("pineapple","pineapple"),
        ("red velvet","red velvet") ,
        ("strawberry","strawberry"),    
    )
    flavor=models.CharField(max_length=200,choices=options,default="chocolate") 
    image=models.ImageField(upload_to="images")

    @property
    def varient(self):
        qs=self.cakevarients_set.all()
        return qs
    
    def __str__(self):
        return self.name
    
    
class cakevarients(models.Model):
    cake=models.ForeignKey(cakes,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()  
    
    options=(
        ("1kg","1kg"),
        ("2kg","2kg"),
        ("2.5kg","2.5kg"),
        ("3kg","3kg"),
        ("4kg","4kg"),
        ("5kg","5kg"),
        ("7kg","7kg")
    )
    size=models.CharField(max_length=200,choices=options,default="1kg")    

  
    # @property
    # def offers(self):
    #     current_date=date.today
    #     qs=self.offers_set.all()
    #     qs=qs.filter(due_date__gte=current_date)
    #     return qs
    
    def __str__(self):
        return self.cake.name
    

class offers(models.Model):
    cakevarient=models.ForeignKey(cakevarients,on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    start_date=models.DateTimeField()
    due_date=models.DateTimeField()

class carts(models.Model):
    cakevarient=models.ForeignKey(cakevarients,on_delete=models.DO_NOTHING)  
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("in-cart","in-cart"),
        ("order-placed","order-placed"),
        ("cancellled","cancellled")

    )
    status=models.CharField(max_length=200,choices=options,default="in-cart")
    date=models.DateTimeField(auto_now_add=True)

class orders(models.Model):
    user=  user=models.ForeignKey(User,on_delete=models.CASCADE)
    cakevarient=models.ForeignKey(cakevarients,on_delete=models.CASCADE) 
    options=(
        ("order-placed","order-placed"),
        ("cancelled","cancelled"),
        ("dispatched","dispatched"),
        ("in-transit","in-transit"),
        ("delivered","delivered")

    )  
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    ordered_date=models.DateTimeField(auto_now_add=True)
    expected_date=models.DateTimeField(null=True)
    address=models.CharField(max_length=200)

from django.core.validators import MinValueValidator,MaxValueValidator

class reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cake=models.ForeignKey(cakes,null=True,on_delete=models.SET_NULL) 
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comments=models.CharField(max_length=200)    
