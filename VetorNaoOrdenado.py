class VetorNaoOrdenado:
    def __init__(self, capacidadeVetor):
        self.capacidadeVetor = capacidadeVetor
        self.tamanhoVetor = 0
        self.vetor = []

    def incluir(self, elementoVetor):
        if not isinstance(elementoVetor, int):
            print("Foi inserido um elemento inválido. Por favor, insira um número inteiro.")
        elif self.tamanhoVetor == self.capacidadeVetor:
            print("Capacidade máxima do vetor foi atingida.")
            return
        else:
            self.vetor.append(elementoVetor)
            self.tamanhoVetor += 1
            print(f"Este é o seu vetor {self.vetor}")
 
    def remover(self, elementoVetor):
        if self.tamanhoVetor == 0:
            print("O vetor está vazio. Não é possível remover elementos.")
            return
        elif not isinstance(elementoVetor, int):
            print("Foi inserido um elemento inválido. Por favor, insira um número inteiro.")
            return
        elif elementoVetor not in self.vetor:
                print("Não há esse número em seu vetor") 
                print(f"Este é o seu vetor {self.vetor}")
        else:
            self.vetor.remove(elementoVetor)
            self.tamanhoVetor -= 1
            print(f"Este é o seu vetor {self.vetor}")

#Exemplo de Uso
vetor = VetorNaoOrdenado(3)
vetor.incluir(2)
vetor.incluir(25)
vetor.remover(3)
vetor.incluir(8)
vetor.incluir(10)
