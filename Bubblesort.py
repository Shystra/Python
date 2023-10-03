def trocar (sequencia1, indice):
    temporario = sequencia1[indice]
    sequencia1[indice] = sequencia1[indice + 1]
    sequencia1[indice + 1] = temporario


sequenciaNumeral = [10,50,1,3,2,5,7]
troca = 1

while troca: 
    troca = 0
    indice = 0
    
    for indice in range(0, len(sequenciaNumeral) - 1):
        if sequenciaNumeral[indice]>sequenciaNumeral[indice + 1]:
            trocar (sequenciaNumeral, indice)
            troca = 1

print (sequenciaNumeral)