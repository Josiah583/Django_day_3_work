from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q 

# Create your models here.
# modules 
# models

class Store(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    tagline = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    def __str__(self) ->str:
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) ->str:
        return self.name

class Products(models.Model):
    # owner
    store = models.ForeignKey(Store, on_delete=models.DO_NOTHING, related_name="products", null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products", null=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=10)
    is_available = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True )
    rating = models.IntegerField()

    def discount(self, discount=20):
        self.price = self.price * (discount/100)
        return self.price
    

    def __str__(self) -> str:
        return f"{self.name},{self.desc} {self.price}"
 
 # decribes the behaviout of your modeln
class Meta:
    ordering = {'name', '-price',}
    verbose_name = 'products'
    constraints = [models.CheckConstraint(check=Q('price__gt=12000'), name="price_gt_12000")]
    





