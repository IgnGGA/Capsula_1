#1. Muestre la distribución de ingresos de los clientes en un gráfico.
#2. Obtenga el Ingreso promedio por sexo, desviación estándar y coeficiente de variabilidad
#3. Obtenga la distribución del ingreso según sexo a través de un gráfico de cajas, histograma y violín.
#
#---------------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd

def importandoDatos():
    archivo=pd.read_excel('Base_taller_semana1.xlsx')
    #print (archivo)
    return archivo

def distribuicionIngresos():#Solucion 1
    
    datos=importandoDatos()
    rangosIngresos=pd.cut(datos['Ingreso_Anual'], bins=6).value_counts(sort=False)#dividiremos los datos en 'n' grupos, y tendremos los valores en rangos
    rangosEdad=pd.cut(datos['Edad'], bins=6).value_counts(sort=False)
    estadisticas= datos.describe()
    print(f'Estadisticos:\n{estadisticas}\n{rangosIngresos}\n{type(rangosIngresos)}')
    rangosIngresos, rangosEdad=rangosIngresos.tolist(), rangosEdad.tolist()#Despues de transformar los datos y visualizar la composicion de los rangos los tranformamos en una lista para poder graficarla
    return (rangosIngresos, rangosEdad, datos)

#--------------------------Grafico de Puntos---------------------------------------------------------
def graficado():
    import matplotlib.pyplot as plt

    x=['G1','G2','G3','G4','G5','G6']
    rangos=distribuicionIngresos()
    rangosIngresos=rangos[0]
    rangosEdad=rangos[1]
    datos=rangos[2]
    
    def graficosDePuntos(ejeX,ejeY,titulo,estilo):
        fig, ax = plt.subplots()
        fig.suptitle(str(titulo))
        ax.scatter(ejeX ,ejeY)
        plt.grid(color='#95a5a6', linestyle=estilo, linewidth=1, axis='x', alpha=1)
        plt.show()
    def graficosDeLineas(ejeX,ejeY,titulo,estilo):
        fig, ax = plt.subplots()
        fig.suptitle(str(titulo))
        ax.plot(ejeX ,ejeY)
        plt.grid(color='#95a5a6', linestyle=estilo, linewidth=1, axis='x', alpha=1)
        plt.show()
    def graficosEnBarra(ejeX,ejey,titulo,tEjeX,tEjeY,artAttack):
        plt.bar(x=ejeX, height=ejey, color=artAttack)
        plt.title(titulo)
        plt.xlabel(tEjeX)
        plt.ylabel(tEjeY)
        plt.show()
    
    graficosDePuntos(x,rangosIngresos,'Rango vs Ingresos Anuales','--')
    graficosDeLineas(x,rangosEdad,'Rango vs Edad','--')
    graficosDePuntos(datos['Edad'],datos['Ingreso_Anual'],'Edad vs Ingresos Anuales','')
    graficosDePuntos(datos['Ingreso_Anual'],datos['Edad'],'Ingresos Anuales vs Edad','')
    graficosEnBarra(datos['Sucursal'],datos['Ingreso_Anual'],'Sucursal vs Ingreso','Sucursal','Ingreso Anual','green')
    graficosEnBarra(datos['Sexo'],datos['Ingreso_Anual'],'Sexo vs Ingreso','Sucursal','Ingreso Anual','orange')

graficado()