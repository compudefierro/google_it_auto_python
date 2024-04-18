frutas = ["manzana", "banana", "naranja", "pera", "kiwi","fresa", "sandia"]
frutas.append("uva")
frutas.append("uva")
frutas.append("uva")
frutas.extend(['manzana', 'naranja'])
frutas.insert(1, "fresa")
# print(frutas)

def remove_duplicates(items):
    seen = []
    duplicates = []

    for item in items:
        if item not in seen:
            seen.append(item)
        else:
            duplicates.append(item)

    return seen, duplicates
resultado = remove_duplicates(frutas)
for item in resultado: print(f'lista curada: {item}')

def convertir_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos - horas * 3600) // 60
    residuo_segundos = segundos -  horas * 3600 - minutos * 60
    return horas, minutos, residuo_segundos

# for leyenda in ['horas: ', 'minutos: ', 'segundos: ']: print(leyenda)
# for item in convertir_segundos(5000): print(item)

lista1 = ['Horas: ', 'Minutos: ', 'Segundos: ']
lista2 = convertir_segundos(5000)

for elemento1, elemento2 in zip(lista1, lista2):
    print(elemento1, elemento2)

animals = ["Lion", "Tiger", "Elephant", "Zebra", "Rhino", "Hippopotamus"]
chars = 0

for animal in animals:
    chars += len(animal)
print('El total de caracteres es: {}, promedio len {}'.format(chars, chars / len(animals)))

personal = ["Jorge", "Raul", "Luis", "Carlos"]
for index, item in enumerate(personal):

    print(index + 1, item)

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
print(full_emails([("5yf0T@example.com", "Jorge"), ("YrU2G@example.com", "Raul")]))