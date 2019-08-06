import json
from pathlib import Path              

#Grabar la lista en el json
def GrabarFile(lis):
    with open("commerce.json","w") as file:
        json.dump(lis, file) 
#Abrimos el archivo en lectura
def openFile():
    file=Path('commerce.json')
    if file.is_file():
        with open('commerce.json', 'r') as file:
            data= json.load(file)
        return data
    else:
        commerce={}
        return commerce
#Validamos el producto
def Validar(lis,prod):
    for i in lis:
        if i["Nombre"]==prod:
            lis.remove(i)
            print("El producto ya existe")
            return True
        else:
            return False
#Cargamos el producto
def Carga_prod(lis):
    datos={}
    prod=input("Ingrese nombre de producto: ")
    datos["Nombre"]=prod
    precio=input("Ingrese el carateristica: ")
    datos["Caracteristica"]=precio
    validacion=Validar(lis,prod)
    lis.append(datos)
#Eliminamos el producto
def Sacar_prod(lis):
    aux={}
    nombre=input("Que producto desea sacar:")
    for i in lis:
        if i["Nombre"]==nombre:
            for x,y in i.items():
                if x=="Nombre":
                    aux["Nombre"]=y
                else:
                    aux["Caracteristica"]=y
    lis.remove(aux)
#Modificamos
def Modificacion(lis):
    nombre=input("\nQue producto desea modificar: ")
    cambio=input("Por que nombre lo desea modificar: ")
    for i in lis:
        if i["Nombre"] == nombre:
            i["Nombre"]=cambio

#Inicializacion
productos=[]
rta=input("Desea cargar producto nuevo: (s/n) ")
while (rta== 's' or rta=='S'):
    commerce=openFile()
    Carga_prod(productos)
    rta=input("Desea ingresar producto nuevo: (s/n) ")
GrabarFile(productos)

#Eliminacion
rta=input("Desea eliminar al un producto: (s/n)")
if (rta=='s' or rta=='S'):
    Sacar_prod(productos)
    GrabarFile(productos)


#Modificacion
rta=input("Desea modificar a un producto: (s/n)")
if (rta=='s' or rta=='S'):
    Modificacion(productos)
    GrabarFile(productos)
print(productos)