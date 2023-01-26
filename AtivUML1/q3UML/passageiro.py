class Passageiro():

  def __init__(self, nome, idade, telefone, passaporte, reservas=[]):
    self.__nome = nome 
    self.__idade = idade
    self.__telefone = telefone
    self.__passaporte = passaporte
    self.__reservas = reservas

  def CancelarReserva(self,reserva):

      voo = reserva.getVoo()
      reservas = voo.getReservas()
      reservas.remove(reserva)
      voo.setReservas(reservas)

  def CriarReserva(self, valor, voo, passageiro, tipoPagamento):

    if voo.AssentosLivres() > 0:

      reserva = voo.Reserva(valor, voo, passageiro, tipoPagamento)
      self.__reservas.append(reserva)

      return reserva
    
    else:
      return print("Sem assentos livres")
  
  def PagarReservas(self, reservas:list() ):
    #somente quando o passageiro paga a reserva ela é validada no voo
    for i in reservas:
      voo = i.getVoo()
      if voo.AssentosLivres() > 0:
        
        valor = i.getValor()
        formaPagamento = i.getTipoPagamento()
        print("Pagamento de R${} efetuado em {}".format(valor, formaPagamento))

        reservasVoo = voo.getReservas()
        reservasVoo.append(i)
        voo.setReservas(reservasVoo)


