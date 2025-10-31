
# Hecho por Samir Parra, Kenion Reales, Alexis Borrero, Johan Caro.

#️⃣ 1️⃣ Representación con tuplas para las cartas de una baraja
# Cada carta será una tupla con (número, palo)
# Ejemplo: (7, "Corazones")

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]

baraja = []
for palo in palos:
    for numero in numeros:
        baraja.append((numero, palo))

print("Baraja de cartas completa:")
print(baraja)


#️⃣ 2️⃣ Verificar si las cartas forman un póker
def poker(cartas):
    for carta in cartas:
        if cartas.count(carta) == 4:
            return "¡Es un póker!"
    return "No es un póker"

# Pedimos las 5 cartas al usuario
cartas = []
for i in range(5):
    carta = input(f"Ingrese el valor de la carta {i+1}: ")
    cartas.append(carta)

# Verificamos si es póker
resultado = poker(cartas)
print(resultado)


#️⃣ 3️⃣ Calcular el producto escalar de dos vectores
def producto_escalar(v1, v2):
    if len(v1) != len(v2):
        print("Los vectores no tienen la misma longitud.")
        return 

    producto = 0
    for i in range(len(v1)):
        producto += v1[i] * v2[i]
    
    return producto

v1 = [2, 3, 4]
v2 = [1, 0, -1]

resultado = producto_escalar(v1, v2)
print("El producto escalar es:", resultado)


#️⃣ 4️⃣ Verificar si dos vectores son ortogonales
# Si son ortogonales sale True, si no lo son False
def verificaciondeortogonales(v1, v2):
    total = 0
    for i in range(len(v1)):
        total += v1[i] * v2[i]
    return total

def son_ortogonales(v1, v2):
    if len(v1) != len(v2):
        return False
    return verificaciondeortogonales(v1, v2) == 0

v1 = [1, 2, -2]
v2 = [2, -1, 1]

print(son_ortogonales(v1, v2))  # True o False


#️⃣ 5️⃣ Verificar si dos vectores son paralelos
# Si no son paralelos sale False, y si son paralelos sale True
def paralelos(v1, v2):
    if len(v1) != len(v2):
        return False

    if v1 == [0] * len(v1) and v2 == [0] * len(v2):
        return True

    for i in range(len(v1)):
        if v2[i] != 0:
            k = v1[i] / v2[i]
            break
    else:
        return False

    for i in range(len(v1)):
        if v1[i] != v2[i] * k:
            return False

    return True

v1 = [8, 10, 6]
v2 = [4, 5, 3]
print(paralelos(v1, v2))


#️⃣ 6️⃣ Calcular la norma de un vector
def norma(vector):
    suma = 0
    for componente in vector:
        suma = suma + componente ** 2
    norma = suma ** 0.5
    print("La norma del vector es:", norma)

# Ejemplo de uso
v = [3, 4]
norma(v)


#️⃣ 7️⃣ Separar una lista según un número k
# Devuelve tres listas: menores, mayores, iguales, y otra con múltiplos
x = int(input("Ingrese un número para validar: "))
lista1 = [num for num in range(1, 31)]
lista2 = [num for num in lista1 if num > x]
lista3 = [num for num in lista1 if num < x]
lista4 = [num for num in lista1 if num == x]
lista5 = [num for num in lista1 if num % x == 0]

print("Lista de números:", lista1)
print(f"Números mayores de {x}:", lista2)
print(f"Números menores de {x}:", lista3)
print(f"Números iguales a {x}:", lista4)
print(f"Números múltiplos de {x}:", lista5)
