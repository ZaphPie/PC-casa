par = 0
impar = 0
total = 0
archivo = open('numeros.txt', 'w+')
valor = int(input('Ingrese: '))
for i in range(1, valor+1):
    archivo.write(str(i)+'\n')
    total += i
    if i % 2 == 0:
        par += 1
    elif i % 2 != 0:
        impar += 1

otro = open('reporte.txt', 'w+')

otro.write(f'Numero de pares: {par}'+'\n')
otro.write(f'Numero de impares: {impar}'+'\n')
otro.write(f'Suma: {total}')


