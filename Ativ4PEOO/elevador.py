class Elevador():
    def __init__(self, andarAtual=0, totalAndares=0, capacidadeElevador=0, pessoasNoElevador=0):
        self.__andarAtual = andarAtual
        self.__totalAndares = totalAndares
        self.__capacidadeElevador = capacidadeElevador
        self.__pessoasNoElevador = pessoasNoElevador
    #Andar atual
    def get_andarAtual(self):
        return self.__andarAtual 
    
    def set_andarAtual(self, andarAtual):
        self.__andarAtual = andarAtual

    #Total de andares
    def get_totalAndares(self):
        return self.__totalAndares
    
    def set_totalAndares(self, totalAndares):
        self.__totalAndares = totalAndares
    
    #Capacidade Maxima
    def get_capacidadeElevador(self):
        return self.__capacidadeElevador
    
    def set_capacidadeElevador(self, capacidadeElevador):
        self.__capacidadeElevador = capacidadeElevador
    
    #Pessoas no Elevador
    def get_pessoasNoElevador(self):
        return self.__pessoasNoElevador
    
    def set_pessoasNoElevador(self, pessoasNoElevador):
        self.__pessoasNoElevador = pessoasNoElevador
    
    #classes
    def inicializar(self, capacidadeElevador, totalAndares):
        self.__capacidadeElevador = capacidadeElevador
        self.__totalAndares = totalAndares

    

    def entrar(self):
        '''
        def entrar(self, pessoas):  
            listaPessoas = []
            listaPessoas.append(pessoas)
            quantPessoas = len(listaPessoas)     
            if quantPessoas <= self.__capacidadeElevador:
                self.__pessoasNoElevador += 1;
            else:
                print("Capacidade maxima atingida")
        '''
        if self.__pessoasNoElevador < self.__capacidadeElevador:
            self.__pessoasNoElevador += 1;
            return True
        else:
            print("Capacidade maxima atingida")
            return False

    def sair(self):
        if self.__pessoasNoElevador > 0:
            self.__pessoasNoElevador -= 1
        else:
            print("Não tem ninguem")
    
    def subir(self):
        if self.__andarAtual < self.__totalAndares:
            self.__andarAtual += 1
        else:
            print("Não pode subir para o ultimo andar")
    
    def descer(self):
        if self.__andarAtual > 0:
            self.__andarAtual -= 1
        else:
            print("Não pode descer, está no terreo")
        
    def __str__(self):
        return "Capacidade Maxima: {}\nPessoas no elevador: {}\nTotal de andares: {}\nAndar do Elevador: {}\n".format(self.__capacidadeElevador,self.__pessoasNoElevador,self.__totalAndares, self.__andarAtual)
    '''
    sobrecarga de operadores
    def __add__(self, elevador):
        self.__andarAtual += elevador(self.__andarAtual)
        return "elevador"
    '''

    def __add__(self, other):
        return self.__andarAtual + other.__andarAtual, self.__totalAndares + other.__totalAndares
    
