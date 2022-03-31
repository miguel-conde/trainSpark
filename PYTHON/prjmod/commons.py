import os

# DIR_ROOT = os.path.abspath(os.path.join('.')) # Tb OK, al menos en VSCode
DIR_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# print("DIR_ROOT:" + DIR_ROOT)

DIR_DATA = os.path.join(DIR_ROOT, "data")   

DIR_DL =  os.path.join(DIR_DATA, "datalake")
DL_FILE_FLIGHTS = os.path.join(DIR_DL, "flights.csv")

DIR_DW =  os.path.join(DIR_DATA, "datawarehouse")

DIR_OUTPUTS = os.path.join(DIR_ROOT, "outputs")   