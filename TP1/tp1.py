import matplotlib.pyplot as plt
import numpy as np
plt.style.use('Solarize_Light2')

# TP 1.1 Simulación de una ruleta
# Datos
def frecuenciaR(nro, valores):
    frecuenciaA = 0
    for n in valores:
        if n == nro:
            frecuenciaA += 1
    freqRel = frecuenciaA / len(valores)
    return freqRel


frecuencia = 1 / 37
esperanza = np.arange(0, 37).mean()  # Media aritmética
desvio = np.arange(0, 37).std()  # Desviación estándar
varianza = np.arange(0, 37).var()  # Varianza

t = int(input("Ingrese el número de tiradas: "))  # Número de tiradas
c = int(input("Ingrese el número de corridas: "))  # Número de corridas
nroEvaluar = -1
while nroEvaluar < 0 or nroEvaluar > 36:
    nroEvaluar = int(input("Ingrese un número entre 0 y 36 para el que desea obtener los resultados: "))
    if nroEvaluar < 0 or nroEvaluar > 36:
        print("El número ingresado está fuera del rango válido.")


frecuencias = [[0 for x in range(t)] for y in range(c)]
medias = [[0 for x in range(t)] for y in range(c)]
desvios = [[0 for x in range(t)] for y in range(c)]
varianzas = [[0 for x in range(t)] for y in range(c)]


for i in range(0, c):
    numeros = np.random.randint(0, 37, t)
    print(numeros)
    for n in range(0, t):
        lista = numeros[:n + 1]
        frecuencias[i][n] = frecuenciaR(nroEvaluar, lista)
        medias[i][n] = lista.mean()
        desvios[i][n] = lista.std()
        varianzas[i][n] = lista.var()


# Gráficos
fig, axs = plt.subplots(
    ncols=2, nrows=2, constrained_layout=True, figsize=[9, 6])


axs[0, 0].set_title('Frecuencia Relativa (fr) del número ' + str(nroEvaluar))
axs[0, 0].set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia) + 0.05)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs[0, 0].plot(range(1, t + 1), frecuencias[i])
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-',
                  label='fre: ' + str(round(frecuencia, 3)))

axs[0, 1].set_title('Valor Promedio (vp)')
axs[0, 1].set(xlabel='Tiradas', ylabel='Valor Promedio (vp)')
axs[0, 1].set_ylim(bottom=0, top=max(np.amax(medias), esperanza) + 1)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs[0, 1].plot(range(1, t + 1), medias[i])
axs[0, 1].axhline(y=esperanza, color='b', linestyle='-',
                  label='vpe: ' + str(round(esperanza, 3)))

axs[1, 0].set_title('Valor del Desvío (vd)')
axs[1, 0].set(xlabel='Tiradas', ylabel='Valor del Desvío (vd)')
axs[1, 0].set_ylim(bottom=0, top=max(np.amax(desvios), desvio) + 1)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs[1, 0].plot(range(1, t + 1), desvios[i])
axs[1, 0].axhline(y=desvio, color='b', linestyle='-',
                  label='vde: ' + str(round(desvio, 3)))

axs[1, 1].set_title('Valor de la Varianza (vve)')
axs[1, 1].set(xlabel='Tiradas', ylabel='Valor de la Varianza (vv)')
axs[1, 1].set_ylim(bottom=0, top=max(np.amax(varianzas), varianza) + 10)
for i in range(0, c):
    # , label='corrida '+str(i+1)+'°')
    axs[1, 1].plot(range(1, t + 1), varianzas[i])
axs[1, 1].axhline(y=varianza, color='b', linestyle='-',
                  label='vve: ' + str(round(varianza, 3)))

for ax in axs.flat:
    ax.legend()
    ax.set_xlim(left=0, right=t)

plt.show()