from django.db import models
# Create your models here.
class MarketPlace(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.CharField(max_length=200, blank= True)
    product_image = models.ImageField('Upload Image')
    
    def __str__(self):
        return self.product_name + self.product_description
    
    def price(self):
        return "%s"  % self.product_price   