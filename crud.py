drinks = []

def add_drink(drink):
    drinks.append(drink)

def del_drink(drink):
    try:
        drinks.remove(drink)
    except Exception:
        print("No existe en la lista")

def show_drinks():
    print("-" * 4, "My Drinks", "-" * 4)
    for drink in drinks:
        print("-->", drink)

choise_text = '''
Elige una Opción:
    1 - Agregar
    2 - Eliminar
    3 - Mostrar 
    4 - Salir
'''

while True:
    choise_user = int(input(choise_text))
    if choise_user == 1:
        drink = input('Ingresa un tipo de pisto:')
        add_drink(drink)
    elif choise_user == 2:
        drink = input('Ingresa un tipo de pisto:')
        del_drink(drink)
    elif choise_user == 3:
        show_drinks()
    elif choise_user == 4:
        break
    else:
        print('Opción Incorrecta')