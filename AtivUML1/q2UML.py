class Pedido():

    itensPedidos = []

    def __init__(self, valor_total):
        self.valor_total = valor_total

    def adicionar_item(self, item):
        self.itensPedidos.append(item)

        return self.itensPedidos

    def obter_total(self):
        soma = 0
        for i in self.itensPedidos:
            soma += soma + i.valor
        return soma

    class itemPedido():
        def __init__(self, quantidade, produto, pedido):
            self.quantidade = quantidade
            self.produto = produto
            self.pedido = pedido

class Produto():
    def __init__(self, codigo, valor, descricao):
        self.codigo = codigo
        self.valor = valor
        self.decricao = descricao


if __name__ == '__main__':
    
    produto1 = Produto('0104040400', 100, 'creme de barbear')
    produto2 = Produto('fefefefffe', 50, 'gilete MAX')
    produto3 = Produto('777777777', 2000, 'Cadeira')

    pedido1 = Pedido(1000)

    itemP1 = Pedido.itemPedido(2, produto1, pedido1)

    pedido1.adicionar_item(itemP1)

    print(pedido1.obter_total())
