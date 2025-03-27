infoDescripcion = ["Aguacate hass","Aguacate papelito","Bold","Banano","Durazno","Limion Comun","Limon mandarino","Limon tahiti","Mandarina","Mango tomy","Maracuya","Naranja tangelo","Naranja valencia","Panela","Platano","Platano maduro","Guanabana","Almuerzo-Desayuno","Arriendo casa","Arriedo local","Arriendo parqueadero","BCS carro","Chevyplan","Entrada abastos","Gasolina","Gasto personal","Insumo","Lavado","Mario","Onces","Prestamo","Parqueadero carro","Parqueadero moto","Self security","Servicio de energia","Servicio de agua","Venta caja","Venta nequi","Venta daviplata"]

x = str(input("Fecha: "))

try:
    f = int(x)
    final = "/".join([x[i:i+2] for i in range(0,len(x),2)])
    print(final[0:8])
except:
    print("Esto no es compatible")




