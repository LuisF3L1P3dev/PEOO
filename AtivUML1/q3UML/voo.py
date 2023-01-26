class Voo():

  class Reserva():

    def __init__(self, valor, voo, passageiro, tipoPagamento):
      self.__valor = valor 
      self.__voo = voo
      self.__passageiro = passageiro
      self.__tipoPagamento = tipoPagamento

    def getVoo(self):
      return self.__voo

    def setVoo(self,voo):
      self.__voo = voo

    def getValor(self):
      return self.__valor

    def getTipoPagamento(self):
      return self.__tipoPagamento

  def __init__(self, codigo, horario, data, aeroportoPartida, aeroportoDestino, tipoVoo, assentos, reservas=[], tripulacao=[]):
    self.__codigo = codigo
    self.__horario = horario
    self.__data = data
    self.__aeroportoPartida = aeroportoPartida
    self.__aeroportoDestino = aeroportoDestino
    self.__tipoVoo = tipoVoo
    self.__assentos = assentos
    self.__reservas = reservas
    self.__tripulacao = tripulacao

  def AssentosLivres(self):

    return int(self.__assentos - len(self.__reservas))

  def NumeroTripulantes(self):

    return len(self.__tripulacao)

  def getReservas(self):
    return self.__reservas

  def setReservas(self, reservas):
    self.__reservas = reservas

  def setTripulacao(self,tripulacao):
    self.__tripulacao = tripulacao

  def getTripulacao(self):
    return self.__tripulacao