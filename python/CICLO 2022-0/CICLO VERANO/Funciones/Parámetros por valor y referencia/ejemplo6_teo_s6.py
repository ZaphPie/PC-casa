#input: num(int) -> num>10
#output: sigPrimo,antPrimo (int)
#--------------------------------------------------------
def esPrimo(num):
   if num==1:
       return False
   divisor = 2
   while divisor < num:
       if num % divisor == 0:
           return False
       divisor = divisor + 1
   return True

def siguientePrimo(numero):
   cont = numero + 1
   while not(esPrimo(cont)):
       cont = cont + 1
   return cont


def anteriorPrimo(numero):
   cont = numero -1
   while  not(esPrimo(cont)):
       cont = cont -1
   return cont


#--------------------------------------
num = int(input("Número [ mayor a 10] : "))
while num<=10:
   num = int(input("Número [ mayor a 10] : "))
print("El siguiente número primo es : ", siguientePrimo(num))
print("El anterior número primo es  : ", anteriorPrimo(num))