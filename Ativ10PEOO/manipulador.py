class ManipuladorDeTributaveis():
    def calcula_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        return total

if __name__ == '__main__':
    from Mix_Ins import ContaCorrente, SeguroDeVida, TributavelMixIn

    cc1 = ContaCorrente('123-4', 'João', 1000.0, 5000.0, '14/02/22')
    cc2 = ContaCorrente('123-4', 'José', 1000.0, 6000.0, '15/03/21')
    seguro1 = SeguroDeVida(100.0, 'José', '345-77')
    seguro2 = SeguroDeVida(200.0, 'Maria', '237-98')

    lista_tributaveis = []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)

    manipulador = ManipuladorDeTributaveis()
    total = manipulador.calcula_impostos(lista_tributaveis)

    print(total)

