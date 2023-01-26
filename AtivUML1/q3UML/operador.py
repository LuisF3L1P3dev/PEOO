class Operador():

  def __init__(self, nome, salario, rg, endereco, telefone):
    self.__nome = nome
    self.__salario = salario
    self.__rg = rg
    self.__endereco = endereco
    self.__telefone = telefone

  def CriarReserva(self, valor, voo, passageiro, tipoPagamento):

    if voo.AssentosLivres() > 0:

      reserva = voo.Reserva(valor, voo, passageiro, tipoPagamento)
      vooReservas = voo.getReservas()
      vooReservas.append(reserva)
      voo.setReservas(vooReservas)
      return reserva
    
    else:
      return print("Sem assentos livres")


  def CancelarReserva(self,reserva):
    voo = reserva.getVoo()
    reservas = voo.getReservas()
    reservas.remove(reserva)
    voo.setReservas(reservas)