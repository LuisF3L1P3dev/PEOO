from bombaCombustivel import *

b1 = BombaDeCombustivel("gasolina", 6.30 , 1000)

""" print(b1.tipoCombustivel)
print(b1.valorLitro)
print("Litros da Bomba: ",b1.quantCombustivel) """

car1 = Carro("fiat", 2015, 0, 6)

print("_______Abastecer por litro_______")
b1.abastecerPorValor(6.30, car1)
print(car1.get_abastecer())
print(b1.get_quantCombus())

print("_______Abastecer por Valor_______")
b1.abastecerPorLitro(3, car1)
print(car1.get_abastecer())
print(b1.get_quantCombus())

print("_______alterar Valor Litro_______")
b1.alterarValor(5)
b1.abastecerPorValor(10, car1)
print(car1.get_abastecer())
print(b1.get_quantCombus())

print("_______alterar Tipo Combustivel_______")
b1.alterarCombustivel("Etanol")
print(b1.get_tipoCombus())

print("_______alterar Quantidade de Combustivel na Bomba_______")
b1.alterarQuantidadeCombustivel(1000)
print(b1.get_quantCombus())

print("_______Carro_______")
print(car1.get_modelo(), car1.get_ano())
print("Tanque",car1.get_abastecer(),"L")

car1.percorrer(40)
