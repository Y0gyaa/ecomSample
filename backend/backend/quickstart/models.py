from django.db import models
import uuid

class Product(models.Model):
    CATEGORIES = {
        "Clo": "Clothes",
        "Toi": "Toilettries",
        "Kit": "Kithen",
        "Fur": "Furniture",
        "Eat": "Eatables",
    }
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255,blank=False,null=False)
    description = models.TextField()
    in_stock = models.BooleanField(default=True)
    available_stock = models.BigIntegerField(blank=False,null=False)
    price = models.BigIntegerField(blank=False, null=False)
    category = models.CharField(max_length=3,choices=CATEGORIES)
    image = models.URLField()

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.URLField()
    products_count = models.PositiveIntegerField()

    def __str__(self):
        return self.name


