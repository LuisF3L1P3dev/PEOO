from datetime import datetime

class Pessoa:
    def __init__(self, nome, sexo, data_nas):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nas = data_nas
    
    def __str__(self):
        return "{}\n{}\n{}\n".format(self.__nome, self.__sexo, self.__data_nas)

class Aluno(Pessoa):
    def __init__(self, nome, sexo, data_nas, matric):
        super().__init__( nome, sexo, data_nas)
        self.__matric = matric

class Ator(Pessoa):

    class Contrato():
        def __init__(self, inicio, fim, salario):
            self.__inicio = inicio
            self.__fim = fim
            self.__salario = salario

    def __init__(self, nome, sexo, data_nas, inicio, fim, salario):
        super().__init__(nome, sexo, data_nas)
        self.__contrato = self.Contrato(inicio, fim, salario)

class Personagem(Ator):
    def __init__(self, nome, sexo, data_nas, caracterizacao, novela):
        super().__init__(nome, sexo, data_nas)
        self.__caracterizacao = caracterizacao
        self.__novela = novela



if __name__ == "__main__":
    inicio = datetime(2020, 5, 17)
    fim = datetime(2023, 1, 1)
    salario = 6000
    ator = Ator('Damião', 'm', '20/04/2003',inicio,fim,salario)

    p1 = Pessoa('liuis', 'm', '14/05/2002' )
    a1 = Aluno("davi", 'm', '07/06/2000', '20221094040016')
    at1 = Ator('Damião', 'm', '20/04/2003', 'Mecanico')
    per1 = Personagem('Maria', 'f', '08/07/1997', 'Barman', 'O clone')

    print(p1.__str__())