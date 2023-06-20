# Tuplas
# (item1, item2, itemN)
# Inmutables
my_tuple = ("uno", 2, 3.1416, False)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
# Error
# my_tuple[0] = "nuevo Valor"

# Conjunto Set
# {item1, item2, itemN}
# Coleccion sin indice y sn duplicados 

my_set = {1, 2, 2, 2, 3, 4, "uno"}
print(type(my_set))
print(my_set)
my_set.add(5)

a = {1, 2, 3, 4}
b = {4, 5, 6, 7}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Diccionarios
# { item1: valor, otem2: valor}

alumno = {
    "name": "Shagy",
    "apellido": "Lozano",
    "edad": 19,
    "genero": "Elicoptero Apache",
    "calificaciones": [10, 0.1, 8]
}
print(type(alumno))
print(alumno)
print(alumno["name"], alumno["apellido"])
if alumno["edad"] < 18:
    print("Es menor de edad")
alumno["calificaciones"].append(10)
print(alumno["calificaciones"])