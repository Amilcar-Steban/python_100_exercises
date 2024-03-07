"""
Concatenate three text strings
"""
name = input("Nombre: ")
lastname = input("Apellidos: ")
career = input("Carrera: ")

if not name or not lastname or not career:
    print("Rellene todos los campos")
else:
    def concatenate(name, lastname, career):
        concatenate = f"{name} {lastname}, que genial que estudies {career}"
        return concatenate

result = concatenate(name,lastname,career)

print("Hola! "f"{result}")