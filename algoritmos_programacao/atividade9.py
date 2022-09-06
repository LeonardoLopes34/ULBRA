from traceback import print_tb


num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1>num2 and num1>num3:
    print("O primeiro número é maior que os outros dois")
elif num2>num1 and num2>num3:
    print("O segundo número é maior que os outros dois")
elif num3>num1 and num3>num2:
    print("O terceiro número é maior que os outros dois")
else:
    print("Os números são iguais")