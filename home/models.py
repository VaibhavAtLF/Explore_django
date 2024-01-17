from django.db import models

# create your model here/
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    pub_date = models.DateField()
    price = models.IntegerField(default = 0)
    # img = models.ImageField(upload_to="home/image.jpg",default="")

class sumit(models.Model):
    name = models.CharField(max_length=50)
    age =models.IntegerField(default = 22)
