class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10     

class Autenticavel:

    def autentica(self, senha):
        if self._senha == senha:
            print(self._nome,"autencicado com sucesso")
            return True
        else:
            print('Senha errada tente novamente')
            return False

class Gerente(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000
    '''
    def autentica(self, senha):
        if self._senha == senha:
            print(self._nome,"autencicado com sucesso")
            return True
        else:
            print('Senha errada tente novamente')
            return False
    '''
class Diretor(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha
    '''
    def autentica(self, senha):
        if self._senha == senha:
            print(self._nome,"autencicado com sucesso")
            return True
        else:
            print('Senha errada tente novamente')
            return False
    '''
class Cliente(Autenticavel):
    pass

class SistemaInterno:

    def login(self, funcionario,senha):
        if (hasattr(funcionario, 'autentica')):
            funcionario.autentica(senha)
            # chama método autentica
            return True
        else:
            print('{} não é autenticável'.format(self.__class__.__name__))
            # imprime mensagem de ação inválida 
            return False

class FuncionarioAutenticavel(Funcionario):

    def autentica(self, senha):
        pass



if __name__ == '__main__':
    print()
    f1 = Funcionario("carlos",78481515, 2000)
    g1 = Gerente("marcos",13516885, 40000, '123', 10)
    d1 = Diretor('Half',7484487478,50000,'523')
    system1 = SistemaInterno()
    funAut = FuncionarioAutenticavel('Luis',8948794,1000)
    print("Bonificação funcionario:",f1.get_bonificacao())
    print("Bonificação Gerente:",g1.get_bonificacao())
    #g1.autentica('123')
    print()
    print("Funcionario",system1.login(f1,'023'),"\n")
    print("Gerente",system1.login(g1,'123'),"\n")
    print("Diretor",system1.login(d1,'523'),"\n")
    #no d1 ainda mostra que a senha está errada mas mostra como true, porvavelmente pq na senha do d1 está diferente a da classe login
    print(funAut.autentica(g1))



