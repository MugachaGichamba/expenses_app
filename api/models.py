from django.db import models

# Create your models here.


class Tenant(models.Model):
    first_name = models.CharField(verbose_name="First Name",
                            max_length=100 )
    last_name = models.CharField(verbose_name="Last Name",
                                 max_length=100)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now=True)


    phone_number = models.CharField(verbose_name="phone number",
                            max_length=12 )
    rent_per_month = models.DecimalField(max_digits=5,
                                         decimal_places=1)

    def __str__(self):
        return self.first_name + " " +self.last_name

        class Meta:
            ordering = ['first_name']
