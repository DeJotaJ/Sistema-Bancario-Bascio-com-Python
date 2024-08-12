import time

op = -1

def sacar(*, valor_saque, valor_limite_saque, limite_saque, saldo_final, saques):
    
    if(limite_saque > 0):
        
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

    return saldo_final, saques, limite_saque

def depositar(saldo_final, depositos, valor_deposito):    
    if(valor_deposito > 0):
        saldo_final += valor_deposito
        depositos += valor_deposito
        print(f"Você depositou R$: {valor_deposito:.2f}.\nSeu saldo é de: R$: {saldo_final:.2f}")
    else:    
        print("Digite um valor válido\n")
    
    return saldo_final, depositos
    
def extrato(saldo_inicial, saldo_final,/, depositos, saques):
    print(f"""
Saldo inicial: R$: {saldo_inicial:.2f}
Valor do(s) depósito(s): R$: {depositos:.2f}
Valor do(s) saque(s): R$: {saques:.2f}
Seu saldo atual é de: R$: {saldo_final:.2f}
            """)
    return saldo_inicial, saldo_final, saques, depositos
    time.sleep(8)
    print("\nAguarde...")
    time.sleep(2)

def criarUsuario(nomeUsuario, dataNasc, cpf, endereco,/, usuarios):
    
    idade = 0
    print("="*50)
    idade = (2024 - int(dataNasc))
    usuario = {"nome":nomeUsuario, "idade":idade, "CPF":cpf, "endereco":endereco}
    usuarios.append(usuario)
    
    for indice in usuarios:
        
        for chave in indice:
            space = 12 - len(chave)
            print(f"{chave}{' '*space}: {indice[chave]}")
    
    print("="*50)

    return usuarios

def criarCC(ag, numConta, usuario, contas):

    for c in contas:
        print(c["Numero da conta"])
        if c["Numero da conta"] == numConta:
            c["Numero da conta"] == numConta + 1
    
    conta = {"Agência":ag, "Numero da conta":numConta, "Usuario":usuario}
    contas.append(conta)
    
    for indice in contas:
        
        for chave in indice:
            space = 12 - len(chave)
            print(f"{chave}{' '*space}: {indice[chave]}")
    
    print("="*50)

    return contas

def main():
    
    AG = "0001"
    saldo_inicial = 1412.00
    saldo_final = 1412.00
    limite_saque = 5
    depositos = 0
    saques = 0
    valor_limite_saque = 500
    listaUsuarios = []
    listaContas = []
    nConta = 0
    
    while True:
        
        op = int(input(f"""
 ------------------- ----------------------------
|           MENU            |                    |
|                           |      SALDO         |
|       1 - Sacar           |      {saldo_final}        |
|       2 - Depositar       |--------------------|
|       3 - Extrato         |  LIMITE DE SAQUE   |
|       4 - Criar Usuario   |                    |
|       5 - Criar Conta     |                    |
|       6 - Consultar Conta |                    |
|       0 - Sair            |         {limite_saque}          |
 ------------------- ----------------------------
Digite a operação desejada: """))

        #SACAR
        if(op == 1):
            
            valor = int(input("Quanto deseja sacar? "))
            saldo_final, saques, limite_saque = sacar(
                valor_saque=valor, 
                valor_limite_saque=valor_limite_saque, 
                limite_saque=limite_saque, 
                saldo_final=saldo_final, 
                saques=saques)
        
        #DEPOSITAR    
        elif(op == 2):
            
            valor_deposito = int(input("Quanto  deseja depositar? "))
            saldo_final, depositos = depositar(saldo_final, depositos, valor_deposito)
            time.sleep(2)
        
        #VER EXTRATO
        elif(op == 3):
        
            print(extrato(saldo_inicial, saldo_final, depositos = depositos, saques = saques))
            time.sleep(5)
        
        #CRIANDO USUÁRIO
        elif(op == 4):
            
            nomeUsuario = input("Digite seu nome\n==> ")
            dataNasc = input("Digite o ano de nascimento\n==> ")
            cpf = input("Digite seu CPF(Sem .  ou -)\n==>")
            endereco = input("Digite seu endereço seguindo o seguinte modelo\n logradouro, nº - bairro - cidade/sigla do estado\n==>")
            
            listaUsuarios = criarUsuario(nomeUsuario, dataNasc, cpf, endereco, listaUsuarios)
        
        elif(op == 5):
            
            ag = AG
            nConta += 1
            numConta = nConta
            usuario = input("Digite seu CPF(Sem .  ou -)\n==>")
            
            listaContas = criarCC(ag, numConta, usuario, listaContas)
        
        elif(op == 6):
            
            usuario = input("Digite seu CPF(Sem .  ou -)\n==>")
            for conta in listaContas:
                if(usuario == conta["Usuario"]):
                    print(conta)
                else:
                    print("Conta não encontrada")
            
        elif op == 0 :

            break
    
main()