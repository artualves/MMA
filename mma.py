from abc import ABC, abstractmethod, ABCMeta

"""

"""

class Lutador(ABC):
    nome = str
    energia = float
    
    def __init__(self, n:str, e:float):
        self.nome = n
        self.energia = e

    def __str__(self):
        return f'Nome: {self.nome}, {self.energia:.2f} %'
    
    def soco(self, oponente):
        oponente.energia -= 5.5

class Boxeador(Lutador):
    def cruzado(self, oponente):
        oponente.energia -= 10.2

    def gancho(self, oponente):
        oponente.energia -= 20.8

class JiuJitsu(Lutador):
    def chave_braco(self, oponente):
        oponente.energia -= 100

class MuayThai(Boxeador):
    def chute_alto(self, oponente):
        oponente.energia -= 15.4

class MMA(JiuJitsu, MuayThai):
    def superman_punch(self, oponente):
        oponente.energia -= 53.2