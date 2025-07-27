from adress import Adress
from mailing import Mailing

to_adress = Adress("236997", "Самара", "Солнечная", "22", "1")
from_adress = Adress("126974", "Сочи", "Ленина", "2", "33")
track = "K2367"
cost = 150

mailing = Mailing(to_adress, from_adress, track, cost)
print(mailing)
