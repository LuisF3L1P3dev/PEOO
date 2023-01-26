

class Aeroporto():
  
  def __init__(self, localizacao, maxDecolagensHora, nome, operadores=[]):
    self.__localizacao = localizacao
    self.__maxDecolagensHora = maxDecolagensHora
    self.__nome = nome
    self.__operadores = operadores
