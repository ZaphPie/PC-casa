import numpy
notas = [ [18,17,20,16] , 
         [5,10, 20,19] ]
notas_np = numpy.array(notas)
filas, columnas = notas_np.shape
print(notas_np[ : , columnas-1: ] )