from smartphone import Smartphone

catalog = [
    Smartphone("Iphone", "15", "+79260195531"),
    Smartphone("Iphone", "16", "+79001694430"),
    Smartphone("Iphone", "16e", "+79201657900"),
    Smartphone("Samsung", "Galaxy S25", "+79361593317"),
    Smartphone("Samsung", "Galaxy S25 Ultra", "+79136175502"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
