import openpyxl

try:
    wb = openpyxl.load_workbook("empleados.xlsx")
    hoja = wb.active
except:
    wb = openpyxl.Workbook()
    hoja = wb.active

linea = hoja.max_row + 1
print(linea)
hoja["A1"] = "Fecha"
hoja["B1"] = "Descripcion"
hoja["C1"] = "Responsable"
hoja["D1"] = "Peso"
hoja["E1"] = "Valor"
hoja["F1"] = "Fuente"

fecha = str(input("Fecha del registro: "))
descripcion = str(input("Descripcion del registro: "))
responsable = str(input("Responsable de este registro: "))
peso = float(input("Peso del producto(Si es que tiene): "))
valor = int(input("Valor del producto: "))
fuente = str(input(f'¿De donde salio la plata?: '))
print(f"""Los tados agregados fueron
    La fecha es: {fecha}
    La descripcion es: {descripcion}
    El responsable es: {responsable}S
    El peso es: {peso}
    El valor es: {valor}
    La fuente es: {fuente}
"""
      )
#entrada = int(input(f'A que horas llegaste? '))
#salida = int(input(f'A que horas te fuiste? '))

hoja.append([fecha, descripcion, responsable, peso, valor, fuente,])

wb.save("empleados.xlsx")
print("listo")

