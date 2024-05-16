# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Errorlogs(models.Model):
    errorid = models.BigAutoField(db_column='ErrorID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    errormessage = models.TextField(db_column='ErrorMessage', db_comment='错误信息')  # Field name made lowercase.
    occurredatbigint = models.DateTimeField(db_column='OccurredAtbigint', db_comment='发生时间')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'errorlogs'


class Feedbacks(models.Model):
    feedbackid = models.BigAutoField(db_column='FeedbackID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    feedbackcbigintontent = models.TextField(db_column='FeedbackCbigintontent')  # Field name made lowercase.
    submittedat = models.DateTimeField(db_column='SubmittedAt')  # Field name made lowercase.
    statusbigint = models.CharField(db_column='Statusbigint', max_length=3)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedbacks'


class Helpsupport(models.Model):
    supportid = models.BigAutoField(db_column='SupportID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    issuedesbigintcription = models.TextField(db_column='IssueDesbigintcription', db_comment='问题描述')  # Field name made lowercase.
    submittedat = models.DateTimeField(db_column='SubmittedAt', db_comment='提交时间')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'helpsupport'


class Permissions(models.Model):
    permissionid = models.BigAutoField(db_column='PermissionID', primary_key=True)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=4)  # Field name made lowercase.
    permissiondescription = models.CharField(db_column='PermissionDescription', max_length=255, db_comment='权限描述')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'permissions'


class Queries(models.Model):
    queryid = models.BigAutoField(db_column='QueryID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    querycontent = models.TextField(db_column='QueryContent', db_comment='记录自然语言查询内容')  # Field name made lowercase.
    querytime = models.DateTimeField(db_column='QueryTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'queries'


class Queryhistory(models.Model):
    historyid = models.AutoField(db_column='HistoryID', primary_key=True)  # Field name made lowercase.
    userid = models.PositiveBigIntegerField(db_column='UserID')  # Field name made lowercase.
    queryid = models.ForeignKey(Queries, models.DO_NOTHING, db_column='QueryID')  # Field name made lowercase.
    executiontime = models.DateTimeField(db_column='ExecutionTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'queryhistory'


class Userpermissions(models.Model):
    userid = models.OneToOneField('Users', models.DO_NOTHING, db_column='UserID', primary_key=True)  # Field name made lowercase.
    permissionid = models.ForeignKey(Permissions, models.DO_NOTHING, db_column='PermissionID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userpermissions'


class Users(models.Model):
    userid = models.BigAutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=4)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'
