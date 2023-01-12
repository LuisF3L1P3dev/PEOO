'''
Crie um programa para representa um blog. O blog contém várias postagens que
são cadastradas por usuários auten;cados. Siga o diagrama de classes abaixo para
a implementação:
'''
from datetime import datetime
from datetime import timedelta

class Usuario:

    def __init__(self, id: int, nome: str, login: str, senha: str):
        self.id = id
        self.nome = nome
        self.login = login
        self.senha = senha

class Postagem:

    def __init__(self, id: int, titulo: str, texto: str, dataPublicacao):
        self.id = id
        self.titulo = titulo
        self.texto = texto
        self.dataPublicacao = dataPublicacao
        

class Blog:
    
    def __init__(self):
        self.postagens = []

    def adcionarPostagem(self, postagem):
        #if type(postagem) == self.postagem:
        self.postagens.append(postagem)

    def publicarPostagem(self, postagem):     
        postagem.dataPublicacao = datetime.now()
        for i in self.postagens:
            if i.id == postagem.id:
                return postagem.id
    
    def listarPostagensPublicadas(self):
        postagensPublicadas = []
        for i in self.postagens:
            if i.dataPublicacao  < datetime.now():
                postagensPublicadas.append(postagem)
            return postagensPublicadas
    
    def listarTodasAsPostagens(self):
        return self.postagens

    def apagarPostagens(self, postagem):
        for i in self.postagens:
            if i.id == postagem.id:
                self.postagens.remove(postagem)

if __name__ == "__main__":
    user1 = Usuario(1, 'luis', 'luis', '1234')
    post1 = Postagem(1, 'economia', 'oioiioi', '14/05/2022')
    #post2 = Postagem(2, 'saúde', 'caracois', datetime.now())
    post3 = Postagem(3, 'educação', 'abelhas', '31/12/2022')
    blog1 = Blog()

    #add postagem
    blog1.adcionarPostagem(post1)
    blog1.adcionarPostagem(post3)

    #publicar postagem
    print(blog1.publicarPostagem(post1))

    #listar Postagens Publicadas
    blog1.listarPostagensPublicadas()

    #listar Todas As Postagens
    blog1.listarTodasAsPostagens()

    #Apagar todas as postagens
    blog1.apagarPostagens(post1)