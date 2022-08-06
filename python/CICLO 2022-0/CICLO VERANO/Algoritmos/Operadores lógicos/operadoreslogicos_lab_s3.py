"""
Los conectores lógicos:
and -> Es True si ambos son True
or -> Es True si al menos uno es True
not -> Convierte el True en False y viceversa


Los operadores de relación:
> Mayor
>= Mayor o igual
< Menor
<= Menor o igual
!= Diferente
== Iguales
not , ! Negación

CARACTERÍSTICAS:
- Conectores lógicos tienen mayor precedencia que operadores de relación
- Operaciones con la misma precedencia se evalúan de izquierda a derecha
- Los paréntesis permiten modificar las precedencias
- Tienen menor precedencia que los operadores matemáticos

TRUE = 1
FALSE = 0




"""

numero = int(input("Número: "))
rpta = numero%2==0
print("El número es" + rpta*" par" + (not(rpta))*" impar")
