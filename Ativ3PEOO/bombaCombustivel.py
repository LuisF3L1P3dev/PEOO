class BombaDeCombustivel:
    
    def __init__(self, tipoCombustivel, valorLitro, quantCombustivel):
        self.__tipoCombustivel = tipoCombustivel
        self.__valorLitro = valorLitro
        self.__quantCombustivel = quantCombustivel

    def abastecerPorValor(self, valor, carro):       
        carro.set_abastecer(valor/self.__valorLitro)
        self.__quantCombustivel -= (valor/self.__valorLitro)
        print("Foi adicionado ", valor/self.__valorLitro ," L de", self.__tipoCombustivel )

    def abastecerPorLitro(self, litros, carro):
        carro.set_abastecer(litros)
        self.__quantCombustivel -= litros
        print("O valor a ser pago R$: ", litros * self.__valorLitro,"de", self.__tipoCombustivel )

    def alterarValor(self, valor):
        self.__valorLitro = valor
    
    def alterarCombustivel(self, tipoCombustivel):
        self.__tipoCombustivel = tipoCombustivel
    
    def alterarQuantidadeCombustivel(self, quantCombustivel):
        self.__quantCombustivel += quantCombustivel

    def get_quantCombus(self):
        return self.__quantCombustivel

    def get_tipoCombus(self):
        return self.__tipoCombustivel 

class Carro:
    def __init__(self, modelo, ano, tanque, kmPorLitro):
        self.__modelo = modelo
        self.__ano =  ano
        self.__tanque = tanque
        self.__kmPorLitro = kmPorLitro
    
    def get_modelo(self):
        return self.__modelo

    def get_ano(self):
        return self.__ano

    def set_abastecer(self, quantidadeCombustivel):
        self.__tanque += quantidadeCombustivel

    def get_abastecer(self):
        return self.__tanque

    def percorrer(self, distancia):
        if(self.__tanque >= distancia/self.__kmPorLitro):
            self.__tanque -= distancia/self.__kmPorLitro
            print("O carro percorreu", distancia ,"Km, o tanque está com", self.__tanque, "L" )
        else:
            print("O carro percorreu ", self.__tanque * self.__kmPorLitro ,"Km")
            self.__tanque = 0


    def get_percorrer(self):
        pass