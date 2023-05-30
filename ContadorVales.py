class ContadorVales:
    def __init__(self, passos, caminho):
        self.passos = passos
        self.caminho = caminho
        self.vale = 0

    def contadorVales(self):
        if self.passos != len(self.caminho):
            print("Precisa que o número de passos e a quantidade de 'D' e 'U' do caminho, seja igual")
        else:
        #Verificador se é subida ou descida
            contador = 0 #Inicialização do contador
            for i in self.caminho:
        # Se o caminho for igual a U, ele sobre
                if i == "U":
                    contador += 1
            #Se ao estiver subido ele chegar a 0, então ele percoreu um vale
                    if contador == 0:
                        self.vale +=1            
                # Se o caminho for igual a D, ele desce
                else:
                    i == "D"
                    contador -= 1
                   
        print(" A quantida de vales é :", self.vale)
#Exemplos de Uso
passos=12
caminho= "DDUUDDUDUUUD"
#retorno=2
qtdeVales = ContadorVales(passos, caminho)
qtdeVales.contadorVales()

passos=10
caminho= "DUDDDUUDUU"
qtdeVales = ContadorVales(passos, caminho)
qtdeVales.contadorVales()
#retorno=2

passos=100
caminho="DUDUUUUUUUUDUDDUUDUUDDDUUDDDDDUUDUUUUDDDUUUUUUUDDUDUDUUUDDDDUUDDDUDDDDUUDDUDDUUUDUUUDUUDUDUDDDDDDDDD"
qtdeVales = ContadorVales(passos, caminho)
qtdeVales.contadorVales()
#retorno=2

#Quantidade de Passos e caminhos está divergente
passos=9 #Colocado 9 para verificação
caminho= "DUDDDUUDUU"  #são 10 passos no caminho
qtdeVales = ContadorVales(passos, caminho)
qtdeVales.contadorVales()