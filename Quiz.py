import os
os.system("cls")

# Ejercicio 1

print("Ejercicio 1")
lista = []
materias = int(input("¿Cuantas materias has cursado?: "))

for i in range(materias):
    nombre = input("Nombre de la materia: ")
    nota = float(input("Nota de la materia: "))
    lista.append((nombre, nota))

for i in range(materias):
    print(lista[i])

os.system("pause")
os.system("cls")

# Ejercicio 2

print("Ejercicio 2")

lista = []
personas = int(input("¿Cuantas personas desea registrar?: "))

for i in range(personas):
    nombre = input("Nombre: ")
    lista.append(nombre)

for i in range(personas):
    print("Su nombre es:", lista[i])

os.system("pause")
os.system("cls")

# Ejercicio 3

print("Ejercicio 3")

divisa = {'Euro': '€', 'Dollar': '$', 'Yen': '¥'}
divisa_usuario = input("Ingrese la divisa: ")

if not divisa_usuario in divisa:
    print("La divisa no se encuentra en el diccionario")
else:
    valor = float(input("Ingrese valor en pesos a convertir: "))

if divisa_usuario == "€":
    print("El valor en euros es:", valor / 0.00012)

elif divisa_usuario == "$":
    print("El valor en dolares es:", valor / 0.00015)

elif divisa_usuario == "¥":
    print("El valor en yenes es:", valor / 0.016)
else:
    pass

os.system("pause")
os.system("cls")

# Ejercicio 4

print("Ejercicio 4")

Valores = input("Ingrese valores: ")
lista = [Valores]

for i in range(len(lista)):
    if type(lista[i]) == int:
        print("El valor", lista[i], "es entero")
    elif type(lista[i]) == float:
        print("El valor", lista[i], "es decimal")
    elif type(lista[i]) == str:
        print("El valor", lista[i], "es un string")
    elif type(lista[i]) == tuple:
        print("El valor", lista[i], "es una tupla")
    elif type(lista[i]) == list:
        print("El valor", lista[i], "es una lista")
    elif type(lista[i]) == dict:
        print("El valor", lista[i], "es un diccionario")
    else:
        print("El valor", lista[i], "es de otro tipo")

os.system("pause")
os.system("cls")