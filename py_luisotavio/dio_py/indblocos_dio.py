saldo = 2500
saque = 1000
cheque_especial = 400

conta_normal = False
conta_universitaria = True

if conta_normal: 

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com cheque especial!")
    else:
        print("Não foi possivel sacar seu dinheiro...")

elif conta_universitaria:

    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")