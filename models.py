# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Car(models.Model):
    carid = models.IntegerField(db_column='CarID', primary_key=True)  # Field name made lowercase.
    carmodel = models.CharField(db_column='CarModel', max_length=255)  # Field name made lowercase.
    carmake = models.CharField(db_column='CarMake', max_length=255)  # Field name made lowercase.
    carseries = models.CharField(db_column='CarSeries', max_length=255)  # Field name made lowercase.
    caryear = models.IntegerField(db_column='CarYear')  # Field name made lowercase.
    carpricenew = models.DecimalField(db_column='CarPriceNew', max_digits=15, decimal_places=2)  # Field name made lowercase.
    carenginesize = models.CharField(db_column='CarEngineSize', max_length=255)  # Field name made lowercase.
    carfuelsystem = models.CharField(db_column='CarFuelSystem', max_length=255)  # Field name made lowercase.
    cartankcapacity = models.CharField(db_column='CarTankCapacity', max_length=255)  # Field name made lowercase.
    carpower = models.CharField(db_column='CarPower', max_length=255)  # Field name made lowercase.
    carseatingcapacity = models.IntegerField(db_column='CarSeatingCapacity')  # Field name made lowercase.
    carstandardtransmission = models.CharField(db_column='CarStandardTransmission', max_length=255)  # Field name made lowercase.
    carbodytype = models.CharField(db_column='CarBodyType', max_length=255)  # Field name made lowercase.
    cardrive = models.CharField(db_column='CarDrive', max_length=255)  # Field name made lowercase.
    carwheelbase = models.CharField(db_column='CarWheelbase', max_length=255)  # Field name made lowercase.
    avaliable = models.IntegerField(db_column='Avaliable')  # Field name made lowercase.
    roadworthy = models.IntegerField(db_column='RoadWorthy')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'car'


class Customer(models.Model):
    customerid = models.AutoField(db_column='CustomerID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=255)  # Field name made lowercase.
    customerphonenumber = models.CharField(db_column='CustomerPhoneNumber', max_length=255)  # Field name made lowercase.
    customeraddress = models.CharField(db_column='CustomerAddress', max_length=255)  # Field name made lowercase.
    customeroccupation = models.CharField(db_column='CustomerOccupation', max_length=255)  # Field name made lowercase.
    customerdob = models.CharField(db_column='CustomerDOB', max_length=255)  # Field name made lowercase.
    customergender = models.CharField(db_column='CustomerGender', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'


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


class Orderrecord(models.Model):
    orderid = models.IntegerField(db_column='OrderID', primary_key=True)  # Field name made lowercase.
    ordercreatedate = models.CharField(db_column='OrderCreateDate', max_length=255)  # Field name made lowercase.
    orderstatus = models.CharField(db_column='OrderStatus', max_length=255)  # Field name made lowercase.
    orderpickupdate = models.DateField(db_column='OrderPickupDate')  # Field name made lowercase.
    orderreturndate = models.DateField(db_column='OrderReturnDate')  # Field name made lowercase.
    customerid = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CustomerID')  # Field name made lowercase.
    carid = models.ForeignKey(Car, models.DO_NOTHING, db_column='CarID')  # Field name made lowercase.
    orderpickupstoreid = models.ForeignKey('Store', models.DO_NOTHING, db_column='OrderPickupStoreID')  # Field name made lowercase.
    orderreturnstoreid = models.ForeignKey('Store', models.DO_NOTHING, db_column='OrderReturnStoreID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderrecord'


class Staff(models.Model):
    staffid = models.AutoField(db_column='StaffID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='UserID', blank=True, null=True)  # Field name made lowercase.
    staffname = models.CharField(db_column='StaffName', max_length=255)  # Field name made lowercase.
    staffemailaddress = models.CharField(db_column='StaffEmailAddress', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    storeid = models.AutoField(db_column='StoreID', primary_key=True)  # Field name made lowercase.
    branchname = models.CharField(db_column='BranchName', unique=True, max_length=255)  # Field name made lowercase.
    branchstreetaddress = models.CharField(db_column='BranchStreetAddress', max_length=255)  # Field name made lowercase.
    branchcity = models.CharField(db_column='BranchCity', max_length=255)  # Field name made lowercase.
    branchstate = models.CharField(db_column='BranchState', max_length=255)  # Field name made lowercase.
    branchphonenumber = models.CharField(db_column='BranchPhoneNumber', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class User(models.Model):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', unique=True, max_length=255)  # Field name made lowercase.
    useremail = models.CharField(db_column='UserEmail', unique=True, max_length=255)  # Field name made lowercase.
    usercliearancelevel = models.IntegerField(db_column='UserCliearanceLevel')  # Field name made lowercase.
    userpassword = models.CharField(db_column='UserPassword', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
