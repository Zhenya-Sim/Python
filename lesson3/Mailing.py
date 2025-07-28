class Mailing:
    def __init__(self, to_adress, from_adress, track, cost):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {str(self.from_adress)}"
                f" в {str(self.to_adress)}. Стоимость {self.cost} рублей.")
