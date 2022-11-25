from datetime import date, datetime

class Cliente:
        
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
    pass

#5

    def __init__(self, numero, cliente, saldo, limite, data_abertura):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo
        self.limite = limite
        self.data_abertura = data_abertura
        self.historico = Historico()
#9
    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append('Deposito de {}'.format(valor))

#10
    #def saca(self, valor):
    #    self.saldo -= valor
#11
    #def extrato(self):
    #    print("numero: {}\nSaldo: {}".format(self.numero, self.saldo))

#12
    def saca(self, valor):
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True
#13 
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para conta {}".format(valor, destino.numero))
            return True
#15           
    

    def extrato(self):
        #print("numero: {}\nSaldo: {}\nNome: {}\ncpf: {}".format(self.numero, self.saldo, self.cliente.nome, self.cliente.cpf))
        print("Numero: {}\nSaldo: {}\nNome: {}\nCPF: {}".format(self.numero, self.saldo, self.cliente.nome, self.cliente.cpf),'\n')
        #print("numero: {}\nSaldo: {}".format(self.numero, self.saldo, Cliente.nome, Cliente.cpf ))
        self.historico.transacoes.append("tirou extrato - saldo de {}".format(self.saldo))

#16

class Data:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def data_aber(self):
        print("dia: {} ,mes: {} ,ano: {} ".format(self.day, self.month, self.year))

#17
class Historico:

    def __init__(self):
        self.data_abertura = datetime.today()
        self.transacoes = []
    
    def imprime(self):
        print('Data abertura: {}'.format(self.data_abertura))
        print('transações: ')

        for i in self.transacoes:
            print("-", i)

#Atividade 8 - Herança e Polimorfismo - Alura
'''
1 - Adicione na classe Conta um novo método chamado atualiza() que atualiza a conta de acordo com a taxa percentual:
'''

def atualiza(self, taxa):
    self.__saldo += self.__saldo * taxa

        


    