class Relevancia:
    def __init__(self):
        self.__topicos = {
            "Desemprego":0,
            "Etica":0  ,
            "Seguranca":0,
            "Regulamentacao":0,
            "Potencial":0
        }

    def setOpiniao(self,desemprego,etica,seguranca,regulamentacao,potencial):
        """Seta os dados da pesquisa"""
        self.__topicos[0] = desemprego
        self.__topicos[1] = etica
        self.__topicos[2] = seguranca
        self.__topicos[3] = regulamentacao
        self.__topicos[4] = potencial
    
    #get em cada atributo pra ter a porcentagem de cada um
    def getTopicos(self):
        """Busca os dados da pesquisa"""
        return self.__topicos

    def __repr__(self):
        """Transforma a pesquisa em uma string pra print"""
        #Por conta do obj estar dentro de uma lista, o __str__ não funciona, tem q ser repr
        return f'Desemprego: {self.__topicos[0]}, etica: {self.__topicos[1]},segurança{self.__topicos[2]},regulamentação:{self.__topicos[3]},potencial: {self.__topicos[4]}'