# Generated by Django 2.1 on 2018-09-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_management', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('carid', models.IntegerField(db_column='CarID', primary_key=True, serialize=False)),
                ('carmodel', models.CharField(db_column='CarModel', max_length=255)),
                ('carmake', models.CharField(db_column='CarMake', max_length=255)),
                ('carseries', models.CharField(db_column='CarSeries', max_length=255)),
                ('caryear', models.IntegerField(db_column='CarYear')),
                ('carpricenew', models.DecimalField(db_column='CarPriceNew', decimal_places=2, max_digits=15)),
                ('carenginesize', models.CharField(db_column='CarEngineSize', max_length=255)),
                ('carfuelsystem', models.CharField(db_column='CarFuelSystem', max_length=255)),
                ('cartankcapacity', models.CharField(db_column='CarTankCapacity', max_length=255)),
                ('carpower', models.CharField(db_column='CarPower', max_length=255)),
                ('carseatingcapacity', models.IntegerField(db_column='CarSeatingCapacity')),
                ('carstandardtransmission', models.CharField(db_column='CarStandardTransmission', max_length=255)),
                ('carbodytype', models.CharField(db_column='CarBodyType', max_length=255)),
                ('cardrive', models.CharField(db_column='CarDrive', max_length=255)),
                ('carwheelbase', models.CharField(db_column='CarWheelbase', max_length=255)),
            ],
            options={
                'db_table': 'car',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerid', models.AutoField(db_column='CustomerID', primary_key=True, serialize=False)),
                ('customername', models.CharField(db_column='CustomerName', max_length=255)),
                ('customerphonenumber', models.CharField(db_column='CustomerPhoneNumber', max_length=255)),
                ('customeraddress', models.CharField(db_column='CustomerAddress', max_length=255)),
                ('customeroccupation', models.CharField(db_column='CustomerOccupation', max_length=255)),
                ('customerdob', models.CharField(db_column='CustomerDOB', max_length=255)),
                ('customergender', models.CharField(db_column='CustomerGender', max_length=45)),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderrecord',
            fields=[
                ('orderid', models.IntegerField(db_column='OrderID', primary_key=True, serialize=False)),
                ('ordercreatedate', models.CharField(db_column='OrderCreateDate', max_length=255)),
                ('orderstatus', models.CharField(db_column='OrderStatus', max_length=255)),
                ('orderpickupdate', models.CharField(db_column='OrderPickupDate', max_length=255)),
                ('orderreturndate', models.CharField(db_column='OrderReturnDate', max_length=255)),
            ],
            options={
                'db_table': 'orderrecord',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffid', models.AutoField(db_column='StaffID', primary_key=True, serialize=False)),
                ('staffname', models.CharField(db_column='StaffName', max_length=255)),
                ('staffemailaddress', models.CharField(db_column='StaffEmailAddress', max_length=255)),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('storeid', models.AutoField(db_column='StoreID', primary_key=True, serialize=False)),
                ('branchname', models.CharField(db_column='BranchName', max_length=255, unique=True)),
                ('branchstreetaddress', models.CharField(db_column='BranchStreetAddress', max_length=255)),
                ('branchcity', models.CharField(db_column='BranchCity', max_length=255)),
                ('branchstate', models.CharField(db_column='BranchState', max_length=255)),
                ('branchphonenumber', models.CharField(db_column='BranchPhoneNumber', max_length=255)),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='UserID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='Username', max_length=255, unique=True)),
                ('useremail', models.CharField(db_column='UserEmail', max_length=255, unique=True)),
                ('usercliearancelevel', models.IntegerField(db_column='UserCliearanceLevel')),
                ('userpassword', models.CharField(db_column='UserPassword', max_length=255)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
