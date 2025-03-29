while True:
    print("Calculadora sencilla")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Raíz cuadrada (sqrt)")
    print("6. Potencia (^))")
    print("7. Salir")

    # Pedir al usuario la opción
    opcion = input("Selecciona una operación (1/2/3/4/5/6/7): ")
    
    if opcion == '7':
        print("Hasta luego")
        break

    # Pedir números
    numUno = float(input("Ingresa el primer número: "))
    numDos = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = numUno + numDos
        print(f"Resultado: {numUno} + {numDos} =  {resultado}")
    elif opcion == '2':
        resultado = numUno - numDos
        print(f"Resultado: {numUno} - {numDos} =  {resultado}")
    elif opcion == '3':
        resultado = numUno * numDos
        print(f"Resultado: {numUno} * {numDos} =  {resultado}")
    elif opcion == '4':
        if numDos != 0:
            resultado = numUno / numDos
            print(f"Resultado: {numUno} / {numDos} =  {resultado}")
        else:
            print("No se puede dividir entre cero")
            
    elif opcion == '5':
        if numUno >= 0:
            resultado = numUno ** 0.5
            print(f"Resultado: {numUno} sqrt =  {resultado}")

    elif opcion == '6':
        resultado = numUno ** numDos
        print(f"Resultado: {numUno} ^ {numDos} = {resultado}")
        
    else:
        print("Opción no valida.")