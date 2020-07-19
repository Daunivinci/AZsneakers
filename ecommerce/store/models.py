from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name    = models.CharField(max_length=200)
    color   = models.CharField(max_length=200, default='')
    image   = models.ImageField(null=True, blank=True)
    price   = models.FloatField()
    stock   = models.BooleanField(default=False,null=True, blank=True)
    EU_35   = models.BooleanField(default=False, blank=True)
    EU_35_5 = models.BooleanField(default=False, blank=True)
    EU_36   = models.BooleanField(default=False, blank=True)
    EU_36_5 = models.BooleanField(default=False, blank=True)
    EU_37   = models.BooleanField(default=False, blank=True)
    EU_37_5 = models.BooleanField(default=False, blank=True)
    EU_38   = models.BooleanField(default=False, blank=True)
    EU_38_5 = models.BooleanField(default=False, blank=True)
    EU_39   = models.BooleanField(default=False, blank=True)
    EU_39_5 = models.BooleanField(default=False, blank=True)
    EU_40   = models.BooleanField(default=False, blank=True)
    EU_40_5 = models.BooleanField(default=False, blank=True)
    EU_41   = models.BooleanField(default=False, blank=True)
    EU_41_5 = models.BooleanField(default=False, blank=True)
    EU_42   = models.BooleanField(default=False, blank=True)
    EU_42_5 = models.BooleanField(default=False, blank=True)
    EU_43   = models.BooleanField(default=False, blank=True)
    EU_43_5 = models.BooleanField(default=False, blank=True)
    EU_44   = models.BooleanField(default=False, blank=True)
    EU_44_5 = models.BooleanField(default=False, blank=True)
    EU_45   = models.BooleanField(default=False, blank=True)
    EU_45_5 = models.BooleanField(default=False, blank=True)
    EU_46   = models.BooleanField(default=False, blank=True)
    EU_46_5 = models.BooleanField(default=False, blank=True)
    EU_47   = models.BooleanField(default=False, blank=True)
    EU_47_5 = models.BooleanField(default=False, blank=True)
    EU_48   = models.BooleanField(default=False, blank=True)
    EU_48_5 = models.BooleanField(default=False, blank=True)
    EU_49   = models.BooleanField(default=False, blank=True)
    EU_49_5 = models.BooleanField(default=False, blank=True)
    EU_50   = models.BooleanField(default=False, blank=True)

#    caunter_EU_35   = models.CharField(max_length=2, blank=False)
#    caunter_EU_35_5 = models.CharField(max_length=2)
#    caunter_EU_36   = models.CharField(max_length=2)
#    caunter_EU_36_5 = models.CharField(max_length=2)
#    caunter_EU_37   = models.CharField(max_length=2)
#    caunter_EU_37_5 = models.CharField(max_length=2)
#    caunter_EU_38   = models.CharField(max_length=2)
#    caunter_EU_38_5 = models.CharField(max_length=2)
#    caunter_EU_39   = models.CharField(max_length=2)
#    caunter_EU_39_5 = models.CharField(max_length=2)
#    caunter_EU_40   = models.CharField(max_length=2)
#    caunter_EU_40_5 = models.CharField(max_length=2)
#    caunter_EU_41   = models.CharField(max_length=2)
#    caunter_EU_41_5 = models.CharField(max_length=2)
#    caunter_EU_42   = models.CharField(max_length=2)
#    caunter_EU_43   = models.CharField(max_length=2)
#    caunter_EU_43_5 = models.CharField(max_length=2)
#    caunter_EU_44   = models.CharField(max_length=2)
#    caunter_EU_44_5 = models.CharField(max_length=2)
#    caunter_EU_45   = models.CharField(max_length=2)
#    caunter_EU_45_5 = models.CharField(max_length=2)
#    caunter_EU_46   = models.CharField(max_length=2)
#    caunter_EU_46_5 = models.CharField(max_length=2)
#    caunter_EU_47   = models.CharField(max_length=2)
#    caunter_EU_47_5 = models.CharField(max_length=2)
#    caunter_EU_48   = models.CharField(max_length=2)
#    caunter_EU_48_5 = models.CharField(max_length=2)
#    caunter_EU_49   = models.CharField(max_length=2)
#    caunter_EU_49_5 = models.CharField(max_length=2)
#    caunter_EU_50   = models.CharField(max_length=2)




    def __str__(self):
        return self.name
    @property
    def imageURL(self):
        try:url = self.image.url
        except:
            url = ''
            return url