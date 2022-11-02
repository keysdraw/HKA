#Berechnung Altersunterschied Geschwister

#Hat Nutzer einen Bruder oder Schwester, wenn ja gut-> alter herausfinden und diff berechnen wenn nicht ende
user_input = input("Hast du einen Bruder oder eine Schwester?")

if user_input == 'ja' or user_input == 'Ja':
    alter1 = int(input('Wie alt bist du?')) #altersabfrage 1
    alter2 = int(input('Wie alt ist dein Bruder oder deine Schwester?')) #alterabfrage 2

    alter_diff = alter1 - alter2 #altersunterschied berechnen
    if alter_diff < 0: #Vorzeichen entfernen
        alter_diff = alter_diff * (-1)
    print('Euer Alterunterschied beträgt %s Jahre.' % alter_diff) #ausgabe altersunterschied
else:
    print('Pech gehabt')
