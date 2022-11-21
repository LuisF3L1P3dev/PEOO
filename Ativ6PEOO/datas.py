import datetime as dt

class data():
    today = dt.date.today()
    def __init__(self, dia = today.day , mes = today.month, ano= today.year):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
    #dia
    def get_dia(self):
        return self.__dia

    def set_dia(self, dia):
        self.__dia = dia
    #mes
    def get_mes(self):
        return self.__mes

    def set_mes(self, mes):
        self.__mes = mes
    #ano
    def get_ano(self):
        return self.__ano

    def set_dia(self, ano):
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)
    
    def avancarDia(self):
        if self.__dia + 1 > 30: 
            self.__dia = 1
            if self.__mes + 1 > 12:
                self.__dia = 1
                self.__mes = 1
                self.__ano +=1
            else:
                self.__mes += 1
        else:
            self.__dia +=1

    def verificarAnoBissexto(self):
        if self.__ano %4 == 0:
            return "{} é Bissexto".format(self.__ano)
        else:
            return "{} não é Bissexto".format(self.__ano) 
    """  
    def __add__(self, other):
        if other == type(data):
            return data(self.__dia + other.__dia, self.__mes + other.__mes, self.__ano + other.__ano)
        else:
            return avancarDia(other)
    """

    def __add__(self, other):
        novoDia = 0
        novoMes = 0
        novoAno = 0
        #quando dia maior que 30
        if self.__dia + other.__dia > 30:
            novoDia = (self.__dia + other.__dia) - 30
            novoMes = self.__mes + 1
            if self.__mes + other.__mes > 12:

                self.__mes =  (self.__mes + other.__mes)-12
                
d1 = data()
print("Data Atual:",d1.__str__())

d1.avancarDia()
print("Dia avançado:",d1.__str__(),"\n")

'''
Para facilitar os meses 
foram definidos com 30 dias
'''
d2 = data(30,12,2004)
print("Data Definida:",d2.__str__())
d2.avancarDia()
print("Avançando dia e mudando ano:",d2.__str__(), "\n")

print(d1.verificarAnoBissexto())
print(d2.verificarAnoBissexto())
d3 = data(14,5,2004)
print(d3.verificarAnoBissexto())
print("")

d4 = d1 + d2
print("soma de:", d1.__str__(),"+",d2.__str__(),"=",d4)

#ta dando erro nessa parte
d3.__add__(3) 








