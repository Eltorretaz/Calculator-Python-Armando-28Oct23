num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))
select = float(input("Selecciona el operador: 1=+, 2=-, 3=*, 4=/, 5=%"))

if select == 1:
    print("has sumado")
    resultado = num1 + num2
    print(resultado)
if select == 2:
    print("has resta")
    resultado = num1 - num2
    print(resultado)
if select == 3:
    print("has multiplicar")
    resultado = num1 * num2
    print(resultado)
if select == 4:
    print("has dividir")
    resultado = num1 / num2
    print(resultado)
if select == 5:
    print("has sacado el resto")
    resultado = num1 % num2
    print(resultado)  
