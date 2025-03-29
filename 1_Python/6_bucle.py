tabla = int(input("Ingresa la tabla a generar "))
contador = 1

while contador < 11:
    resultado = tabla * contador
    
    print(contador,"*",tabla,"=",resultado)
    
    contador = contador + 1