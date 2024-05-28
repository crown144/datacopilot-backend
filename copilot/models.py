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

class Authors(models.Model):
    authorid = models.AutoField(db_column='AuthorID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    birthdate = models.DateField(db_column='Birthdate', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authors'
        

class Books(models.Model):
    bookid = models.AutoField(db_column='BookID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255)  # Field name made lowercase.
    authorid = models.ForeignKey(Authors, models.DO_NOTHING, db_column='AuthorID', blank=True, null=True)  # Field name made lowercase.
    publishedyear = models.TextField(db_column='PublishedYear', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    genre = models.CharField(db_column='Genre', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'books'
        

class Loans(models.Model):
    loanid = models.AutoField(db_column='LoanID', primary_key=True)  # Field name made lowercase.
    bookid = models.ForeignKey(Books, models.DO_NOTHING, db_column='BookID', blank=True, null=True)  # Field name made lowercase.
    memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='MemberID', blank=True, null=True)  # Field name made lowercase.
    loandate = models.DateField(db_column='LoanDate')  # Field name made lowercase.
    returndate = models.DateField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loans'


class Members(models.Model):
    memberid = models.AutoField(db_column='MemberID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=255)  # Field name made lowercase.
    joindate = models.DateField(db_column='JoinDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'members'