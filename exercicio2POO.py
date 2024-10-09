class Pessoa:
    def __init__(self,nome,peso,idade,comendo=False):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=comendo
    def andar(self):
        print(f"{self.nome}Foi andar")

    def comer(self):
        if self.comendo == False:
            print("Foi comer")
            self.comendo=True
        else:
            print("Já esta comendo")
    def dormir(self):
        print("foi dormir")

p1 = Pessoa("Matheus",70,26,)
p1.nome="Matheus Alves"
p1.andar()


c2 = Pessoa("Márcio",70)