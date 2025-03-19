import openpyxl

try:
    wb = openpyxl.load_workbook("empleados.xlsx")
    hoja = wb.active
except:
    wb = openpyxl.Workbook()
    hoja = wb.active

linea = hoja.max_row + 1
print(linea)

entrada = int(input(f'A que horas llegaste? '))
salida = int(input(f'A que horas te fuiste? '))

hoja.append([linea - 1, entrada, salida,])

wb.save("empleados.xlsx")
print("listo")

