from conta import *

cliente1 = Cliente('luis','dantas', '077777-77')
conta1 = Conta('000-0005', cliente1 , 1150, 50000, '11/08/2005')
conta1.extrato()

cliente2 = Cliente('Damiao','Teodosio', '88888-888')
conta2 = Conta('000-0004', cliente2 , 800, 2500, '09/02/2005')
conta2.extrato()

cliente3 = Cliente('davi','dantas', '555555-55')
data3 = Data('2015','05','23')
conta3 = Conta('000-0005', cliente3 , 1150, 50000, data3)
conta3.extrato()
conta3.data_abertura.data_aber()

cliente4 = Cliente('Davi', 'Costa', "45646-45")
data4 = Data('2022', '06', '24')
conta4 =  Conta('0000-11115', cliente4, 4500, 70000, data4)
