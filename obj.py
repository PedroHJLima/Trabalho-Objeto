pesquisa = {'AC':[], 'AL':[], 'AP':[], 'AM':[], 'BA':[], 'CE':[], 'DF':[], 'ES':[], 'GO':[], 'MA':[], 'MT':[], 'MS':[], 'MG':[], 'PA':[], 'PB':[], 'PR':[], 'PE':[], 'PI':[], 'RJ':[], 'RN':[], 'RS':[], 'RO':[],
'RR':[], 'SC':[], 'SP':[], 'SE':[], 'TO':[]}

class Relevancia:
    def __init__(self):
        self.__desemprego = None
        self.__etica = None
        self.__seguranca = None
        self.__regulamentacao = None
        self.__potencial = None

    def setOpiniao(self,desemprego,etica,seguranca,regulamentacao,potencial):
        self.__desemprego = desemprego
        self.__etica = etica
        self.__seguranca = seguranca
        self.__regulamentacao = regulamentacao
        self.__potencial = potencial
    
    def calcularSomaTotal(self):
        # Calculando a soma total dos atributos
        return sum([int(self.__desemprego), int(self.__etica), int(self.__seguranca), int(self.__regulamentacao), int(self.__potencial)])

    def getDesemprego(self):
        return int(self.__desemprego)
    def getEtica(self):
        return int(self.__etica)
    def getSeguranca(self):
        return int(self.__seguranca)
    def getRegulamentacao(self):
        return int(self.__regulamentacao)
    def getPotencial(self):
        return int(self.__potencial)
    

    """porcentagem_desemprego = (self.__desemprego / soma_total) * 100
    porcentagem_etica = (self.__etica / soma_total) * 100
    porcentagem_seguranca = (self.__seguranca / soma_total) * 100
    porcentagem_regulamentacao = (self.__regulamentacao / soma_total) * 100
    porcentagem_potencial = (self.__potencial / soma_total) * 100"""


    def __str__(self):
        #Seta o objeto como string quando printar
        return f'Desemprego: {self.__desemprego}, etica: {self.__etica},segurança{self.__seguranca},regulamentação:{self.__regulamentacao},potencial: {self.__potencial}'
    
    def __repr__(self):
        #Por conta do obj estar dentro de uma lista, o __str__ não funciona, tem q ser repr
        return f'Desemprego: {self.__desemprego}, etica: {self.__etica},segurança{self.__seguranca},regulamentação:{self.__regulamentacao},potencial: {self.__potencial}'



def validaEstado(estado):
    #Procura a sigla na lista de estados e vê se existe
    while True:
        if estado in pesquisa.keys():
            return estado
        else:
            input("Estado inválido, enter para continuar: ")
            estado = validaEstado(input("Qual a sigla do seu estado? ").upper())
            


def escolhaValida(escolha,print):
    #Vê se a nota é um número e se está entre 1 e 5
    while True:
        if not escolha.isnumeric() or int(escolha) < 1 or int(escolha) > 5:
            input("Opção inválida - pressione Enter")
            escolha = (input(print))
        else:
            return escolha


def realizaPesquisa():
    #Gera as mensagens de pergunta e recebe os valores
    desempregoPrint = "Qual sua preocupação com desemprego?"
    eticaPrint = "Qual sua preocupação com etica?"
    segurancaPrint = "Qual sua preocupação com seguranca?"
    regulaPrint = "Qual sua preocupação com regulamentação?"
    potencialPrint = "Qual sua preocupação com potencial?"

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
2- Relatório\n""")
    return escolha

"""----------------------------"""

while True:
    print("\n"*3) #Quebra linha todo menu
    escolha = menu()

    if escolha == "1":
        #Realizar a avaliação
        estado = validaEstado(input("Qual a sigla do seu estado?").upper())
        formulario = realizaPesquisa()
    
        #print(formulario)
        rlv = Relevancia()
        rlv.setOpiniao(formulario[0],formulario[1],formulario[2],formulario[3],formulario[4])

        print(rlv)
        pesquisa[estado].append(rlv)
        print(pesquisa[estado].__str__())

    elif escolha == "2":
        estado = validaEstado(input(f"Qual estado deseja ver a porcentagem?").upper())
        somaTotal, desempregoTotal,eticaTotal,segurancaTotal,regulamentacaoTotal,potencialTotal = 0,0,0,0,0,0


        for i in pesquisa[estado]:
            somaTotal += i.calcularSomaTotal()

            desempregoTotal += i.getDesemprego()
            eticaTotal += i.getEtica()
            segurancaTotal += i.getSeguranca()
            regulamentacaoTotal += i.getRegulamentacao()
            potencialTotal += i.getPotencial()

        porcentagem_desemprego = (desempregoTotal / somaTotal) * 100
        porcentagem_etica = (eticaTotal / somaTotal) * 100
        porcentagem_seguranca = (segurancaTotal / somaTotal) * 100
        porcentagem_regulamentacao = (regulamentacaoTotal / somaTotal) * 100
        porcentagem_potencial = (potencialTotal / somaTotal) * 100

        print(f"Desemprego:{porcentagem_desemprego}\n\
Ética:{porcentagem_etica}\nSegurança:{porcentagem_seguranca}\n\
Regulamentação:{porcentagem_regulamentacao}\nPotencial:{porcentagem_potencial}")

    elif escolha == "0":
        input("Desligando - Enter para continuar")
        break
    else:
        input("Opção invalida, enter para continuar")
