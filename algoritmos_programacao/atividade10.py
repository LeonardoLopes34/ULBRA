conta = int(input("Insira o número da conta bancária: "))
saldo = int(input("Insira o saldo da conta bancária: "))

if saldo<=0:
    print("A conta bancária ",conta,"está com a conta estourada")
else:
    print("A conta bancária",conta,"está com conta normal")