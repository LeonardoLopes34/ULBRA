from re import I


num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if num1>num2:
    print("O primeiro número",num1,"é maior que o segundo número",num2,)
elif num2>num1:
    print("O segundo número",num2,"é maior que o primeiro número",num1,)
else:
    print("Os dois números são iguais")
    