from django.urls import path

from . import views

app_name = 'CRC_APP'
urlpatterns = [
    path('', views.index, name='index'),
    path('BranchOverview/', views.BranchOverview),
    path('BranchOverview/<SearchBranch>', views.BranchOverview),
    path('BranchManagement/', views.BranchManagement, name='BranchManagement'),
    path('BranchDetails', views.BranchDetails, name='BranchDetails'),
    path('CarFeatureAnalysis/', views.CarFeatureAnalysis,
         name='CarFeatureAnalysis'),
    path('CarRecomendation/', views.CarRecomendation, name='CarRecomendation'),
    path('BranchDetails/', views.BranchDetails, name='BranchDetails'),
    path('register/', views.register, name='register'),
    path('BranchDetails/', views.BranchDetails, name='BranchDetails'),
    path('BranchDetails/<State>/', views.BranchDetails),
    path('EditCarAvailablity', views.EditCarAvailability),
    path('VehicleHireAnalysis/', views.vehicleHireAnalysis,
         name='VehicleHireAnalysis'),
    path('VehicleDataComparison/', views.VehicleDataComparison.getView,
         name='VehicleDataComparison'),
]
