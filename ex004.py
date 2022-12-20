x = input("digite algo: ")

print(f"tipo primitivo: {type(x)}")
print(f"só tem espaços? {x.isspace()}")
print(f"é um número? {x.isnumeric()}")
print(f"é alfabetico? {x.isalpha()}")
print(f"é alfanumérico? {x.isalnum()}")

print(f"está em maiúsculas? {x.isupper()}")
print(f"está em minúsculas? {x.islower()}")
print(f"está capitalizada? {x.istitle()}")
