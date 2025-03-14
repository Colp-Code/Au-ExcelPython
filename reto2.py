import openpyxl

wb = openpyxl.load_workbook("empleados.xlsx")
print("Ya esta cargada")
hoja = wb.active

hoja["D1"] = "Salario"

salarios = [8000,9000,10000]

for i, salario in enumerate(salarios, start=2):
    hoja[f"D{i}"] = salario
    print(i)

wb.save("empleados.xlsx")
print("Ya se guardo")
