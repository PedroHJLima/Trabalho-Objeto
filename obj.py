pesquisa = {'AC':[], 'AL':"", 'AP':"", 'AM':"", 'BA':"", 'CE':"", 'DF':"", 'ES':"", 'GO':"", 'MA':"", 'MT':"", 'MS':"", 'MG':"", 'PA':"", 'PB':"", 'PR':"", 'PE':"", 'PI':"", 'RJ':"", 'RN':"", 'RS':"", 'RO':"",
'RR':"", 'SC':"", 'SP':"", 'SE':"", 'TO':""}

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
    
    def getOpiniao(self):
        return self.__desemprego, self.__etica, self.__seguranca, self.__regulamentacao, self.__potencial


    def __str__(self):
        #Seta o objeto como string quando printar
        return f'Desemprego: {self.__desemprego}, etica: {self.__etica},segurança{self.__seguranca},regulamentação:{self.__regulamentacao},potencial: {self.__potencial}'



def validaEstado(estado):
    #Procura a sigla na lista de estados e vê se existe
    print (pesquisa.keys())
    while True:
        if estado in pesquisa.keys():
            return estado
        else:
            input("Estado inválido, digite novamente: ")
            estado = validaEstado(input("Qual a sigla do seu estado?").upper())
            


def escolhaValida(escolha,print):
    #Vê se a nota está entre 1 e 5
    while True:
        if escolha < 1 or escolha > 5 :
            input("Opção invalida - enter")
            escolha = escolhaValida(int(input(print)),print)
        else:
            return escolha


def realizaPesquisa():
    #Gera as mensagens de pergunta e recebe os valores
    desempregoPrint = "Qual sua preocupação com desemprego?"
    eticaPrint = "Qual sua preocupação com etica?"
    segurancaPrint = "Qual sua preocupação com seguranca?"
    regulaPrint = "Qual sua preocupação com regulamentação?"
    potencialPrint = "Qual sua preocupação com potencial?"

    desemprego = escolhaValida(int(input(desempregoPrint)),desempregoPrint)
    etica = escolhaValida(int(input(eticaPrint)),eticaPrint)
    seguranca = escolhaValida(int(input(segurancaPrint)),segurancaPrint)
    regulamentacao = escolhaValida(int(input(regulaPrint)),regulaPrint)
    potencial = escolhaValida(int(input(potencialPrint)),potencialPrint)

    return desemprego,etica,seguranca,regulamentacao,potencial


while True:
    estado = validaEstado(input("Qual a sigla do seu estado?").upper())
    formulario = realizaPesquisa()
    
    print(formulario)
    rlv = Relevancia()
    rlv.setOpiniao(formulario[0],formulario[1],formulario[2],formulario[3],formulario[4])

    #pesquisa.({estado: rlv})
    #print(pesquisa[estado])