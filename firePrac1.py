import firebase_admin
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

baseDeDatos = cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

baseDeDatos = firestore.client()

usuarios = baseDeDatos.collection("clientes").document("usuarios")

usuarios.update({
    "eda":30,
    "email":"sergio@gmail.com"
    })