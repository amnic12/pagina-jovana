print ("1) rectangulo")
print ("2) triangulo") 
print ()
n1 = int(input("ingrese un numero: "))
if n1==1: 
    l1 = int(input ('ingrese uno de sus lados: '))
    a= l1 *l1 
    print ("el area es: ", a)
elif n1==2: 
    h= int(input('ingrese la altura: '))
    b= int(input ('ingrese la base: '))
    area= (b*h)/2
    print ("el area es: ", area)
else: 
    print ("error")    
