import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

baseDeDatos = cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
baseDeDatos = firestore.client()

datos = baseDeDatos.collection("Equipo").document("losTilines")

doc = baseDeDatos.collection("Equipo").get()
jugador = None
for dato in doc:
    datoJson = dato.to_dict()
    for jugadores in datoJson.get('equipos', []):
        if jugadores['posicion'] == "EnCuatro":
            jugador = jugadores
            print(jugador)
            break


datos.update({'equipos':firestore.ArrayRemove([jugador])})
datos.update({'equipos':firestore.ArrayUnion([{'nombre': 'pedro','posicion':'delantero'}])})

conteo = {}

for diccio in doc:
    docDict = diccio.to_dict()
    for jugadores in docDict.get('equipos', []):
        posicion = jugadores['posicion']
        conteo[posicion] = conteo.get(posicion, 0) + 1

print(conteo)

print(f'defensas: {conteo["defensa"]}')
print(f'porteros: {conteo["portero"]}')
print(f'delanteros: {conteo["delantero"]}')