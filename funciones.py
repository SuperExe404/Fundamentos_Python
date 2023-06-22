# Funciones de python
# def name_function(parametros):
#   Codigo
#   Return

# Funcion sin parametros y sin retorno
def saludos():
    print("Hola a todos!")

saludos()

# Funciones con un parametro
def get_age_in_future(age):
    print(f" en 3 años tendreas { age + 3} años")

get_age_in_future(39)

# Funciones con 2 parametros sin retorno
def suma(num1, num2):
    print(f"{ num1 } + { num2 } = { num1 + num2 }")

suma(12, 35)

# Funciones con parametros opcionales
def get_heroes(h1 = "Chinoide", h2 = "Pitipulgas"):
    print([h1, h2])

get_heroes()
get_heroes("Patron")
get_heroes("Patron", "Shagy")
get_heroes(h2 = "Patron", h1 = "Shagy")

# Funcion con retorno
def title(texto):
    return texto.title()

text_changed = title("hOlA A tOdOs")
print(text_changed)
