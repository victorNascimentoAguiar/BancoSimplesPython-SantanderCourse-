menu = """ 

[d] Depositar
[s] Sacar
[e] Extato
[f] Finalizar seção
"""

saldo = 0
limite = 500
extrato = ""
numeroDeSaques = 0
limiteDeSaques = 3

while True:
    opcao = input(menu)
#operacao feita para armezanar o valor dito pelo usuario
    if opcao == 'd':
        print('Deposito')

        entradaDeposito = input('digite o valor que deseja depositar: ')
        try:
            ValorDeposito = int(entradaDeposito)

            #verifica se o valor e valido 
            if ValorDeposito is not None and ValorDeposito >= 0:
                saldo = saldo + ValorDeposito
                print(f'voce acabou de depositar R${ValorDeposito:.2f} seu saldo agore e de R${saldo:.2f}')
                #caso nao seja valido retorna mensgem
            else:
                print('valor invalido')
        except ValueError:
            print('Valor invalido. porfavor digite um valor valido')
    #oporacao de saque onde o usuario pode sacar o dinheiro que antes havia depositado 
    elif opcao == 's':
        print('Sacando')
        entradaSacar = input('digite o valor que deseja sacar: ')
        try:
            
            valorSacar = int(entradaSacar)
            #validacoes para verificar se o usuario esta valido para sacar o dinheiro
            if valorSacar <= limite and numeroDeSaques <= limiteDeSaques and valorSacar <= saldo:
                numeroDeSaques += 1
                limite = limite - valorSacar
                saldo = saldo - valorSacar
                saquesDisponiveis= limiteDeSaques - numeroDeSaques
                print(f'Valor a Sacar R${valorSacar} limite diario de saque {saquesDisponiveis} Saldo disponivel R${saldo}')
            else:
                print(f'operacao nao pode ser realiazada: limite de saques diario {saquesDisponiveis} limite diario de saque R${limite} seu saldo atual R${saldo}')                  
        except ValueError:
            print('Valor invalido. porfavor digite um valor valido')
    #mostra o extrato da conta com as informacoes nescessarias
    elif opcao == 'e':
        print('extrato')
        print (f"""
        
        Saldo da conta : R${saldo}
        limite diario de saque R${limite} 
        vezes que ainda pode sacar {saquesDisponiveis}


               """)
        #comando para finalizar o programa
    elif opcao == 'f':
        print('finalizando')
        break
    #cheka se a opcao esta valida
    else:
        print('Operacao invalida')


