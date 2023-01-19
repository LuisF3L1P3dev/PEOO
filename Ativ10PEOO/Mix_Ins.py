from datetime import date, datetime

class Cliente:
        
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

class Conta:
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
    #Atividade 8 - Herança e Polimorfismo - Alura
    '''
    1 - Adicione na classe Conta um novo método chamado atualiza() que atualiza a conta de acordo com a taxa    percentual:
    '''
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa
        return self.saldo

    def __str__(self):
        return "Dados da conta:\nNumero: {}\nTitular: {} {}\nSaldo: {}\nLimite: {}\n".format(self.numero, self.cliente.nome, self.cliente.sobrenome, self.saldo, self.limite)
#16

class Data:

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def data_aber(self):
        print("dia: {} mes: {} ano: {} ".format(self.day, self.month, self.year))

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

class Tributavel:

    def get_valor_imposto(self):
        pass

class TributavelMixIn:

    def get_valor_imposto(self):
        pass

class ContaCorrente(Conta, TributavelMixIn):

    def atualiza(self, taxa):
        return super().atualiza(taxa * 2) 
    
    def deposita(self, valor):
        return super().deposita(valor - 0.10)
    
    def get_valor_imposto(self):
        return self.saldo * 0.01

class ContaPoupanca(Conta):
   def atualiza(self, taxa):
        return super().atualiza(taxa * 3) 

class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice):
        self._valor = valor
        self._titular = titular
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05

'''
Vamos criar uma classe que seja responsável por fazer a atualização de todas as contas bancárias e gerar um relatório com o saldo anterior e saldo novo de cada uma das contas. Na pasta src, crie a classe AtualizadorDeContas
'''
class AtualizadorDeContas():
    def __init__(self, selic, saldo_total=0):
        self.selic = selic
        self.saldo_total = saldo_total

    def roda(self, conta):
        print("Saldo da Conta: {}".format(conta.saldo))
        self.saldo_total += conta.atualiza(self.selic)
        print("Saldo Final: {}".format(self.saldo_total))

