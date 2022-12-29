'''
Crie um programa para representa um blog. O blog contém várias postagens que
são cadastradas por usuários auten;cados. Siga o diagrama de classes abaixo para
a implementação:
'''
import datetime

class Usuario:
    
    def __init__(self, id: int, nome: str, login: str, senha: str):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha

class Postagem:
    def __init__(self, id: int, titulo: str, texto: str, dataPublicacao: datetime()):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.dataPublicacao = dataPublicacao
        

class Blog:
    
    def __init__(self):
        postagens = []
    

    def adcionarPostagem(self, postagem:Postagem):
        #if type(postagem) == self.postagem:
        self.postagens.append(postagem)

    def publicarPostagem(self, postagem:Postagem):
        for i in self.postagens:
            if i.id == postagem.id:
                return postagem.id