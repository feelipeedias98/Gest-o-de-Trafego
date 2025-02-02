
print('''
    _____          _   /\/|             _         ______        _        
  / ____|         | | |/\/             | |      |  ____|       | |       
 | |  __  ___  ___| |_ __ _  ___     __| | ___  | |__ _ __ ___ | |_ __ _ 
 | | |_ |/ _ \/ __| __/ _` |/ _ \   / _` |/ _ \ |  __| '__/ _ \| __/ _` |
 | |__| |  __/\__ \ || (_| | (_) | | (_| |  __/ | |  | | | (_) | || (_| |
  \_____|\___||___/\__\__,_|\___/   \__,_|\___| |_|  |_|  \___/ \__\__,_|
                                                                         ''')

def validar_e_formatar_cpf(cpf):
    if len(cpf) != 11: # Verifica se o CPF tem 11 números
        return None, "Erro: O CPF deve conter exatamente 11 números."

    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"# Formata o CPF no padrão XXX.XXX.XXX-XX
    return cpf_formatado, None

def saudacao (nome):#Função criada para a indentificação do user
    print(f"\nOlá,{nome}, seja bem vindo(a)!!") #printa o nome do user 

def calcular_valor_devolucao(km_inicial, km_devolucao, dias_alugados, diaria, taxa_km=0.5):#Calcula o valor da devolução baseado em km percorridos e dias alugados.
    km_percorridos = km_devolucao - km_inicial
    if km_percorridos < 0:
        return None, "Erro: A quilometragem de devolução não pode ser menor que a quilometragem inicial."
    valor_total = (dias_alugados * diaria) + (km_percorridos * taxa_km)# Calcula o valor total
    return valor_total, km_percorridos

while True :
    nome_usuario = input ("\n Por favor, digite seu nome : ")#input para o user inserir seu nome
    if all(part.isalpha() for part in nome_usuario.split()) : 
        saudacao(nome_usuario)#chama a função saldacao
        break
    else : 
        print("\n Erro: Digite apenas letras para o nome.")

def carro (car) : #Função criada para tratar da seleção co veiculo
    print(f"\nExcelente escolha o modelo {car} ! ")#Printa o modelo do carro escolhido 

print("\n Posso anotar seus dadoos ? isso levará apenas alguns minutos ^^ ")

ficha_cadastral_user = {} #Cria um dicionário vazio para de armazenar os dados do user.

print("\n ========== Ficha Cadastral User  ==========")#Coleta os dados do user para inserir no dicionário vazio

while True:
    ficha_cadastral_user["Nome Completo"] = input("\n Por favor, Digite seu Nome Completo : ")
    if all(part.isalpha() for part in ficha_cadastral_user["Nome Completo"].split()):
        print("Nome cadastrado ^^ .")
        break
    else:
        input("O nome contém caracteres inválidos. Tente novamente.")

while True:
    ficha_cadastral_user["CPF"] = input("\n Por favor, digite seu CPF : ")
    
    if ficha_cadastral_user["CPF"].isdigit(): 
        cpf_formatado, erro = validar_e_formatar_cpf(ficha_cadastral_user["CPF"])
        
        if erro:
            print(erro)  # Exibe a mensagem de erro se o CPF for inválido
        else:
            print(f"\n CPF cadastrado com sucesso: {cpf_formatado}")
            ficha_cadastral_user["CPF"] = cpf_formatado  # Armazena o CPF formatado no dicionário
            break
    else:
        print("\n O CPF contém caracteres não numéricos.")

while True: 
    ficha_cadastral_user["Idade"] = input("\n Por favor, digite sua idade : ")
    if ficha_cadastral_user["Idade"].isdigit():
        print("\n Idade cadastrada ^^ .")
        break
    else:
        print("\n Idade contém caracteres não numéricos.")

while True:
    ficha_cadastral_user["E-mail"] = input("\n Por favor, digite seu e-mail : ")
    if "@" in ficha_cadastral_user["E-mail"] and "." in ficha_cadastral_user["E-mail"]:
        print("\n E-mail cadastrado ^^ .")
        break  
    else:
        print("\n O e-mail é inválido. Tente novamente.")
   
print(" \n =======Informações Cadastradas======= ")
for lista, listacarro in ficha_cadastral_user.items() : #Laço de repetição para ordenar o formato de colunas ao dicionario
    print(f"{lista}:{listacarro}")
        
print("\n Tudo certo, agora por favor selecione o serviço desejado")

from datetime import datetime 

ficha_cadastral_carro = {} #Cria um dicionário vazio para de armazenar os dados relacionados a devolução do carro 

carros_disponiveis = ["Pajero", "Civic", "New Fusca", "Corolla", "Gran Siena","Gol"] #Exibe o modelo dos carros disponiveis para locação 

placa_carros = ["ABC-1234", "FBA-9876", "XYZ-5678", "LMN-4321", "OPQ-8765", "RST-3456"]#Exibe as placas dos carros 

km_carros = [12000, 13345, 18500, 25000, 14200, 9900]#Exibe os Km rodados dos carros 

diaria = [200, 170, 135, 200, 100, 85]

carro_locado = False # váriavel para controlar se existe carro locado ou não 

while True : # laço de repetição para selecionar locação de carro 
    registro = input("\n Para locar um carro, digite 1 ou para devolução do veículo digite 2 ou para sair digite 0 : ")
    
    if registro == '1' : 
        if carro_locado:  # Verifica se já existe um carro locado
            print("\nVocê já possui um carro locado. Para locar um novo veículo, devolva o atual primeiro.")
        else:
            print("\nLista de carros disponíveis:")#printa os carros disponiveis
            carro_locado = True

            for index, modelo in enumerate(carros_disponiveis, start=1):#função enumerate percorre a lista realizando a contagem dos carros 
                print(f"{index}: {modelo}")#Este comando imprime cada modelo de carro junto com seu número correspondente.
           
            opcao= input("\nPor favor pressione o numero do carro que deseja :")#Apresenta a lista de carros disponiveis 
            
            if opcao.isdigit() and 1 <= int(opcao) <= len(carros_disponiveis):#inspeção para garantir que o user digitou um numero int, dentro da realidade da lista
                modelo_escolhido = carros_disponiveis[int(opcao) - 1]#Cria um índice para selecionar o modelo conforme a escolha do usuário
                placa_escolhida = placa_carros[int(opcao) - 1]
                km_escolhido = km_carros[int(opcao) - 1]
                diaria_escolhida= diaria[int(opcao) -1]
                
                carro(modelo_escolhido)#chama a função carro com o modelo escolhido

                print("\n ========== Ficha Cadastral Carro  ==========")
                
                ficha_cadastral_carro["\n Hora da locação"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                ficha_cadastral_carro["\n Modelo escolhido"] = f"{modelo_escolhido}, Placa: {placa_escolhida}, Km: {km_escolhido}, Diária:R${diaria_escolhida},00"
                
                for uso, registrouso in ficha_cadastral_carro.items() : #Laço de repetição para ordenar o formato de colunas ao dicionario
                    print(f"{uso}:{registrouso}")     

                print("\n Cadastro realizado com sucesso, aproveite nossos serviços ^^")
                
    elif registro == '2':  # Opção de devolução
        if not carro_locado:  # Verifica se não há carro locado
            print("\nVocê não possui um carro locado para devolver.")    
        else:
            print("\n Olá, tudo bem ? Chegou o dia da devolução do carro, vamos começar ?")
            for index, modelo in enumerate(carros_disponiveis, start=1):#função enumerate percorre a lista realizando a contagem dos carros 
                    print(f"{index}: {modelo}")#Este comando imprime cada modelo de carro junto com seu número correspondente.
            
            carro_dev = input("Por favor selecione qual carro gostaria de devolver : ")

            if carro_dev.isdigit() and 1 <= int(carro_dev) <= len(carros_disponiveis):#inspeção para garantir que o user digitou um numero int, dentro da realidade da lista
                # modelo_escolhido = carros_disponiveis[int(carro_dev) - 1]
                modelo_selecionado_para_devolver = carros_disponiveis[int(carro_dev) - 1]
                
                if modelo_selecionado_para_devolver != modelo_escolhido:
                    print(f"O modelo que você quer devolver é diferente do que você locou, você locou o {modelo_escolhido}")
                else:
               
                    print("\n ==========Inpeção de Devolução==========")
                    
                km_devolucao = int(input("\nDigite a quilometragem atual do carro: "))
                dias_alugados = int(input("\nInforme o número de dias que ficou com o carro: "))

            valor_total, km_percorridos = calcular_valor_devolucao(km_escolhido, km_devolucao, dias_alugados, diaria_escolhida)

            if valor_total is None:
                print(km_percorridos)  # Exibe a mensagem de erro retornada
            else:
                print(f"\nModelo a ser devolvido: {modelo_escolhido}")#Coleta os dados do user para inserir no dicionário vazio
                ficha_cadastral_carro["\nQuilometros percorridos"] = f"{km_percorridos} Km"
                ficha_cadastral_carro["\nValor total a pagar"] = f": R$ {valor_total:.2f}"
                ficha_cadastral_carro["\nHora da devolução"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")#função para imprimir data e hora att
                ficha_cadastral_carro["\nModelo devolvido"] = f"{modelo_escolhido}, Placa: {placa_escolhida}"
                
                for uso, registrouso in ficha_cadastral_carro.items():
                    print(f"{uso}:{registrouso}")

                print("\nObrigado por utilizar nossos serviços. Devolução concluída com sucesso!")
                ficha_cadastral_carro.clear()# Limpa os dados após a devolução
                carro_locado = False


    elif registro == '0' : #sai do programa 
        print("Obrigado por nos procurar, até uma porxima vez!!!")
        break
    else: 
        print("Opção invalida. Por favor tente novamente.")
    
        
        


    

        
        
        
        

    

        


        
        