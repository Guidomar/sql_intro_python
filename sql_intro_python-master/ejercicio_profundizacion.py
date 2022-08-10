import numpy as np
import matplotlib.pyplot as plt
import sqlite3


def fetch():
    conn = sqlite3.connect('heart.db')
    c=conn.cursor()
    
    c.execute('SELECT pulso FROM sensor')
    data = c.fetchall()
    
    
    return data
    
    conn.close()

def show():
    
    x= fetch()
    fig = plt.figure()
    ax= fig.add_subplot()
    ax.plot(x, color='blue')
    ax.set_facecolor('whitesmoke')
    ax.set_title('Pulsaciones sensadas durante el evento')
    plt.show()

def estadistica():
    d = fetch()
    valor_medio =round(np.mean(d),2)
    print("El valor medio es :", valor_medio)

    minimo = np.min(d)
    print ("El valor mínimo es : ", minimo)

    maximo = np.max(d)
    print ("El valor máximo es : ", maximo)

    desvio_std = round(np.std(d),2)
    print ("El desvío estandar es :", desvio_std)

def regiones():
    
    valores = fetch()
    mean = round(np.mean(valores), 2)
    std = round(np.std(valores),2)
    
    # Lista 1
    x_1 = []
    y_1 = []

    for i in range(len(valores)):
        if valores [i][0]<= (mean-std):
            x_1.append(valores[i][0])
            y_1.append(i)
        
    '''
    print("x_1 :", x_1)
    print("len x :",len(x_1))
    print("y_1", y_1)
    print("len y :",len(y_1))'''
            
    
   # Lista 2
    x_2 = []
    y_2 = []

    for i in range(len(valores)):
        if valores[i][0] >= (mean+std):
            x_2.append(valores[i][0])
            y_2.append(i)

    # Linea 3
    x_3 = []
    y_3 = []

    for i in range(len(valores)):
        if valores[i][0] >(mean-std) or valores [i][0]<(mean+std):
            x_3.append(valores[i][0])
            y_3.append(i)

    # Grafica de scatter Plot l1,l2 y l3:
    fig = plt.figure()
    
    fig.suptitle('Líneas l1, l2 y l3', fontsize=16)
    
    ax1=fig.add_subplot(1,3,1)
    ax1.scatter(x_1,y_1, c='blue')
    ax1.set_title("Scatter_1") 
    ax1.set_ylabel("Y[indice]")
    ax1.set_xlabel("X[pulso]")
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
   
    ax2=fig.add_subplot(1,3,2)
    ax2.scatter(x_2,y_2, c='green')
    ax2.set_title("Scatter_2") 
    ax2.set_ylabel("Y[indice]")
    ax2.set_xlabel("X[pulso]")
    ax2.set_facecolor('whitesmoke')
    ax2.grid('solid')

    ax3=fig.add_subplot(1,3,3)
    ax3.scatter(x_3,y_3, c='red')
    ax3.set_title("Scatter_3") 
    ax3.set_ylabel("Y[indice]")
    ax3.set_xlabel("X[pulso]")
    ax3.set_facecolor('whitesmoke')
    ax3.grid('solid')
   
    plt.show()

if __name__== '__main__':
    fetch() 
    show()
    estadistica()
    regiones()

