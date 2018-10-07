from django.shortcuts import render, redirect
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import path
from django.db import connection
from .forms import BranchSerachForm
from .forms import BranchOverviewForm
from .forms import CarFeatureAnalysisForm
from .forms import BranchManagementForm
from .forms import EditCarAvailablityForm
from .models import Store, Orderrecord, Car
from .forms import VehicleHireAnalysisForm
from django.db import connections
import django.db as db
import collections
from .forms import CarRecomendationForm
from .backend_code.CarRecomendation import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import TemplateView
from .decorators import staff_required, management_required


# Create your views here.


def index(request):
    # return HttpResponse("Hello World from Python Django")
    template = loader.get_template('CRC_APP/index.html')
    context = {
        'hello': 'testing',
    }
    return HttpResponse(template.render(context, request))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/CRC_APP')
    else:
        form = UserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)


@login_required
@management_required
def BranchOverview(request):
    if request.method == 'POST':
        form = BranchOverviewForm(request.POST)
        if form.is_valid():
            state = []
            car_selection = form.cleaned_data['car_selection']
            state.append(form.cleaned_data['State1'])
            state.append(form.cleaned_data['State2'])
            state.append(form.cleaned_data['State3'])
            state.append(form.cleaned_data['State4'])
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            date_selection = form.cleaned_data['date_selection']
            query_list = []
            for state_selection in state:
                query = "select distinct c.CarModel,count(c.CarModel) as totalHired from orderrecord o " + \
                    "inner join car c on o.CarID = c.CarID " + \
                    "inner join store s on o.OrderReturnStoreID = s.StoreID " + \
                    "where (o.{} >= '{}-{}-{}' and o.{} <= '{}-{}-{}') ".format(date_selection, start_date.year, start_date.month, start_date.day, date_selection, end_date.year, end_date.month, end_date.day) + \
                    "and (s.BranchState like '{}') ".format(state_selection) + \
                    "and (c.CarDrive like '{}') ".format(car_selection) + \
                    "group by c.CarModel"
                query_list.append(query)
            print(query_list)

    else:
        form = BranchOverviewForm()
        # BranchSearch = request.GET.BranchName
    return render(request, 'CRC_APP/BranchOverview.html', {'form': form})


@login_required
@staff_required
def BranchManagement(request):
    if request.method == 'POST':
        form = BranchManagementForm(request.POST)
        if form.is_valid():
            if(form.cleaned_data['CustomSQL'] != ''):
                Table = form.cleaned_data['TableSelection']
                TableStructure = getTableStructure(Table)
                SQLQuery = CustomSQL(form.cleaned_data['CustomSQL'])
                if(isinstance(SQLQuery, collections.Mapping)):
                    errors = SQLQuery
                    SQLHeader = None
                    SQLQuery = None
                else:
                    errors = None
                    SQLHeader = SQLQuery[0]
                    SQLQuery = SQLQuery[1]
            else:
                errors = None
                SQLQuery = None
                SQLHeader = None
                Table = form.cleaned_data['TableSelection']
                TableStructure = getTableStructure(Table)
        else:
            Table = form.cleaned_data['TableSelection']
            TableStructure = getTableStructure(Table)
            SQLQuery = None
            SQLHeader = None
            errors = {'error': "Form data isn't accepted"}

    else:
        errors = None
        SQLHeader = None
        SQLQuery = None
        TableStructure = None
        form = BranchManagementForm()
    return render(request, 'CRC_APP/BranchManagement.html', {'form': form, 'tableHead': SQLHeader, 'table': TableStructure, 'SQLResult': SQLQuery, 'error': errors})


def BranchDetails(request, State=''):
    template_name = "CRC_APP/BranchDetails.html"
    result = None
    errors = None
    if request.method == 'POST':
        form = BranchSerachForm(request.POST)
        if form.is_valid():
            # print("South")
            text = form.cleaned_data['Suburb']
            print(text)
            return HttpResponseRedirect('/CRC_APP/BranchDetails/{}'.format(text))

    else:
        form = BranchSerachForm()
        if State != '':
            result = displayBranchDetails(State)
            if len(result) == 0:
                errors = "There are no branches in the state!"

    args = {'form': form, 'Branch': result, 'error': errors}
    return render(request, template_name, args)


def CarRecomendation(request):
    return CarRecomendationPage.getView(request)


@login_required
@management_required
def CarFeatureAnalysis(request):
    if request.method == 'POST':
        form = CarFeatureAnalysisForm(request.POST)
        if form.is_valid():
            CarFeatureGroupBy = form.cleaned_data['CarFeature']
            StoreSearch = form.cleaned_data['StoreSeach']
            # Use CarFeatureGroupBy to do some sql query and change results of context
            if StoreSearch == '':
                query = "SELECT c.{}, Count(*) As CarNum FROM car c ".format(CarFeatureGroupBy) + \
                    "LEFT JOIN orderrecord o " + \
                    "On c.CarID = o.CarID " + \
                    "Group By {} ".format(CarFeatureGroupBy) + \
                    "Order By CarNum Desc " + \
                    "Limit 5"
                results = my_custom_sql(query)
                results = results[1]
            else:
                query = "SELECT StoreID From store WHERE BranchName LIKE '{}%'".format(
                    StoreSearch)
                storeResult = my_custom_sql(query)
                storeID = storeResult[1][0][0]
                query = "SELECT c.{}, Count(*) As CarNum FROM car c ".format(CarFeatureGroupBy) + \
                    "LEFT JOIN orderrecord o " + \
                    "On c.CarID = o.CarID " + \
                    "Where o.OrderPickupStoreID = {} ".format(storeID) + \
                    "Group By {} ".format(CarFeatureGroupBy) + \
                    "Order By CarNum Desc " + \
                    "Limit 5"
                results = my_custom_sql(query)
                results = results[1]

    else:
        # Default example results
        results = []
        form = CarFeatureAnalysisForm()
    context = {
        'results': results,
        'form': form
    }
    template = loader.get_template('CRC_APP/CarFeatureAnalysis.html')
    return HttpResponse(template.render(context, request))


class VehicleDataComparison:

    @staticmethod
    def getView(request):
        results = VehicleDataComparison.getData()
        context = {
            'results': results
        }
        template = loader.get_template(
            'CRC_APP/VehicleDataComparison/VehicleDataComparison.html')
        return HttpResponse(template.render(context, request))

    @staticmethod
    def getData():
        results = my_custom_sql('''
			SELECT 
				BranchName, 
				SUBSTRING(OrderPickupDate, 1, 4) as Year, 
				SUBSTRING(OrderPickupDate, 5, 2) as Month,
				CASE
					WHEN (year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) >= 18 and  year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) <= 25) THEN '18-25'
					WHEN (year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) >= 26 and  year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) <= 40) THEN '26-40'
					WHEN (year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) >= 41 and  year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) <= 55) THEN '41-55'
					WHEN (year(now())-year(str_to_date(CustomerDOB, '%d/%m/%Y')) >= 56) THEN '56+'
				END as age,
				CarMake,
				count(*) as VehiclesBurrowed
			FROM customer, orderrecord, car, store
			WHERE OrderPickupStoreID=StoreID
			AND orderrecord.CustomerID=customer.CustomerID
			AND orderrecord.CarID=car.CarID
			GROUP BY BranchName, Year, Month, age, CarMake;
		''')
        return results[1]


def vehicleHireAnalysis(request):
    template = loader.get_template('CRC_APP/VehicleHireAnalysis.html')
    title = None
    tables = None
    header = None
    errors = None
    if request.method == 'POST':
        form = VehicleHireAnalysisForm(request.POST)
        if form.is_valid():
            month = form.cleaned_data['Month']
            year = form.cleaned_data['Year']
            print(month, year)
            print(type(month), type(year))
            title = month+"/"+year
            search = year+month
            print(search)
            query = "SELECT DISTINCT c.CarModel,c.CarMake,c.CarSeries,count(c.CarModel) as TotalHired from orderrecord o inner join car c on o.CarID=c.CarID where o.OrderCreateDate LIKE '{}%' group by c.CarModel order by TotalHired desc limit 5".format(
                search)
            popular = my_custom_sql(query)
            print(popular)
            header = popular[0]
            print(header)
            tables = popular[1]
            print(tables)
            if len(tables) == 0:
                errors = "There is no data available"

    else:
        form = VehicleHireAnalysisForm()
    context = {
        'form': form,
        'Heading': title,
        'Output': tables,
        'thead': header,
        'warning': errors
    }
    return HttpResponse(template.render(context, request))


def EditCarAvailability(request):
    template_name = "CRC_APP/EditCarAvaliablity.html"
    if request.method == 'POST':
        form = EditCarAvailablityForm(request.POST)
        if form.is_valid():
            avaliable = form.cleaned_data['Avalible']
            roadworthy = form.cleaned_data['RoadWorthy']
            carID = form.cleaned_data['carID']
            avaliable_result = Car.update_avaliable(carID, avaliable)
            roadworthy_result = Car.update_roadworthy(carID, roadworthy)
            if(roadworthy_result == 'success' and avaliable_result == 'success'):
                result = 'SUCCESS'
            else:
                result = 'FAILED CarID: {} does not exist'.format(carID)
        else:
            result = 'form is not valid'

    else:
        result = None
        form = EditCarAvailablityForm()
    return render(request, template_name, {'form': form, 'result': result})


def processOrderQuerySet(query):
    data = []
    for orders in query:
        orderID = orders.orderid
        CarModel = orders.carid.carmodel
        CustomerName = orders.customerid.customername
        CustomerPhNo = orders.customerid.customerphonenumber
        CustomerAddress = orders.customerid.customeraddress
        BranchReturn = orders.orderreturnstoreid.branchname
        orderRentDate = orders.orderpickupdate
        orderReturnDate = orders.orderreturndate
        list = []
        list.append(orderID)
        list.append(CarModel)
        list.append(CustomerName)
        list.append(CustomerPhNo)
        list.append(CustomerAddress)
        list.append(BranchReturn)
        list.append(orderRentDate)
        list.append(orderReturnDate)
        data.append(list)
    return data


def getTableStructure(table):
    cursor = connections['default'].cursor()
    cursor.execute('describe {}'.format(table))
    row = cursor.fetchall()
    return row


def CustomSQL(SQLFunction):
    try:
        cursor = connections['CustomSQL'].cursor()
        cursor.execute(SQLFunction)
        row = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = []
        data.append(columns)
        data.append(row)
        return data
    except:
        return {'error': "SQL Query didn't work"}


def my_custom_sql(SQLFunction):
    with connection.cursor() as cursor:
        try:
            cursor.execute(SQLFunction)
            row = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = []
            data.append(columns)
            data.append(row)
        except:
            return {'error': "SQL Query didn't work"}
    return data


def displayBranchDetails(State):
    objects = Store.objects.filter(branchstate=State)
    # count=len(objects)
    # Create dictionary for Short form State
    Shortform = {
        "Queensland": "QLD",
        "New South Wales": "NSW",
        "Tasmania": "TAS",
        "Victoria": "VIC",
        "South Australia": "SA"
    }
    data = []
    for store in objects:
        data.append({'Name': store.branchname, 'Address': store.branchstreetaddress,
                     'City': store.branchcity, 'State': Shortform[store.branchstate],
                     'Contact': store.branchphonenumber})
    print("success")
    return data


# Branch Overview SQL query

# select distinct c.CarModel,count(c.CarModel) as totalHired from orderrecord o
# inner join car c on o.CarID = c.CarID
# inner join store s on o.OrderReturnStoreID = s.StoreID //need to change OrderReturnStoreID based on whether user
#                                                        //picks returnDate or rentdate. If rent date radiobutton is
#                                                        //chosen, use OrderPickupStoreID
# where (o.OrderReturnDate >= '2005-07-01' and o.OrderReturnDate <= '2005-07-31') //dates seen are placeholder values
#                                                                                 //change to {}.Also change
#                                                                                 //OrderReturnDate to OrderPickupDate
#                                                                                 //if rent date radiobutton is chosen
# and (s.BranchState like 'South Australia')// South Australia is a placeholder. change to {}
# and (c.CarDrive like '4WD') // 4WD is a placeholder. change to {}
# group by c.CarModel;

# Arrays that could maybe help with the changing of columns
# returnPeriod=[OrderReturnStoreID,OrderReturnDate]
# rentPeriod=[OrderPickupStoreID,OrderPickupDate]
