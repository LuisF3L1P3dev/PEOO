from aeroporto import Aeroporto
from tripulante import Tripulante
from passageiro import Passageiro
from operador import Operador
from voo import Voo

import datetime

aeroporto1 = Aeroporto("Pau dos Ferros/RN", 10, "Aeroporto Pauferrense")
aeroporto2 = Aeroporto("São Paulo/SP", 20, "São Paulo")

tripulante1 = Tripulante("Davy", 32423, 32432, "Piloto")
tripulante2 = Tripulante("Luis", 32543543, 3121, "Copiloto")

passageiro1 = Passageiro('Damião', 18, 858558, 'Brasil')

voo = Voo(23423,datetime.time(),datetime.date(2023,1,27),aeroporto1,aeroporto2,'nacional',10)
voo.setTripulacao([tripulante1, tripulante2])

ope = Operador("Davi",1000,232,2323,23)

reserva1 = ope.CriarReserva(10,voo, "sdsad", "Cartão")
reserva2 = ope.CriarReserva(100,voo, "sdsad", "Cartão")

reserva3 = passageiro1.CriarReserva(100,voo, passageiro1, "Cartão")
passageiro1.PagarReservas([reserva3])


print("Assentos livres: ",voo.AssentosLivres())

ope.CancelarReserva(reserva1)
passageiro1.CancelarReserva(reserva3)

print("Assentos livre: ",voo.AssentosLivres())

print("Número de tripulantes: {}".format(voo.NumeroTripulantes()))