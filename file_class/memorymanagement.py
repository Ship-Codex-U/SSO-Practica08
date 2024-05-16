from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from copy import deepcopy

class MemoryManagement:
    def __init__(self, size, values, textLabel) -> None:
        self.__size = size
        self.__values = deepcopy(values)
        self.__textLabel = textLabel
        self.__newDataModification = False
        self.__sizeNewData = []
        self.__pointStart = []
        
        self.__available = []
        for i in range(len(self.__values)):
            self.__available.append(True)
        
        self.__size_o = size
        self.__values_o = deepcopy(values)
        self.__textLabel_o = deepcopy(textLabel)
        self.__available_o = deepcopy(self.__available)
            
        self.__nextPos = 0
        
    def createNewPartition(self, size, status, position):
        self.__sizeNewData = deepcopy([])
        self.__pointStart = deepcopy([])
        self.__newDataModification = True        
        self.__size += size
        
        if (position == 'Al inicio'):
            for pos, value in enumerate(self.__values):
                self.__values[pos] += size
            
            self.__values.insert(0, size)
            
            self.__textLabel.insert(0, str(size) + 'kb')
            
            if (status == 'Disponible'):
                self.__available.insert(0, True)
            elif (status == 'Ocupado'):
                self.__available.insert(0, False)
                

            for pos, value in enumerate(self.__available):
                if (value == False):
                    if (pos == 0):
                        self.__pointStart.append(0)
                        self.__sizeNewData.append(size)
                    elif (pos > 0):
                        self.__pointStart.append(self.__values[pos - 1])
                        self.__sizeNewData.append(self.__values[pos] - self.__values[pos - 1])

        elif (position == 'Al final'):
            self.__values.append(self.__size)
            self.__textLabel.append(str(size) + 'kb')
            
            if (status == 'Disponible'):
                self.__available.append(True)
            elif (status == 'Ocupado'):
                self.__available.append(False)
                
                self.__pointStart.append(self.__size - size)
                self.__sizeNewData.append(size)       
    
    def memoryReset(self):
        self.__size = self.__size_o
        self.__values = deepcopy(self.__values_o)
        self.__textLabel = deepcopy(self.__textLabel_o)
        self.__newDataModification = False
        self.__sizeNewData = deepcopy([])
        self.__pointStart = deepcopy([])
        
        self.__available = deepcopy(self.__available_o)
        
        self.__nextPos = 0
        
    
    def getMemoryStructure(self):
        # Limpia la figura actual antes de crear una nueva gráfica
        plt.clf()   
        # Crear una gráfica de barras con un solo valor
        data = [self.__size]  # Valor único para la barra
        labels = ['Memoria']  # Etiqueta para la barra
        
        # Crear un gráfico de barras horizontal con color verde
        plt.barh(labels, data, color='forestgreen')

        # Agregar líneas verticales en los puntos de corte especificados
        cortes = self.__values
        
        for corte in cortes:
            plt.axvline(x=corte, color='black', linestyle='--', linewidth=2)
        
        if self.__newDataModification:
            for value, start in zip(self.__sizeNewData, self.__pointStart):
                plt.barh(labels, value, left=start, color='red')

        # Agregar etiquetas a los cortes
        # Inicializa el bucle desde el primer corte (índice 0)
        for i in range(len(cortes)):
            if i == 0:
                # La primera iteración se maneja para agregar la etiqueta con el valor de 1000
                centro = cortes[i] / 2  # Centro desde el inicio hasta el primer corte
                plt.text(centro, 0, str(self.__textLabel[0]), rotation=90, ha='center', va='center', fontsize=10, color='white', bbox=dict(facecolor='none', alpha=0, edgecolor='none'))
            else:
                # Las iteraciones subsiguientes calculan el centro y la diferencia de cada sección
                centro = (cortes[i - 1] + cortes[i]) / 2
                plt.text(centro, 0, str(self.__textLabel[i]), rotation=90, ha='center', va='center', fontsize=10, color='white', bbox=dict(facecolor='none', alpha=0, edgecolor='none'))

        self.__newDataModification = False
        
        # Mostrar la gráfica en el widget QGraphicsView
        return FigureCanvas(plt.gcf())
    
    def firstFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            pos = 0
            flag = True
            while flag:
                if(pos < len(self.__values)):
                    if pos == 0:
                        if(self.__available[0] == True and value <= self.__values[pos]):
                            self.__values.insert(0, value)
                            self.__textLabel.insert(0, label)
                            
                            newValor = self.__values[pos + 1] - value
                            newLabel = str(newValor) + 'kb'                        
                            self.__textLabel[pos + 1] = newLabel
                            
                            self.__pointStart.append(0)
                            self.__sizeNewData.append(value)
                            
                            self.__available.insert(0, False)
                            
                            flag = False
                    else:
                        sizeAvailable = self.__values[pos] - self.__values[pos - 1]
                        
                        if(self.__available[pos] == True and value <= sizeAvailable):
                            self.__values.insert(pos, self.__values[pos - 1] + value)
                            self.__textLabel.insert(pos, label)
                            
                            newValor = self.__values[pos + 1] - self.__values[pos] 
                            newLabel = str(newValor) + 'kb'                        
                            self.__textLabel[pos + 1] = newLabel
                            
                            self.__pointStart.append(self.__values[pos - 1])
                            self.__sizeNewData.append(value)
                            
                            self.__available.insert(pos, False)
                            
                            flag = False
                else:
                    flag = False  
                    
                pos += 1


    def bestFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            pos = 0
            bestFit = 9999999
            bestFitPos = -1
            
            
            for value_d in self.__values:
                if(pos < len(self.__values) and self.__available[pos]):
                    if pos == 0:
                        sizeAvailable = self.__values[0]
                    else:
                        sizeAvailable = self.__values[pos] - self.__values[pos - 1]
                    
                    if(sizeAvailable - value < bestFit and sizeAvailable - value >= 0):
                        bestFit = sizeAvailable - value
                        bestFitPos = pos
                
                pos += 1
                    
            if bestFitPos == 0:
                self.__values.insert(0, value)
                self.__textLabel.insert(0, label)
                
                newValor = self.__values[bestFitPos + 1] - value
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[bestFitPos + 1] = newLabel
                
                self.__pointStart.append(0)
                self.__sizeNewData.append(value)
                
                self.__available.insert(0, False)

            elif bestFitPos != -1:
                self.__values.insert(bestFitPos, self.__values[bestFitPos - 1] + value)
                self.__textLabel.insert(bestFitPos, label)
                
                newValor = self.__values[bestFitPos + 1] - self.__values[bestFitPos] 
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[bestFitPos + 1] = newLabel
                
                self.__pointStart.append(self.__values[bestFitPos - 1])
                self.__sizeNewData.append(value)
                
                self.__available.insert(bestFitPos, False)     
                 
    
    def worstFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            pos = 0
            worstFit = 0
            worstFitPos = -1
            
            
            for value_d in self.__values:
                if(pos < len(self.__values) and self.__available[pos]):
                    if pos == 0:
                        sizeAvailable = self.__values[0]
                    else:
                        sizeAvailable = self.__values[pos] - self.__values[pos - 1]
                    
                    if(sizeAvailable - value > worstFit):
                        worstFit = sizeAvailable - value
                        worstFitPos = pos
                
                pos += 1
                    
            if worstFitPos == 0:
                self.__values.insert(0, value)
                self.__textLabel.insert(0, label)
                
                newValor = self.__values[worstFitPos + 1] - value
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[worstFitPos + 1] = newLabel
                
                self.__pointStart.append(0)
                self.__sizeNewData.append(value)
                
                self.__available.insert(0, False)

            elif worstFitPos != -1:
                self.__values.insert(worstFitPos, self.__values[worstFitPos - 1] + value)
                self.__textLabel.insert(worstFitPos, label)
                
                newValor = self.__values[worstFitPos + 1] - self.__values[worstFitPos] 
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[worstFitPos + 1] = newLabel
                
                self.__pointStart.append(self.__values[worstFitPos - 1])
                self.__sizeNewData.append(value)
                
                self.__available.insert(worstFitPos, False)  
        
    
    def nextFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            flag = True
            validatePos = self.__nextPos
            
            while flag:
                    
                if self.__nextPos == 0:
                    if(self.__available[0] == True and value <= self.__values[self.__nextPos]):
                        self.__values.insert(0, value)
                        self.__textLabel.insert(0, label)
                        
                        newValor = self.__values[self.__nextPos + 1] - value
                        newLabel = str(newValor) + 'kb'                        
                        self.__textLabel[self.__nextPos + 1] = newLabel
                        
                        self.__pointStart.append(0)
                        self.__sizeNewData.append(value)
                        
                        self.__available.insert(0, False)
                        
                        flag = False
                else:
                    sizeAvailable = self.__values[self.__nextPos] - self.__values[self.__nextPos - 1]
                    
                    if(self.__available[self.__nextPos] == True and value <= sizeAvailable):
                        self.__values.insert(self.__nextPos, self.__values[self.__nextPos - 1] + value)
                        self.__textLabel.insert(self.__nextPos, label)
                        
                        newValor = self.__values[self.__nextPos + 1] - self.__values[self.__nextPos] 
                        newLabel = str(newValor) + 'kb'                        
                        self.__textLabel[self.__nextPos + 1] = newLabel
                        
                        self.__pointStart.append(self.__values[self.__nextPos - 1])
                        self.__sizeNewData.append(value)
                        
                        self.__available.insert(self.__nextPos, False)
                        
                        flag = False
                        
                self.__nextPos += 1
                
                if(self.__nextPos == validatePos):
                    flag = False 
                
                if(self.__nextPos == len(self.__values)):
                    self.__nextPos = 0
                     
                    
        
        