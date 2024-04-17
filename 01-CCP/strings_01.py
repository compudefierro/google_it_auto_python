def replace_domain(email, old_domain, new_domain):
    """
    Replaces the domain of an email address with a new domain.

    Args:
        email (str): The email address to modify.
        old_domain (str): The current domain of the email address.
        new_domain (str): The new domain to replace the old domain with.

    Returns:
        str: The modified email address with the new domain, or the original email address if the old domain is not found.
    """
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("jorge@example.com", "gmail.com", "example.com"))
print(replace_domain("jorge@gmail.com", "gmail.com", "example.com"))

cadena = "Me llamo Jorge y tengo 2 hijos"
print(f'La frase es: {cadena}')

# Solicitar al usuario las palabras a reemplazar
palabra_original = input("Ingrese la palabra original: ")
palabra_nueva = input("Ingrese la palabra nueva: ")

# Reemplazar la palabra original por la nueva en la cadena
cadena_modificada = cadena.replace(palabra_original, palabra_nueva)

# Imprimir la cadena modificada
print("Cadena original:", cadena)
print("Cadena modificada:", cadena_modificada)

cadena = "Me llamo Jorge y tengo 2 hijos"
print(f'La frase es: {cadena}')
# Solicitar al usuario las palabras a reemplazar
palabra_original = input("Ingrese la palabra original: ")
palabra_nueva = input("Ingrese la palabra nueva: ")

# Dividir la cadena en palabras
palabras = cadena.split()

# Reemplazar la palabra original por la nueva
for i in range(len(palabras)):
    if palabras[i] == palabra_original:
        palabras[i] = palabra_nueva

# Unir las palabras nuevamente en una cadena
cadena_modificada = ' '.join(palabras)

# Imprimir la cadena modificada
print("Cadena original:", cadena)
print("Cadena modificada:", cadena_modificada)

