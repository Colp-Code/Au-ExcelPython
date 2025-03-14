import openpyxl

wb = openpyxl.Workbook()
hoja = wb.active 
hoja.title = "Datos"

personas = [
    ('Juan', 28, 'falso'),
    ('Sergio', 20, 'Patron'),
    ('Ichi', 18, 'Matematico'),
]
t = hoja.append(('Nombre', 'Edad', 'Puesto'))

for empleados in personas:
    hoja.append(empleados)

wb.save("empleados.xlsx")
print("listo")