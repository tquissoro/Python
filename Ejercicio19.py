booleano1 = bool(input("Primer valor: "))
booleano2 = bool(input("Segundo valor: "))
booleano3 = bool(input("Tercer valor: "))
booleano4 = bool(input("Cuarto valor: "))
booleano5 = bool(input("Quinto valor: "))
print("Resultado: ", booleano4 or ((booleano3 and not booleano2) and booleano1) or booleano5)
#0=false
#1=true