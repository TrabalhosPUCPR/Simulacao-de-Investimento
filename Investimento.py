import matplotlib.pyplot as plt
import numpy as np

investimentoinicial = float(input("quanto ira investir "))
investimentopormes = float(input("quanto ira investir por mes "))
tempo = int(input("Por quantos anos "))
tempom = int(input("Por quantos meses "))
tempod = int(input("Por quantos dias "))
juros = float(input("Taxa de juros em % "))
jurosreal = juros / 100
tempomeses = (tempod/30) + (tempo*12) + tempom
print("Tempo de investimento em meses:",round(tempomeses, 2))
x = investimentopormes / jurosreal 
y = (1+jurosreal)** tempomeses
z = y - 1

valorQuaseTotal = z * x
valorinicialJuros = investimentoinicial * (jurosreal + 1)**tempomeses
valorReal = valorQuaseTotal + valorinicialJuros

print("O investimento final vai ser de: " , round(valorReal, 2), "reais")


def investimentofunc(valorReal, tempomeses):
    x = investimentopormes / jurosreal 
    y = (1+jurosreal)** tempomeses
    z = y - 1

    valorQuaseTotal = z * x
    valorinicialJuros = investimentoinicial * (jurosreal + 1)**tempomeses
    valorReal = valorQuaseTotal + valorinicialJuros
    return valorReal
if tempomeses % 2 != 0: 
    tempomeses = np.arange(1,tempomeses, tempomeses-(int(tempomeses)))
else:
    tempomeses = np.arange(1,tempomeses)

plt.grid(color='gray', linestyle='-.', linewidth=0.5)

plt.xlabel('Tempo (meses)')
plt.ylabel('Investimento')
plt.plot(tempomeses.flatten(), investimentofunc(valorReal, tempomeses).flatten())
plt.show()


