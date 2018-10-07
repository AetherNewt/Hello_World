from CRC_APP.models import Store, Orderrecord, Store
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.shortcuts import render, redirect
from django.template import loader

class CarRecomendationPage():
	
	class PageForm(forms.Form):
		TerrainType = forms.ChoiceField(widget=forms.Select(
			attrs={'class': "custom-select"}),
			choices=(("1", "Highway"), ("4WD", "Off Road"), ("3", "Urban")))
		Price = forms.IntegerField(required=False, min_value=0, max_value=1000000, widget=forms.HiddenInput(
			attrs={'class': 'form-control input', 'placeholder': '0', 'readonly': 'priceLabel', 'id': 'priceForm'}))
		Seats = forms.IntegerField(required=False, min_value=0, max_value=1000000, widget=forms.HiddenInput(
			attrs={'class': 'form-control input', 'placeholder': '0', 'readonly': 'priceLabel', 'id': 'seatForm'}))
	
	@staticmethod
	def getView(request):
		filters=''
		results = None
		if request.method == 'POST':
			form = CarRecomendationPage.PageForm(request.POST)
			if form.is_valid():
				filters = {
					'TerrainType': form.cleaned_data['TerrainType'],
					'Price': form.cleaned_data['Price'],
					'Seats': form.cleaned_data['Seats']
				}
				pass  # does nothing, just trigger the validation
		else:
			form = CarRecomendationPage.PageForm()
		results = CarRecomendationPage.getData(filters)
		context = {
			'form': form, 'results': results
		}
		return render(request, 'CRC_APP/CarRecomendation.html', context)
	
	@staticmethod
	def getData(filters):
		lastReturnedOrder = Orderrecord.objects.raw('''
		SELECT OrderID
		FROM orderrecord o1
		WHERE o1.OrderReturnDate = (
			SELECT MAX(o2.OrderReturnDate) As OrderReturnDate
			FROM orderrecord o2
			WHERE o1.CarID = o2.CarID
		)
		''')
		orders = []
		for i in lastReturnedOrder:
			orders.append(str(i.orderid))
		lastReturnedOrder = Orderrecord.objects.filter(orderid__in=orders)
		
		if filters != '':
			minPrices = [0,20000,70000]
			maxPrices = [20000,70000,100000000000]
			minPrice = minPrices[int(filters['Price'])-1]
			maxPrice = maxPrices[int(filters['Price'])-1]
			lastReturnedOrder = lastReturnedOrder.filter(carid__carpricenew__gte=int(minPrice))
			lastReturnedOrder = lastReturnedOrder.filter(carid__carpricenew__lte=int(maxPrice))
			lastReturnedOrder = lastReturnedOrder.filter(carid__carseatingcapacity__gte=int(filters['Seats']))
			if filters['TerrainType'] == "4WD":
				lastReturnedOrder = lastReturnedOrder.filter(carid__cardrive=filters['TerrainType'])
		
		lastReturnedOrder = lastReturnedOrder[:40]
		data = []
		for orders in lastReturnedOrder:
			CarMake = orders.carid.carmake
			CarSeries = orders.carid.carseries
			CarYear = orders.carid.caryear
			CarWheelBase = orders.carid.carwheelbase
			CarDrive = orders.carid.cardrive
			CarSeatingCapacity = orders.carid.carseatingcapacity
			CarPriceNew = orders.carid.carpricenew
			CarLastAddress = orders.orderreturnstoreid.branchname
			
			list = []
			list.append(CarMake)
			list.append(CarSeries)
			list.append(CarYear)
			list.append(CarSeatingCapacity)
			list.append(CarDrive)
			list.append(CarWheelBase)
			list.append(CarLastAddress)
			list.append(CarPriceNew)
			
			data.append(list)
		return data

