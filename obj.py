pesquisa = {}

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
    
    def __str__(self):
        return f'Desemprego: {self.__desemprego}, etica: {self.__etica},segurança{self.__seguranca},regulamentação:{self.__regulamentacao},potencial: {self.__potencial}'

rlv01 = Relevancia()

def validaEstado(estado):
    estados_validos = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
'RR', 'SC', 'SP', 'SE', 'TO']
    if estado not in estados_validos:
        input("Estado inválido, tente novamente")

def realizaPesquisa():
    escolha = int(input("qual sua preoucupação com desemprego?"))
    if escolha != 1 or 2 or 3 or 4 or 5:
        input("Opção invalida")
    else:
        desemprego = escolha
    escolha = int(input("qual sua preoucupação com etica?"))
    seguranca = int(input("qual sua preoucupação com seguranca?"))
    regulamentacao = int(input("qual sua preoucupação com regulamentacao?"))
    potencial = int(input("qual sua preoucupação com potencial?"))

    return desemprego,etica,seguranca,regulamentacao,potencial

while True:
    validaEstado(estado = input("Qual a sigla do seu estado?").upper())

    
    
    rlv01.setOpiniao(desemprego,etica,seguranca,regulamentacao,potencial)
    print(rlv01)
    
