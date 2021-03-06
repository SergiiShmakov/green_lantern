from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models import Index


class Dealer(models.Model):
    dealer_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=False, unique=True)
    email = models.EmailField(max_length=100, blank=True, null=False, unique=True)
    city_id = models.ForeignKey(to='City', db_column='city', blank=True, null=False, on_delete=models.DO_NOTHING,
                                db_constraint=False)

    class Meta:
        ordering = ('dealer_id',)
        indexes = [Index(fields=('title',))]
        verbose_name = _('Dealer')
        verbose_name_plural = _('Dealers')


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=False)
    country_id = models.ForeignKey(to='Country', db_column='country', blank=True, null=False,
                                   on_delete=models.DO_NOTHING, db_constraint=False)

    class Meta:
        ordering = ('name',)
        indexes = [Index(fields=('name',))]
        verbose_name = _('City')
        verbose_name_plural = _('Cities')

    def __str__(self):
        return self.name


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, blank=True, null=False, unique=True)
    code = models.CharField(max_length=10, blank=True, null=False, unique=True)

    class Meta:
        ordering = ('name',)
        indexes = [Index(fields=('name',))]
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')

    def __str__(self):
        return self.name
