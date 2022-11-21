from conta import *


#4
#conta = Conta()
#print(type(conta))

#6
#conta = Conta()
#Vai dar um erro pq com o contrutor é obrigado passar os parametros

#7
#conta = Conta('000-000', 'João', 120, 1000.0, '10/04/2002')

#8
#print(conta.numero)
#print(conta.cliente)


#14

#conta.deposita(50.0)
#conta.extrato()
#conta.saca(20.0)
#conta.extrato()

#15
cliente1 = Cliente('luis','dantas', '077777-77')
conta1 = Conta('000-0005', cliente1 , 1150, 50000, '11/08/2005')
print(conta1.extrato(),'\n')

cliente3 = Cliente('davi','dantas', '555555-55')
data3 = Data('2015','05','23')
conta3 = Conta('000-0005', cliente3 , 1150, 50000, data3)
print(conta3.extrato())
print(conta3.data_abertura.data_aber())

cliente4 = Cliente('Davi', 'Costa', "45646-45")
data4 = Data('2022', '06', '24')
conta4 =  Conta('0000-11115', cliente4, 4500, 70000, data4)
print(conta4.extrato())
print(conta4.data_abertura.data_aber())

print("____________________________________")

conta3.transfere_para(conta4, 150)
conta3.transfere_para(conta4, 174)
conta3.transfere_para(conta4, 100)
conta3.deposita(200)
conta3.saca(50)
conta3.saca(50)



print("Extrato Conta 3: ")
conta3.extrato()
print("\nExtrato Conta 4:")
conta4.extrato()

print('__'*10,'HISTORICO','__'*10,'\nConta3: ')
conta3.historico.imprime()
print('\nConta4:')
conta4.historico.imprime()







