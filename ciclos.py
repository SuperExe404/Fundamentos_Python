# ciclos while
# While Exp_bool: True

i = 1
num = 7
while i <= 10:
    print(f"{ num } * { i } = { num * 1}")
    i += 1

# Ciclo infinito
while True:
    # Rompemos con break
    break 
#else:
#    print("Ciclo terminado")
# El for correcto iterable
# Un iterable es algo que se puede recorrer

# for variable in iterable
my_string = "Hola"
for letra in my_string:
    print(letra, end=", ")

print()

lista = ["uno", "dos", "tres", "cuatro"]
for item in lista:
    print(item)

# funcion range
# range (end)
for i in range(10):
    print(i, end=', ')
print()
# range (ini, end)
for i in range(10, 20):
    print(i, end=', ')
print()
# range (ini, end, step)
for i in range(10, 20 ,2):
    print(i, end=', ')
print()
