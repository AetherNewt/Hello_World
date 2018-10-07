# Import important library
import pandas as pd
import numpy as np
from pandas import DataFrame

# read the car CSV
car = pd.read_csv('car.csv')
# create data frame of the car
df = DataFrame(car, columns=['Car_ID', 'Car_MakeName', 'Car_Model', 'Car_Series', 'Car_SeriesYear', 'Car_PriceNew', 'Car_EngineSize', 'Car_FuelSystem',
                             'Car_TankCapacity', 'Car_Power', 'Car_SeatingCapacity', 'Car_StandardTransmission', 'Car_BodyType', 'Car_Drive', 'Car_Wheelbase'])

# get the location of all the cars make of null
location = df[df['Car_MakeName'].isnull()].index.tolist()

InvalidCarID = []

# create a list with all the invalid carID
for x in range(0, len(location)):
    InvalidCarID.append(df.loc[df.index[location[x]], 'Car_ID'])

# check remove all the invalid carID
for x in range(0, len(location)):
    df = df[df.Car_ID != InvalidCarID[x]]

# check for anymore more invalid carID
anyValid = df[df['Car_MakeName'].isnull()].index.tolist()

# export the filtered car.csv
df.to_csv('carFiltered.csv', index=False)

# read the order csv
order = pd.read_csv('order.csv')

# create a dataframe of the car CSV
orderdf = DataFrame(order, columns=['OrderID', 'OrderCreateDate', 'OrderStatus', 'OrderPickupDate',
                                    'OrderReturnDate', 'CustomerID', 'CarID', 'OrderPickupStoreID', 'OrderReturnStoreID'])
# remove the orders that have an invalid carID
for x in range(0, len(InvalidCarID)):
    orderdf = orderdf[orderdf.CarID != InvalidCarID[x]]

# read store csv file
store = pd.read_csv('Store.csv')
# create store dataframe
storedf = DataFrame(store, columns=['StoreID', 'StoreName', 'StoreAddress',
                                    'StorePhone', 'StoreCity', 'StoreStateName'])
StoreLocation = storedf[storedf['StoreName'].isnull()].index.tolist()

InvalidStoreID = []
# create a list of invalid StoreID
for x in range(0, len(StoreLocation)):
    InvalidStoreID.append(
        storedf.loc[storedf.index[StoreLocation[x]], 'StoreID'])

# remove the rows with an invalid storeID
for x in range(0, len(InvalidStoreID)):
    storedf = storedf[storedf['StoreID'] != InvalidStoreID[x]]

# export the filtered store csv file
storedf.to_csv('storeFiltered.csv', index=False)

# remove the orders with an invalid storeID
for x in range(0, len(InvalidStoreID)):
    orderdf = orderdf[orderdf['OrderPickupStoreID'] != InvalidStoreID[x]]
    orderdf = orderdf[orderdf['OrderReturnStoreID'] != InvalidStoreID[x]]
orderdf.to_csv('orderFiltered.csv', index=False)
