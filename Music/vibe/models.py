from django.db import models

class VibeAdmin(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "musicapitable"

class Register(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    address = models.CharField(max_length=30, blank=False)
    email = models.CharField(max_length=45, blank=False, unique=True)
    phno = models.CharField(max_length=15, blank=False, unique=True)
    username = models.CharField(max_length=30, blank=False, unique=True)
    password = models.CharField(max_length=12, blank=False)

    class Meta:
        db_table = "musicviberegister_table"

class VibePackages(models.Model):
    musicid = models.AutoField(primary_key=True)
    musiccode = models.CharField(max_length=10, blank=False)
    musictitle = models.CharField(max_length=30, blank=False)
    musicPackage = models.CharField(max_length=30, blank=False)
    musicdescription = models.CharField(max_length=35, blank=False)

    class Meta:
        db_table = "Package_table"


class Packages:
    pass



