import time

op = -1
saldo_inicial = 1412.00
saldo_final = 1412.00
limite_saque = 5
depositos = 0
saques = 0
valor_limite_saque = 500


while(op != 0):
    op = int(input(f"""
-------------------- --------------------
|        MENU        |                    |
|                    |      SALDO         |
|    1 - Sacar       |      {saldo_final}        |
|    2 - Depositar   |--------------------
|    3 - Ver saldo   |  LIMITE DE SAQUE   |
|    0 - Sair        |         {limite_saque}          |
-------------------- --------------------
Digite a operação desejada: """))

    if(op == 1):
    
        if(limite_saque > 0):
        
            valor_saque = int(input("Quanto deseja sacar? "))
            if(valor_saque > saldo_final):
                print("Não é possível sacar um valor maior que seu saldo.")
                print("Aguarde...\n")
                time.sleep(2)
            elif(valor_saque <= 0):
                print("Insira um valor maior que R$: 0,00")
                print("Aguarde...\n")
                time.sleep(2)
            else:
                if(((valor_saque + saques) <= valor_limite_saque) and (saques <= valor_limite_saque)):
                    saldo_final -= valor_saque
                    print(f"Você sacou R$: {valor_saque:.2f}.\n Seu saldo é de: R$:{saldo_final:.2f}")
                    
                    limite_saque -= 1
                    saques += valor_saque
                    
                    print("\nAguarde...")
                    time.sleep(2)        
                else:
                    print("Limite de saque ou valor atingido")
                    print("\nAguarde...\n")
                    time.sleep(2)
        else:
            print("Limite de saque ou valor atingido")
            print("\nAguarde...\n")
            time.sleep(2)


    
    elif(op == 2):
        
        valor_deposito = int(input("Quanto  deseja depositar? "))
        if(valor_deposito > 0):
            saldo_final += valor_deposito
            print(f"Você despositou R$: {valor_deposito:.2f}.\nSeu saldo é de: R$: {saldo_final:.2f}")
            depositos += valor_deposito
        else:    
            print("Digite um valor válido\n")
        time.sleep(2)
        
    elif(op == 3):
        print(f"""
Saldo inicial: R$: {saldo_inicial:.2f}
Valor do(s) depósito(s): R$: {depositos:.2f}
Valor do(s) saque(s): R$: {saques:.2f}
Seu saldo atual é de: R$: {saldo_final:.2f}
            """)
        time.sleep(8)
        print("\nAguarde...")
        time.sleep(2)
    elif(op == 0):
        
        print(f"""
    Obrigado por usar nosso sistema.
            """)
        time.sleep(0)
        
    elif isinstance(op, str):
        print("Insira um valor numérico")
