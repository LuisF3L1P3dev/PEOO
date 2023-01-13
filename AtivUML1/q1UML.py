'''
Crie um programa para representa um blog. O blog contém várias postagens que
são cadastradas por usuários auten;cados. Siga o diagrama de classes abaixo para
a implementação:
'''
from datetime import datetime, date
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
        
    def __str__(self):
        return('id: {}\ntitulo: {}\ntexto: {}\ndataPublicacao: {}\n'.format(self.id, self.titulo, self.texto, self.dataPublicacao))
        
class Blog:

    postagensPublicadas = []

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
        for i in self.postagens:
            if i.dataPublicacao < datetime.now():
                self.postagensPublicadas.append(i)
            else:
                print('data errada')
        
        return self.postagensPublicadas
    
    def listarTodasAsPostagens(self):
        return self.postagens

    def apagarPostagens(self, postagem):
        for i in self.postagens:
            if i.id == postagem.id:
                self.postagens.remove(postagem)
    '''
    def loginUsers(self):
        login = str(input('login: '))
        senha = str(input('senha: ')) 
        if login == self.login() and senha == self.senha():
     '''   


if __name__ == "__main__":
    user1 = Usuario(1, 'luis', 'luis', '1234')
    post1 = Postagem(1, 'economia', 'oioiioi', datetime(2022, 5, 20))
    post2 = Postagem(2, 'saúde', 'caracois', datetime.now())
    post3 = Postagem(3, 'educação', 'abelhas', date(2022, 12, 31))
    blog = Blog()

    #add postagem
    print('_____Postagens:_____ ')
    blog.adcionarPostagem(post1)
    blog.adcionarPostagem(post2)
    blog.adcionarPostagem(post3)

    print(post1.__str__())
    print(post2.__str__())
    print(post3.__str__())

    #publicar postagem
    print('_____Publicar postagens:_____ ')
    print(blog.publicarPostagem(post1))
    print(blog.publicarPostagem(post2))
    print(blog.publicarPostagem(post3))

    #listar Postagens Publicadas
    print('_____Listar Postagens Publicadas:_____ ')
    for p in blog.listarPostagensPublicadas():
        print('x')
        print(p)
    
    #listar Todas As Postagens
    print('-------listar Todas As Postagens:------')  
    for p in blog.listarTodasAsPostagens():
        print(p)
    #Apagar todas as postagens
    blog.apagarPostagens(post1)

    listUsers = [user1] #lista de usuarios autenticados
    verificacao = None

    while verificacao != 0:
        verificacao = int(input('1-Criar usuario\n2-Usuario Cadastrado\n0-sair\n'))
        if verificacao == 1:
            
            id = input('id: ')
            nome = str(input('nome: '))
            login = str(input('login: '))
            senha =  str(input('senha: '))

            user = Usuario(id, nome, login, senha)
            listUsers.append(user)

        #caso o usuario já estivar cadastrado, vai poder fazer os procedimentos.

        if verificacao == 2:
            print('Usuarios:')
            login = str(input('login: '))
            senha = str(input('senha: '))

            for i in listUsers:
                print(' ',i.id,'-',i.nome,'\n')

                if login == i.login and senha == i.senha:          

                    verificacao = int(input('3-Adiconar Postagem:\n4-Publicar Postagens:\n5-Listar Postagens Publicadas:\n6-Listar Todas as Postagens\n7-Apagar Postagens\n8-voltar\n'))

                    if verificacao == 3:
                        pass

                    if verificacao == 4:
                        pass

                    if verificacao == 5:
                        pass

                    if verificacao == 6:
                        pass

                    if verificacao == 7:
                        pass

                    if verificacao == 8:
                        pass
                
                else:
                    print('senha e login incorretos tente novamente')

            


