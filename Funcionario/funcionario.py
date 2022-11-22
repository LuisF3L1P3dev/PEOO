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

f1 = Funcionario("carlos",78481515, 2000)
g1 = Gerente("marcos",13516885, 40000, '123', 10)

print("Bonificação funcionario:",f1.get_bonificacao())
print("Bonificação Gerente:",g1.get_bonificacao())