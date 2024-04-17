def sumas(num1, num2):
    return num1 + num2

def loops(start, end):
    while start <= end:
        print(sumas(start, end))
        start += 1

loops(1, 10)

def outer(x, y):
    def inner(a, b):
        return a ** b
    return inner(x, y)

result =  outer(2, 4)
print(result)

x = 10
while x != 0 and x % 2 == 0:
    x /= 2
    print(x)
print(x)
for x in range(5):
    print(x)
print(x)
listaAmigos = ['Jorge', 'Osvaldo',  'Claudia','Dri']
for nombre in listaAmigos:
    print(nombre)
print('fin de listaAmigos')

def to_celcius(x):
    return (x - 32) * 5 / 9

def to_fahrenheit(x):
    return (x * 9 / 5) + 32
print(to_celcius(32))
print(to_fahrenheit(32))

for item in range(0, 11):
    print(item, to_celcius(item), to_fahrenheit(item))

print("Dominos game:")
for left in range(7):
    for right in range(7):
        print(f"[{left} | {right}]", end = " ")

teams = [
    'Dragons',
    'Wolves',
    'Pandas',
    'Unicorns'
]

print(" ")
print("TEAMS FIGHTS: ")
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f'{home_team} vs {away_team}')

def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])
greet_friends('Jorge')
greet_friends(['Jorge'])

def recorrer(cadena):
    if len(cadena) == 0:
        return "fin"
    print(cadena[0])  # Imprime el primer carácter de la cadena
    return recorrer(cadena[1:])  # Llama a la función con la cadena sin el primer carácter

recorrer('jorge')

def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n - 1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

print(factorial(6))