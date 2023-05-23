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

    #get em cada atributo pra ter a porcentagem de cada um
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
    
    def __repr__(self):
        #Por conta do obj estar dentro de uma lista, o __str__ não funciona, tem q ser repr
        return f'Desemprego: {self.__desemprego}, etica: {self.__etica},segurança{self.__seguranca},regulamentação:{self.__regulamentacao},potencial: {self.__potencial}'