import random

SAVE_FILE = "player.txt"


class Player:
    def __init__(self, name, points=0, level=1):
        self.name = name
        self.points = points
        self.level = level

    def add_points(self, n):
        self.points += n
        self.level = self.points // 100 + 1


def save_player(player, filename=SAVE_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"{player.name};{player.points};{player.level}\n")


def load_player(filename=SAVE_FILE):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            name, points, level = f.readline().strip().split(";")
            return Player(name, int(points), int(level))
    except FileNotFoundError:
        name = input("Новый игрок! Как вас зовут: ").strip()
        return Player(name)


def play_round(player):
    dice = random.randint(1, 6)
    print(f"\nПеред кошкой кубик высотой {dice}!")
    choice = input("Прыгать? (да/нет): ").strip().lower()

    if choice == "да":
        if dice <= 2:
            success = True
        elif dice <= 4:
            success = random.random() < 0.7
        else:
            success = random.random() < 0.2
        if success:
            reward = dice * 2
            player.add_points(reward)
            print(f"Кошка перепрыгнула кубик! +{reward} очков")
        else:
            print("Кошка споткнулась! Очков нет.")
    elif choice == "нет":
        player.add_points(1)
        print("Кошка осторожно обходит кубик. +1 очко за осторожность.")
    else:
        print("Не понял команду. Раунд пропущен.")
        return

    save_player(player)
    print(f"Очки сохранены: {player.points} (уровень {player.level})")


def main():
    player = load_player()
    print(f"С возвращением, {player.name}! Очки: {player.points}")
    while True:
        answer = input("\nИграем ещё раунд? (да/нет): ").strip().lower()
        if answer == "нет":
            print("Пока!")
            break
        play_round(player)


if __name__ == "__main__":
    main()
