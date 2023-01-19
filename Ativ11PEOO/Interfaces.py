from Ativ9PEOO/Mix_Ins import Funcionario, Cliente, Conta, Diretor,Gerente, SistemaInterno, FuncionarioAutenticavel
import abc

class Autenticavel(abc.ABC):
    """Classe abstrata que contém operações de um objeto autenticável.
    As subclasses concretas devem sobrescrever o método autentica
    """

    @abc.abstractmethod
    def autentica(self, senha):
        """ Método abstrato que faz verificação da senha.
        Devolve True se a senha confere, e False caso contrário.
        """

if __name__ == '__main__':
    Autenticavel.register(Gerente)
    gerente = Gerente('João', '111111111-11', 3000.0)
    print(isinstance(Autenticavel))
    print(issubclass(Autenticavel))