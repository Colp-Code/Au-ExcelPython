import openpyxl
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

try:
    ff = openpyxl.load_workbook("empleados.xlsx")
    hoja = ff.active
except:
    ff = openpyxl.Workbook()
    hoja = ff.active

try:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)

    db = firestore.client()

    usuarios = db.collection("usuarios").get()
    for doc in usuarios:
        one = doc.to_dict()
        print(one[0]["edad"])
except BaseException as error:
    print('An exception occurred: {}'.format(error))

