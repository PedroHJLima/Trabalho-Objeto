#Criar dicionário automaticamente

pesquisa = {'AC':[], 'AL':[], 'AP':[], 'AM':[], 'BA':[], 'CE':[], 'DF':[], 'ES':[], 'GO':[], 'MA':[], 'MT':[], 'MS':[], 'MG':[], 'PA':[], 'PB':[], 'PR':[], 'PE':[], 'PI':[], 'RJ':[], 'RN':[], 'RS':[], 'RO':[],
'RR':[], 'SC':[], 'SP':[], 'SE':[], 'TO':[]}

from classe import Relevancia

def validaEstado():
    """Procura a sigla na lista de estados e vê se existe"""
    while True:
        estado = (input("Qual a sigla do estado desejado? ").upper())
        if estado in pesquisa.keys():
            return estado
        else:
            opcaoInvalida()

def escolhaValida(escolha,print):
    """Vê se a nota é um número e se está entre 1 e 5"""
    while True:
        if not escolha.isnumeric() or int(escolha) < 1 or int(escolha) > 5:
            opcaoInvalida()
            escolha = (input(print))
        else:
            return escolha

def realizaPesquisa():
    """Gera as mensagens de pergunta e recebe os valores"""
    desempregoPrint = "De 1 a 5, qual sua preocupação com desemprego?"
    eticaPrint = "De 1 a 5, qual sua preocupação com etica?"
    segurancaPrint = "De 1 a 5, qual sua preocupação com seguranca?"
    regulaPrint = "De 1 a 5, qual sua preocupação com regulamentação?"
    potencialPrint = "De 1 a 5, quanto de potencial você acha que tem?"

    #O motivo de mensagens em variáveis é pra que a função possa imprimir as frases certas e não uma genérica
    desemprego = escolhaValida(input(desempregoPrint),desempregoPrint)
    etica = escolhaValida(input(eticaPrint),eticaPrint)
    seguranca = escolhaValida(input(segurancaPrint),segurancaPrint)
    regulamentacao = escolhaValida(input(regulaPrint),regulaPrint)
    potencial = escolhaValida(input(potencialPrint),potencialPrint)

    return desemprego,etica,seguranca,regulamentacao,potencial

def menu():
    escolha = input("""Menu
0- Finalizar o Programa
1- Realizar avaliação
2- Relatório
3- Esvaziar uma lista\n""")
    return escolha

def media(estado):
    """verifica se o estado existe e tira média"""
    if not pesquisa[estado]:
        opcaoInvalida()
    else:
        #Reset de variáveis
        desempregoTotal,eticaTotal,segurancaTotal,regulamentacaoTotal,potencialTotal = 0,0,0,0,0


        for i in pesquisa[estado]:
            #Looping que passa por todas as listas de um estado pra ir somando as notas
            tamanhoLista = len(pesquisa[estado])

            desempregoTotal += int(i.getTopicos()[0])
            eticaTotal += int(i.getTopicos()[1])
            segurancaTotal += int(i.getTopicos()[2])
            regulamentacaoTotal += int(i.getTopicos()[3])
            potencialTotal += int(i.getTopicos()[4])

        #Transforma tudo em média e devolve num limite de um decimal
        porcentagem_desemprego = ((desempregoTotal / tamanhoLista)).__round__(1)
        porcentagem_etica = ((eticaTotal / tamanhoLista)).__round__(1)
        porcentagem_seguranca = ((segurancaTotal / tamanhoLista)).__round__(1)
        porcentagem_regulamentacao = ((regulamentacaoTotal / tamanhoLista)).__round__(1)
        porcentagem_potencial = ((potencialTotal / tamanhoLista)).__round__(1)

        #Print da porcentagem
        print(f"\nEssas são as médias do estado {estado}\nDesemprego:{porcentagem_desemprego}\n\
Ética:{porcentagem_etica}\nSegurança:{porcentagem_seguranca}\n\
Regulamentação:{porcentagem_regulamentacao}\nPotencial:{porcentagem_potencial}")

def opcaoInvalida():
    input("Opção invalida - Enter para continuar")

"""----------------------------"""

while True:

    escolha = menu()

    if escolha == "1":
        #Realizar a avaliação
        estado = validaEstado()
        formulario = realizaPesquisa()
    
        #print(formulario)
        rlv = Relevancia()
        rlv.setOpiniao(formulario[0],formulario[1],formulario[2],formulario[3],formulario[4])

        pesquisa[estado].append(rlv)
        input(f"Pesquisa adicionada ao estado {estado}\nEnter para continuar:")
        print(rlv)

    elif escolha == "2":
        #Print na porcentagem de cada atributo do estado
        estado = validaEstado()
        media(estado)
        input("Enter para continuar: ")

    elif escolha == "3":
        estado = validaEstado()
        media(estado)
        confirma = input("Tem certeza que deseja apagar? - S para confirmar").upper()
        if confirma == "S":
            pesquisa[estado] = []
            input(f"Estado {estado} esvaziado - Enter para continuar")
        else:
            input("Voltando ao menu, enter para continuar")
        
    elif escolha == "0":
        input("Desligando - Enter para continuar")
        break
    else:
        opcaoInvalida()

    print("\n"*3)
