from elevador import *

e1 = Elevador(0, 10, 10, 0)
e2 = Elevador(0, 15, 15, 0)

#0 até 5 , 6 posições
e1.inicializar(5, 10)
e2.inicializar(9, 20)

print("__"*10,"Entrar no Elevador","__"*10)
'''
for i in range(0,3):
    e1.entrar()
    print(e1.get_pessoasNoElevador())
    if e1.entrar() == False:
        break
'''

'''
for i in range(0,7):
    print(e1.get_pessoasNoElevador())
    e1.entrar()

print("__"*10,"Sair do Elevador","__"*10)
e1.sair()
print("\nPessoas no elevador:",e1.get_pessoasNoElevador())

print("__"*10,"Subir o Elevador","__"*10)
for i in range(0,11):
    print("\nAndar Atual",e1.get_andarAtual())
    e1.subir()

print("__"*10,"Descer o Elevador","__"*10)
for i in range(12,0,-1):
    print("\nAndar Atual",e1.get_andarAtual())
    e1.descer()
'''

verificacao = None
while(verificacao != '0'):
    print("__"*10,"ELEVADOR","__"*10)
    print(e1.__str__())

    verificacao = input("\n1-Entrar no Elevador\n2-Sair do Elevador\n3-Subir\n4-Descer\n0-Finalizar\n")
    if verificacao == "1":
        print("\nPessoas no elevador:",e1.get_pessoasNoElevador())
        e1.entrar()
    elif verificacao == "2":
        print("\nPessoas no elevador:",e1.get_pessoasNoElevador())
        e1.sair()
    elif verificacao == "3":
        print("\nAndar Atual",e1.get_andarAtual())
        e1.subir()
    elif verificacao == "4":
        print("\nAndar Atual",e1.get_andarAtual())
        e1.descer()

'''
e1.__add__(e2)
'''
ob3 = e1 + e2
print(ob3)