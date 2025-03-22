import openpyxl
import datetime as dt
import sys

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

current_date = dt.date.today()
format_date = current_date.strftime("%d-%m-%y")
print(f'La fecha es {format_date}')

try:
    respuesta = int(input(f"""¿Quieres la fecha outomatica o la quieres poner?
                          
Poner = 1
automatica = 2
Cual es tu opcion: """))
    if respuesta == 1:
        fecha = str(input("Fecha del registro: "))
    else:
        fecha = format_date

    descripcion = str(input("Descripcion del registro: "))
    responsable = str(input("Responsable de este registro: "))
    peso = float(input("Peso del producto(Si es que tiene): "))
    valor = float(input("Valor del producto: "))
    fuente = str(input(f'¿De donde salio la plata?: '))
    print(f"""Los tados agregados fueron
    La fecha es: {fecha}
    La descripcion es: {descripcion}
    El responsable es: {responsable}S
    El peso es: {peso}
    El valor es: {valor}
    La fuente es: {fuente}
    """)
    try:
        confirmar = int(input("""
        ¿Quieres confirmar esta informacion?
        si = 1
        no = 2
        """))
        if confirmar not in range(1,3):
            print("Opcion no valida")
        elif confirmar == 1:
            hoja.append([fecha, descripcion, responsable, peso, valor, fuente,])
            print("Datos listos")
        else:
            print("Datos no guardados")
            
            
    except:
        print("Tipo de dato no valido")
        sys.exit(1)
except:
    print("Tipo de dato incorrecto")
    sys.exit(1)



      
#entrada = int(input(f'A que horas llegaste? '))
#salida = int(input(f'A que horas te fuiste? '))



wb.save("empleados.xlsx")
print("listo")

