import firebase_admin 
from firebase_admin import firestore
from firebase_admin import credentials

baseDeDatos = cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

baseDeDatos = firestore.client()

db = baseDeDatos.collection("Equipo").document("losTilines")
datos = baseDeDatos.collection("Equipo").get()

listaJugadores = None
for administrar in datos:
    admindDatos = administrar.to_dict()
    for jugadores in admindDatos.get('equipos',[]):
        listaJugadores = jugadores

db.set({"nombre": "Tilines",
  "equipos": [
    {"nombre": "Cristian", "posicion": "defensa"},
    {"nombre": "Sergio", "posicion": "portero"},
    {"nombre": "Yurlaydis", "posicion": "titular"},
    {"nombre": "Pedro", "posicion": "defensa"},
    {"nombre": "Luis", "posicion": "delantero"}
]})

conteo = {}

for diccio in datos:
    docDict = diccio.to_dict()
    for jugadores in docDict.get('equipos', []):
        jugador = jugadores['nombre']
        posicion = jugadores['posicion']
        if posicion not in conteo:
            conteo[posicion] = []
        conteo[posicion].append(jugador)

print(f'Defensas: {conteo.get("defensa", [])}')
print(f'Portero: {conteo["portero"]}')
print(f'Titular: {conteo["titular"]}')
print(f'Delanteros: {conteo["delantero"]}')
