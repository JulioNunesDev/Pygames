class Cachorro:
    def __init__(self, nome_cao, idade_cao, raca_cao, tamanho_cao):
        self.nome_cao = nome_cao
        self.idade_cao = idade_cao
        self.raca_cao = raca_cao
        self.tamanho_cao = tamanho_cao


    def latir(self):
        print(f'{self.nome_cao} está latindo')
    
    def correr(self):
        print(f'{self.nome_cao} está correndo')


caramelo = Cachorro('Caramelo', 1, 'luxo', 'medio')
print(caramelo.nome_cao)
caramelo.latir()