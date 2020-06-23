from django.db import models


class Restaurant(models.Model):
    RestaurantId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    address = models.TextField(max_length=100, unique=True)
    CountryId = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)
    CityId = models.ForeignKey('City', models.DO_NOTHING, db_column='CityId', blank=True, null=True)
    MenuId = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MenuId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'


class Staff(models.Model):
    StaffId = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    birth_date = models.DateField(blank=True)
    email = models.EmailField(max_length=254, blank=True, unique=True)
    phone_number = models.IntegerField(blank=True, unique=True)
    salary = models.DecimalField(max_digits=None, decimal_places=2, blank=True, null=True)
    job_position = models.TextField(max_length=32)
    RestaurantId = models.ForeignKey('Restaurant', models.DO_NOTHING, db_column='RestaurantId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staff'


class Country(models.Model):
    CountryId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'country'


class City(models.Model):
    CityId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    CountryId = models.ForeignKey('Country', models.DO_NOTHING, db_column='CountryId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'city'


class Dish(models.Model):
    DishId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    recipe = models.TextField()
    weight = models.DecimalField(max_digits=None, decimal_places=2)
    price = models.DecimalField(max_digits=None, decimal_places=2)
    MenuId = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MenuId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Menu(models.Model):
    MenuId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    DishId = models.ForeignKey('Dish', models.DO_NOTHING, db_column='DishId', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'menu'
