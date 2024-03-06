from django.db import models

# Create your models here.
class Tag(models.Model):
    value=models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.value

class Product(models.Model):
    product_id=models.CharField(max_length=100)
    product_name=models.CharField(max_length=100)
    product_price=models.DecimalField(decimal_places=2,max_digits=11,default=0)
    is_purchased=True
    product_tags=models.TextField(max_length=1000,default="")
    
    def __str__(self) -> str:
        return str(self.product_id)+' : '+str(self.product_name)
    
class Cart(models.Model):
    cart_id=models.CharField(max_length=100)
    is_active=False
    def __str__(self) -> str:
        return 'Cart: '+ str(self.cart_id)