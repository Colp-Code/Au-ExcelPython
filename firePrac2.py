import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials

baseDeDatos = cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

baseDeDatos = firestore.client()

doc = baseDeDatos.collection("Equipo").document("losTilines")

doc.set({
    "nombre":"Tilines",
    "equipos":[
        {"nombre":"cristian","posicion":"defensa"},
        {"nombre":"sergio","posicion":"portero"}
    ],

})

doc.update({"equipos":firestore.ArrayUnion([{
        "nombre":"yurlaydis",
        "posicion":"titular"
    }])
})

equipo = baseDeDatos.collection("Equipo").get()


resultado = None
for documento in equipo:
    mapa = documento.to_dict()
    for jugador in mapa.get('equipos',[]):
        if jugador.get('nombre') == 'yurlaydis':
            resultado = jugador
            print(resultado)
            break 

doc.update({'equipos':firestore.ArrayRemove([resultado])})
doc.update({'equipos':firestore.ArrayUnion([{'nombre':'yuyeimy','posicion':'EnCuatro'}])})