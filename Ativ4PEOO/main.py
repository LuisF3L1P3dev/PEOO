
from jogador import *

print("__"*10,"Jogador 1","__"*10)
j1 = Jogador("neymar", "meio-campo", 1999, "Brasil", 1.85, 80)
j1.set_altura(1.74)
j1.__str__()
print("idade: ",j1.calcIdade())
j1.aposentar()


print("__"*10,"Jogador 2","__"*10)
j2 = Jogador("Casemiro", "defesa", 1960, "Chile", 1.75, 98)
j2.__str__()
print("idade: ",j2.calcIdade())
j2.aposentar()

print("__"*10,"Jogador 3","__"*10)
j3 = Jogador("Cristiano", "atacante", 1980, "Portugal", 1.90, 87)
j3.__str__()
print("idade: ",j3.calcIdade())
j3.aposentar()

print("__"*10,"Criar jogador","__"*10)
verificacao = 10

listaJogadores = [j1,j2,j3]
'''
aqui queria arranjar uma forma de adiconar objetos em uma lista de forma dinamica
for i in Jogador:
  listaJogadores.append(i)
'''
while(verificacao != "0"):
  print("__"*10,"Time de Futebol","__"*10)
  verificacao = input("1 - Criar jogador\n2 - Listar Jogador \n3 - Remover Jogador \n0 - Sair\n")
  
  if verificacao == "1":
    nome = input("informe o nome do jogador: ")
    posicao = input("informe a posicao: ")
    nascimento = int(input("informe o ano de nascimento: "))
    nacionalidade = input("informe a nacionalidade: ")
    altura = float(input("informe altura: "))
    peso = float(input("informe o peso: "))

    jogador = Jogador(nome, posicao, nascimento, nacionalidade,  altura, peso)
    listaJogadores.append(jogador)

  elif verificacao == "2" :
    for i in listaJogadores:
      print(i)

  elif verificacao == "3" :
    nome = input("informe o nome:")
    for i in listaJogadores:
      if(i.get_nome() == nome):
        listaJogadores.remove(i)

