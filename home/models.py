from django.db import models

# create your model here/
class Product(models.Model):
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    pub_date = models.DateField()

   