from CartaoMensagem import CartaoMensagem, MensagemAniversario, MensagemDiaDosNamorados, MensagemNatal

listaMgs = []

m1 = CartaoMensagem("luis", "Quando se ama alguém, ama-se, e quando não se tem nada mais lhe dar, ainda se lhe dá amor")
'''
print(m1.get_destinatarioCartao())
print(m1.get_mensagem())
'''
m2 = MensagemDiaDosNamorados("Davi","Essa peça que você queria")
'''
print(m2.get_destinatarioCartao())
print(m2.get_mensagem())
'''
m3 = MensagemAniversario("Damis", "Só tenho duas palavras pra falar para você para-bains")
'''
print(m3.get_destinatarioCartao())
print(m3.get_mensagem())
'''
m4 = MensagemNatal("Moises", "Vou olhar os stories de Paulo Muzy, feliz natal!!")
'''
print(m4.get_destinatarioCartao())
print(m4.get_mensagem())
'''

listaMgs.append(m1)
listaMgs.append(m2)
listaMgs.append(m3)
listaMgs.append(m4)


for msg in listaMgs:
    print(msg)
verificacao = 10

while(verificacao != 0):
    print("__"*10,"Caixa de Mensagem","__"*10)
    verificacao = int(input("1-Criar mensagem\n2-Listar\n0-Sair\n"))
    if verificacao == 1:
        
        verificacao = int(input("Escolha o tipo de mensagem:\n3-Dia dos namorados\n4-Mensagem de Natal\n5-Mensagem de Aniversario\n"))

        if verificacao == 3:
            nome = input("nome:")
            mensagem = input("mensagem: ")
            mNamorados = MensagemDiaDosNamorados(nome, mensagem)
            listaMgs.append(mNamorados)

        if verificacao == 4:
            nome = input("nome:")
            mensagem = input("mensagem: ")
            mNatal = MensagemNatal(nome, mensagem)
            listaMgs.append(mNatal)

        if verificacao == 5:
            nome = input("nome:")
            mensagem = input("mensagem: ")
            mAniversario = MensagemAniversario(nome, mensagem)
            listaMgs.append(mAniversario)

    elif verificacao == 2:
        for msg in listaMgs:
            print(msg)


