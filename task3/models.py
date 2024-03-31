from django.db import models


class Product(models.Model):
    price = models.DecimalField(max_digits=54, decimal_places=2)
    margin = models.DecimalField(max_digits=54, decimal_places=2)
    package_code = models.CharField(max_length=128)

    # Encrypted fields
    encrypted_price = models.CharField(max_length=256)
    encrypted_margin = models.CharField(max_length=256)
    encrypted_package_code = models.CharField(max_length=256)
