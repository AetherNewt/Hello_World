import sys
import os
import django
sys.path.append(
    "/media/john/System Drive/Users/John/Desktop/UNI Files/2018 Sem 2/IFB299/IFB299-Group-52/CRCWorkspace")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CRCWorkspace.settings")
django.setup()

from CRC_APP.models import *


carID = 0000
avaliable = 0
result = Car.update_avaliable(carID, avaliable)
print(result)
