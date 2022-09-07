num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))
resto1 = num1%2
resto2 = num2%2

if resto1==0 and resto2==0:
    print(num1,"e",num2,"são multiplas de 2")
elif resto1==0 and resto2==1:
    print(num1,"é multiplo de 2 e",num2,"não é")
elif resto1==1 and resto2==0:
    print(num1,"não é multiplo de 2 e",num2," é")
else:
    print("Os dois números não sao multiplos de 2")