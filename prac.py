import openpyxl
productos = [
    ('producto_1', 'a859', 1500, 9.95),
    ('producto_2', 'b125', 600, 4.95),
    ('producto_3', 'c764', 200, 19.95),
    ('producto_4', 'd399', 2000, 49.95)
]
wb = openpyxl.Workbook()
hoja = wb.active
# Crea la fila del encabezado con los títulos
hoja.append(('Nombre', 'Referencia', 'Stock', 'Precio'))
for producto in productos:
    # producto es una tupla con los valores de un producto 
    hoja.append(producto)

wb.save("prueba.xlsx")
print("listo")