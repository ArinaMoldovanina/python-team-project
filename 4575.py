# Задание 7

class Streamer:
    def __init__(self, name="", subscribers=0, donats=None):
        self.name = name
        self.subscribers = subscribers
        self.donats = donats if donats is not None else []

    def total_donations(self):
        return sum(self.donats)

    def average_donation(self):
        if not self.donats:
            return 0.0
        return self.total_donations / len(self.donats)

    def print_card(self):
        print(f"Стример: {self.name}")
        print(f"Подписчики: {self.subscribers}")
        print(f"Всего донатов: {self.total_donations}")
        print(f"Средний донат: {self.average_donation}")