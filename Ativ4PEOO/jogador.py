import datetime as dt
from datetime import date
class Jogador():
    def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
        self.__nome = nome
        self.__posicao = posicao
        self.__nascimento = nascimento
        self.__nacionalidade = nacionalidade
        self.__altura = altura
        self.__peso = peso
    #nome
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome

    #posicao
    def set_posicao(self, posicao):
        self.__posicao = posicao
    
    def get_posicao(self):
        return self.__posicao

    #nascimento
    def set_nascimento(self, nascimento):
        self.__nascimento = nascimento
    
    def get_nascimento(self):
        return self.__nascimento

    #nacionalidade
    def set_nacionalidadeo(self, nacionalidade):
        self.__nacionalidade = nacionalidade
    
    def get_nacionalidade(self):
        return self.__nacionalidade
    
    #altura
    def set_altura(self, altura):
        self.__altura = altura

    def get_altura(self):
        return self.__altura

    #peso
    def set_peso(self, peso):
        self.__peso = peso

    def get_peso(self):
        return self.__peso

    def calcIdade(self):
        '''
        Também da certo só que é mais codigo:
        date = dt.date.today()
        year = date.strftime("%Y")
        idade = (int(year)) - (int(self.__nascimento))
        print(self.__nome,"tem",f"{idade} anos ")
        '''
        return date.today().year - self.__nascimento
  
    def aposentar(self):
        '''
        podemos ver que uma função está sendo usada dentro de outra função no codigo
            aposentar():
                calcIdade():
        '''
        idade = self.calcIdade()
        if self.__posicao == "defesa" :
            if idade >= 40:
                return("jogador pode pendurar as chuteiras\n")
            else:
                return("Faltam "+str(40 - idade)+" anos para o jogador se aposentar")
        if self.__posicao == "meio-campo":
            if idade >=38:
                return("jogador pode pendurar as chuteiras\n")
            else:
                return("Faltam "+str(38 - idade)+" anos para o jogador se aposentar")
        if self.__posicao == "atacante":
            if idade >= 35:
                return("jogador pode pendurar as chuteiras\n")
            else:
                return("Faltam "+(35 - idade)+" anos para o jogador se aposentar")

    def __str__(self):
        return "Nome: {} \nPosicao: {}\nNascimento: {}\nNacionalidade: {}\nAltura: {}\nPeso: {}\nAposentadoria: {}\nIdade: {}\n".format(self.__nome, self.__posicao, self.__nascimento, self.__nacionalidade ,self.__altura, self.__peso, str(self.aposentar()), self.calcIdade())

        

    

