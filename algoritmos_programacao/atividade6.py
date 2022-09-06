num1 = int(input("Insira o primeira número: "))
num2 = int(input("Insira o segundo número: "))
num3 = int(input("Insira o terceiro número: "))

if num1>0:
    print("A raiz quadrada de",num1, "é de ",num1**0.5)
else:
    print("O quadrado de ",num1,"é de",num1**2,)
if num2>10 and num2<100:
    print("O número está entre 10 e 100-intervalo permitido")
else:
    print(num2,"é menor que 10")
if num3<num2:
    print("O terceiro número é menor que o segundo número, com a diferença de",num2-num3,)
else:
    print("A soma do terceiro e do seugndo número é de",num3+num2)
        