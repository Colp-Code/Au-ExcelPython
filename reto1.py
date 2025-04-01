import openpyxl
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection("usuarios").get()

for doc in docs:
    print(f'ID del docuemnto es {doc.id}')
    print(f'Lo que tiene esto es {doc.to_dict()}')