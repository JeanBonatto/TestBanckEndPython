class ArrayPaisCapital:
    def __init__(self, pais, capital): #Fazendo a inicialização da classe, pelos seus dois objetos
        self.pais = pais
        self.capital = capital
        self.Array = [[pais, capital]]  # Armazenar os pares país-capital em uma lista

    def __repr__(self):
        return f"{self.pais} - {self.capital}"
    

# Inclui um novo par país e capital à lista
    def incluirPaisAndCapital(self, pais, capital):
        self.Array.append([pais, capital])  
        print("País e Capital incluidos com sucesso. Este é o seu Array com Países e Capitais: ",self.Array)

# Ordenar a lista pelo nome do país
    def ordenarPais(self):
        self.Array.sort(key=lambda x: x[0])  
        print(f"Este é o seu Array com Países e Capitais ordenados pelo País: {self.Array}")

# Ordenar a lista pelo nome da capital
    def ordenarCapital(self):
        self.Array.sort(key=lambda x: x[1])  
        print(f"Este é o seu Array com Países e Capitais ordenados pela Capital: {self.Array}")



# Exemplo de Uso, com a inclusão de mais de 8 Objetos (País e sua respectiva Capital)
array = ArrayPaisCapital("Brasil", "Brasília")          # 1º País e Capital
array.incluirPaisAndCapital("Argentina","Buenos Aires") # 2º País e Capital
array.incluirPaisAndCapital("Paraguai","Assunção")      # 3º País e Capital
array.incluirPaisAndCapital("Uruguay","Montevidéu")     # 4º País e Capital
array.incluirPaisAndCapital("Equador","Quito")          # 5º País e Capital
array.incluirPaisAndCapital("Chile","Santiago")         # 6º País e Capital
array.incluirPaisAndCapital("Peru","Lima")              # 7º País e Capital
array.incluirPaisAndCapital("Colômbia","Bogotá")        # 8º País e Capital
array.incluirPaisAndCapital("Venezuela","Caracas")      # 9º País e Capital
array.ordenarPais()
array.ordenarCapital()
