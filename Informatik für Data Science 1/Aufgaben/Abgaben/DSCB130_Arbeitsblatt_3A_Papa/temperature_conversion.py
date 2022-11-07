#getting user input
decision = input('In welches Temperatursystem möchtest du deine Temperatur umwandeln: ')
degrees = input('Gradzahl eingeben: ')

#evaluating input and converting the degrees to degrees_converted
if decision[0] == 'c' or decision[0] == 'C':
    degrees_converted = (float(degrees) - 32) * (5/9)
    print(f'{round(float(degrees),2)}° Fahrenheit sind {round(degrees_converted,2)}° Celsius')

elif decision[0] == 'f' or decision[0] == 'F':
    degrees_converted = float(degrees) * 1.8 + 32
    print(f'{round(float(degrees),2)}° Celsius sind {round(degrees_converted,2)}° Fahrenheit')

else:
    print('Fehler bei eingabe')
    