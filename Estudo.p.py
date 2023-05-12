menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

= > """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

 opcao = input(menu)

if opcao == "d":
    valor = float(input("Informe o valor do depósito"))
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito {valor:.2f}\n"
    else :
        print ("Operação falhou! O valor informado é inválido")
    
elif opcao == "s":
    valor = float(input("Informe o valor do Saque:"))
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques > LIMITE_SAQUES
    
    if excdeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")
        
    elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")
          
    elif excedeu_saques:
        print("Operção falhou!O valor de saque excede o limite")
        
    elif valor > 0:
        saldo -= valor
        extrato += f"Sque: R${valor:.2F}\n"
        numero_saques +=1
        
    else:
        print("Operação falhou! O valor infoormado é invalido ")
          
            

elif opcao == "e":
  print("\nExtrato")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo: R$ {saldo:.2f}")
  print("\n")
 

elif opcao == "q":
    break

else:
    print ("Operação invalida, por favor selecione novamente a opreação desejada")