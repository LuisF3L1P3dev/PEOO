class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def get_bonificacao(self):
        return self._salario * 0.10     

class Gerente(Funcionario):

    def __init__(self, nome, cpf, salario, senha, qtd_gerenciaveis):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis

    def get_bonificacao(self):
        return super().get_bonificacao() + 1000

    def autentica(self, senha):
        if self._senha == senha:
            print(self._nome,"autencicado com sucesso")
            return True
        else:
            print('Senha errada tente novamente')
            return False

class Diretor(Funcionario):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    def autentica(self, senha):
        if self._senha == senha:
            print(Gerente,"autencicado com sucesso")
        else:
            print('Senha errada tente novamente')
            
class SistemaInterno:

    def login(self, funcionario):
        if (hasattr(funcionario, 'autentica')):
            funcionario.autentica(' ')
            # chama método autentica
            return True
        else:
            print('ação inválida ')
            # imprime mensagem de ação inválida 
            return False



if __name__ == '__main__':
    print()
    f1 = Funcionario("carlos",78481515, 2000)
    g1 = Gerente("marcos",13516885, 40000, '123', 10)
    d1 = Diretor('Half',7484487478,50000,'321'
    )
    system1 = SistemaInterno()
    print("Bonificação funcionario:",f1.get_bonificacao())
    print("Bonificação Gerente:",g1.get_bonificacao())
    g1.autentica('123')

    print(system1.login(g1))
