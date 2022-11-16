nombre= input ("Ingrese un nombre")
#print(nombre)
#print(len(nombre))
if len (nombre) >= 12:
    print ("Contra fuerte")
elif len (nombre) <12 and len (nombre)>6:
    print("Contra media")
else:
    print ("Contra débil")
