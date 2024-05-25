# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class Users(models.Model):
    userid = models.BigAutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=6)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'

        1