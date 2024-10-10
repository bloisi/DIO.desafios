def main():

    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[n] Conta
[l] Listar Contas
[u] Usuario
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    usuario_lista = []
    conta_lista = []

    AGENCIA = "0001"

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo, extrato = deposito(saldo, valor, extrato)               

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            if valor > 0:
                saldo, extrato = saque(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            extrato_tela(saldo, extrato)

        elif opcao == "u":
            usuario_cadastro(usuario_lista)    

        elif opcao == "n":
            num_conta = len(conta_lista) + 1
            conta = conta_cadastro(AGENCIA, num_conta, usuario_lista)

            if conta:
                conta_lista.append(conta)

        elif opcao == "l":                
            conta_listagem(conta_lista)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


def deposito(saldo, valor, extrato):
    saldo = saldo + valor
    extrato = extrato + str(valor) + " C\n"

    return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):

    if valor > saldo:
        print ("Valor de saque excedido !")

    elif valor > limite:    
        print ("Limite de saque excedido !")

    elif numero_saques > limite_saques:    
        print ("Quantidade de saques excedido !")

    else:    
        saldo = saldo - valor
        extrato = extrato + str(valor) + " D\n"
        numero_saques = numero_saques + 1

    return saldo, extrato

def extrato_tela(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

def usuario_cadastro(usuario_lista):
    usuario_cpf = input("Informe o CPF: ")

    usuario = usuario_pesquisa(usuario_cpf, usuario_lista)

    if usuario:
        print("Uusuário já cadastrado !")
        return 

    usuario_nome = input ("Informe o nome: ")
    usuário_nascimento = input ("Informe a data de nascimento: ")
    usuario_endereco = input("Informe o endereço: ")

    usuario_lista.append({"usuario_cpf": usuario_cpf, "usuario_nome": usuario_nome,  "usuário_nascimento": usuário_nascimento, "usuario_endereco":usuario_endereco})
    print("Usuário cadastrado !")

def usuario_pesquisa(cpf,lista_usuario):
    usuario_retorno = [usuario for usuario in lista_usuario if usuario["usuario_cpf"]==cpf]
    return usuario_retorno[0] if usuario_retorno else None

def conta_cadastro(agencia, conta, lista_usuario):
    cpf = input("Informe o CPF: ")
    usuario = usuario_pesquisa(cpf, lista_usuario)

    if usuario:
        print("Conta cadastrada !")
        return{"agencia": agencia, "conta": conta, "usuario": usuario}
    else:
        print("Usuário não cadastrado !")

def conta_listagem(conta_lista):
    for conta in conta_lista:
        tela = f"""\ 
                "AG: " {conta['agencia']}
                "CC: " {conta['conta']}
                "Cliente: " {conta['usuario']}
                """
        print (tela)

main()        