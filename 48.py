again = 'si'
count = 0
while again == 'si': 
    name= input('ingresa el nombre de alguien que quieras invitar a tu fiesta: ')
    print (name, "ahora esta invitado")
    count = count + 1
    again= input ('quieres invitar a alguien mas? si o no')
print ('invitaste a', count, "personas")