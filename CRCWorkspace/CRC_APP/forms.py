from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class BranchSerachForm(forms.Form):
    Suburb = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "custom-select"}),
        choices=(("Queensland", "Queensland"),
                 ("New South Wales", "New South Wales"),
                 ("Victoria", "Victoria"),
                 ("Tasmania", "Tasmania"),
                 ("Western Australia", "Western Australia"),
                 ("South Australia", "South Australia"),
                 ("Australian Capital Territory", "Australian Capital Territory"),
                 ("Northern Territory", "Northern Territory"),
                 ))


class BranchOverviewForm(forms.Form):
    choices = (("Queensland", "Queensland"),
               ("New South Wales", "New South Wales"),
               ("Victoria", "Victoria"),
               ("Tasmania", "Tasmania"),
               ("Western Australia", "Western Australia"),
               ("South Australia", "South Australia"),
               ("Australian Capital Territory", "Australian Capital Territory"),
               ("Northern Territory", "Northern Territory"),
               )
    regular_choice = (('no-selection', "none"),
                      ("Queensland", "Queensland"),
                      ("New South Wales", "New South Wales"),
                      ("Victoria", "Victoria"),
                      ("Tasmania", "Tasmania"),
                      ("Western Australia", "Western Australia"),
                      ("South Australia", "South Australia"),
                      ("Australian Capital Territory",
                       "Australian Capital Territory"),
                      ("Northern Territory", "Northern Territory"),
                      )
    date_choices = (('OrderReturnDate', 'Return Date'),
                    ('OrderReturnDate', 'Rent Date'))
    car_choices = (("4WD", "Off Road"), ("AWD", "Suburban"))

    State1 = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=choices)
    State2 = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=regular_choice)
    State3 = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=regular_choice)
    State4 = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=regular_choice)
    start_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        ))
    end_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",
                "type": "date"
            }
        ))
    car_selection = forms.ChoiceField(widget=forms.Select(
        attrs={'class': 'form-control'}), choices=car_choices)
    date_selection = forms.ChoiceField(
        widget=forms.RadioSelect(), choices=date_choices)


class BranchManagementForm(forms.Form):
    SQLTables = (
        ('auth_user', 'Auth_User'),
        ('store', 'Store'),
        ('orderrecord', 'OrderRecord'),
        ('staff', 'Staff'),
        ('car', 'Car'),
    )
    TableSelection = forms.ChoiceField(label=False, choices=SQLTables)
    CustomSQL = forms.CharField(label=False, max_length=1000, required=False, widget=forms.Textarea(
        attrs={'id': 'sqltext', 'rows': "5", 'class': 'form-control input', 'placeholder': 'Enter your SQL queries here'}))


class CarFeatureAnalysisForm(forms.Form):
    CarFeature = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "custom-select"}),
        choices=(
        ("CarMake", "Car Make"),
        ("CarYear", "Car Year"),
        ("CarFuelSystem", "Car Fuel System"),
        ("CarSeatingCapacity", "Car Seating Capacity"),
        ("CarStandardTransmission", "Car Standard Transmission"),
        ("CarBodyType", "Car Body Type"),
        ("CarDrive", "Car Drive")
    )
    )
    StoreSeach = forms.CharField(label=False, required=False, max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control input', 'placeholder': 'Store Name'}))


class CarRecomendationForm(forms.Form):
    TerrainType = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "custom-select"}),
        choices=(("1", "Highway"), ("4WD", "Off Road"), ("3", "Urban")))
    Price = forms.IntegerField(required=False, min_value=0, max_value=1000000, widget=forms.HiddenInput(
        attrs={'class': 'form-control input', 'placeholder': '0', 'readonly': 'priceLabel', 'id': 'priceForm'}))
    Seats = forms.IntegerField(required=False, min_value=0, max_value=1000000, widget=forms.HiddenInput(
        attrs={'class': 'form-control input', 'placeholder': '0', 'readonly': 'priceLabel', 'id': 'seatForm'}))


class EditCarAvailablityForm(forms.Form):
    AvaliableChoice = (('1', 'Yes'), ('0', 'No'))
    carID = forms.IntegerField(label=False,
                               required=True, widget=forms.NumberInput(
                                   attrs={'id': 'carID-input', 'class': 'form-control', 'onfocusout': 'changeRecomendation()'}))
    Avalible = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'Form-label-radio'}), choices=AvaliableChoice)
    RoadWorthy = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'class': 'Form-label-radio'}), choices=AvaliableChoice)


class VehicleHireAnalysisForm(forms.Form):
    Month = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "custom-select"}),
        choices=(
            ("01", "January"),
            ("02", "February"),
            ("03", "March"),
            ("04", "April"),
            ("05", "May"),
            ("06", "June"),
            ("07", "July"),
            ("08", "August"),
            ("09", "September"),
            ("10", "October"),
            ("11", "November"),
            ("12", "December")
    )
    )
    Year = forms.ChoiceField(widget=forms.Select(
        attrs={'class': "custom-select"}),
        choices=(
            ("2005", "2005"),
            ("2006", "2006"),
            ("2007", "2007"),
            ("2008", "2008"),
            ("2009", "2009"),
            ("2010", "2010")
    )
    )
