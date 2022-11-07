#definition of variables via input
category, manufacturer, price = input(
    '''
    Produktkategorie, Hersteller und Preis eingeben.
    In Format: Kategorie, Hersteller, Preis
    '''
).split(',')

#definiton of dict. with variables as values
product_info = {
    'Kategorie': category,
    'Hersteller': manufacturer,
    'Preis': price
}

print(product_info)
