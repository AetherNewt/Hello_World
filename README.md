# IFB299-Group-52

A repository that contains the IFB299 Car Rental Web Application

## Software Version we are using:

Python 3.6.5

Django 2.1

## First activate virtual env:

cd IFB299GRoup52

venv/Scripts/activate(windows)

source ./venv/Scripts/activate (macOS/Linux)

## Runing Server:

Commandline Instructions:

cd CRCWorkspace

py manage.py runserver (windows)

python manage.py runserver (MacOS/linux)

## Importing MySQL DB:

1. Create a Schema called crc-database-data52
2. Use workbench Data Import/Restore
3. Click on the Import from Self-Contained File radio box and clock on the button with ...
4. Brouse to the mysql file in github repo
5. In the Default Target Scheme select crc-database-data52
6. Click on the Start Import button

## Setting User Permission

1. Click on Users and Privilleges
2. Create Account with CRCDevTeam
3. Username: CRCDevTeam
4. Password: Data52Database
5. Limit to Host: localhost
6. Schema Privileges: Add Schema anad permissions

## Connecting to Cloud DB

HostName: 35.197.174.56

Port: 3306

Username: CRCDevTeam

Password: Data52Database

Default Schema: crc-database-data52
