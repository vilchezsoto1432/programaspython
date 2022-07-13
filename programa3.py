def retornar_superficie(lado1,lado2):
    superficie=lado1*lado2
    return superficie

print("Primer Rectangulo")
lado1=int(input("Ingrese el lado mayor del rectangulo:"))
lado2=int(input("Ingrese el lado menor del rectangulo"))
print("segundo rectangulo")
lado3=int(input("Ingrese el lado menor del rectangulo:"))
lado4=int(input("Ingrese el lado mayor del rectangulo:"))
if retornar_superficie(lado1, lado2)==retornar_superficie(lado3, lado4):
    print("Los dos rectangulos tienen la misma superficie")
else:
    if retornar_superficie(lado1, lado2)> retornar_superficie(lado3, lado4):
        print("El primer rectangulo tiene una superficie mayor")
    else:
        print("El segundo rectangulo tiene una superficie mayor")