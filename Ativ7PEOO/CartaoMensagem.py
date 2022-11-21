class CartaoMensagem():

    def __init__(self, destinatarioCartao, mensagem):
        self.__destinatarioCartao = destinatarioCartao
        self.__mensagem = mensagem

    #destinatarioCartao
    def get_destinatarioCartao(self):
        return self.__destinatarioCartao 

    def set_destinatarioCartao(self, destinatarioCartao):
        self.__destinatarioCartao = destinatarioCartao
    
    #mesagem
    def get_mensagem(self):
        return self.__mensagem

    def set_mensagem(self, mensagem):
        self.__mensagem = mensagem

    def __str__(self):
        return "mesagem para {}: {}".format(self.__destinatarioCartao, self.__mensagem)

class MensagemDiaDosNamorados(CartaoMensagem):
    def __init__(self,destinatarioCartao, mensagem ):
        super().__init__(destinatarioCartao, mensagem)
    
class MensagemNatal(CartaoMensagem):
    def __init__(self,destinatarioCartao, mensagem ):
        super().__init__(destinatarioCartao, mensagem) 

class MensagemAniversario(CartaoMensagem):
    def __init__(self,destinatarioCartao, mensagem ):
        super().__init__(destinatarioCartao, mensagem)
       

    