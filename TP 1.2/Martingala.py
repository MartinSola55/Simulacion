import matplotlib.pyplot as plt
import random
import numpy as np
plt.style.use('Solarize_Light2')


def graficar(valoresCapital,frecRel,capital,t):
    plt.plot(valoresCapital,label='Valores Capital')
    plt.plot(capital)
    plt.xlabel('Tiradas')
    plt.ylabel('Capital')
    plt.axhline(y=capital, color='blue')
    plt.axhline(y=0, color='red')
    plt.show()

    etiquetas=[]
    for x in range(1 , t+1):
        etiquetas.append(x)
    indices = np.arange(len(etiquetas))
    plt.bar(indices, frecRel, width=0.5)
    plt.xlabel('Tiradas')
    plt.ylabel('Frecuencias Relativas')
    plt.title('Frecuencias Relativas')
    plt.show()


def martinGala(tiradas,capital,apuesta, tipoJuego):
    apuestaParImpar=apuesta
    apuestaRojoNegro=apuesta
    apuestaMenorMayor=apuesta
    capitalOriginal=capital
    tiradaGanadora=0
    frecuenciaRelativa=[]
    valoresCapital=[]
    for x in range(1,tiradas+1):
        print("Tirada N˚: "+str(x))
        nroParImpar=np.random.randint(0, 36)
        if(nroParImpar%2==0):
            parImpar="par"
        else:
            parImpar="impar"
        rojoNegro=random.choice(["rojo","negro"])
        menorMayor=random.choice(["menor","mayor"])
        numeroRuleta=np.random.randint(0, 36)
        if(numeroRuleta!=0):
            if(numeroRuleta in negros):
                colorNro="Negro"
            else:
                colorNro="Rojo"
            if(numeroRuleta%2==0):
                moduloNro="Par"
            else:
                moduloNro="Impar"
            if(numeroRuleta<19):
                maymenNro="Menor"
            else:
                maymenNro="Mayor"
        else:
                colorNro="Verde"
                moduloNro="-"
                maymenNro="-"


        if(((tipoJuego == "finito") & (capital > 0) & (capital - apuestaParImpar - apuestaMenorMayor - apuestaRojoNegro >= 0)) | (tipoJuego == "infinito")):
            print("Nro de la ruleta: "+str(numeroRuleta)+" ("+ moduloNro + ", " + maymenNro + ", " + colorNro + ")")
            print("Capital: $"+ str(capital)+ "\nApuesta: $"+str(apuestaParImpar)+" al "+parImpar+
                    "\nApuesta: $" +str(apuestaMenorMayor)+" al "+menorMayor+"\nApuesta: $"+str(apuestaRojoNegro)
                    +" al "+ rojoNegro+"\n\n")
            capitalAnterior=capital
            if(numeroRuleta!=0):
                if(((numeroRuleta%2==0) & (parImpar=="impar")) or ((numeroRuleta%2!=0) & (parImpar=="par"))):
                    capital=capital-apuestaParImpar
                    apuestaParImpar=apuestaParImpar*2
                else:
                    capital=capital+apuestaParImpar
                    apuestaParImpar=apuesta
                if(((numeroRuleta<19) & (menorMayor=="mayor")) or ((numeroRuleta>19) & (menorMayor=="menor" ))):
                    capital=capital-apuestaMenorMayor
                    apuestaMenorMayor=apuestaMenorMayor*2
                else:
                    capital=capital+apuestaMenorMayor
                    apuestaMenorMayor=apuesta
                if(((numeroRuleta in negros) & (rojoNegro=="rojo")) or ((numeroRuleta in rojos) & (rojoNegro=="negro"))):
                    capital=capital-apuestaRojoNegro
                    apuestaRojoNegro=apuestaRojoNegro*2
                else:
                    capital=capital+apuestaRojoNegro
                    apuestaRojoNegro=apuesta
            else:
                capital=capital-(apuestaParImpar+apuestaRojoNegro+apuestaMenorMayor)
                apuestaRojoNegro=apuestaRojoNegro*2
                apuestaMenorMayor=apuestaMenorMayor*2
                apuestaParImpar=apuestaParImpar*2
    
            if(capital>capitalAnterior):
                tiradaGanadora=tiradaGanadora+1
            frecuenciaRelativa.append(tiradaGanadora/x)
        else:
            print("Se quedo sin dinero")
            for i in range(x,tiradas+1):
                frecuenciaRelativa.append(tiradaGanadora/i)
            break;
        valoresCapital.append(capital)
        
    graficar(valoresCapital,frecuenciaRelativa,capitalOriginal,tiradas)


t = 150 #Número de tiradas
capital = 10000
apuesta = 100 #Apuesta Mínima
tipoJuego = "finito" #finito | infinito
global negros
global rojos
negros = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

print("\nMartin Gala")
print("--------------------------------------------------------------\n")
martinGala(t,capital,apuesta,tipoJuego)