# Задание 1
try:
    a = int(input("Введи первое число: "))
    b = int(input("Введи второе число: "))
    result = a / b
    print("Результат:", result)
except ValueError:
    print("Введено не число!")
except ZeroDivisionError:
    print("На ноль делить нельзя!")

# Задание 2
try:
    a = float(input("Введите число: "))
    result = 10 / a
    print(f"Результат: 10 / {a} = {result}")
except ValueError:
    print("Ошибка: вы ввели не число!")
except ZeroDivisionError:
    print("Ошибка: делить на ноль нельзя!")
else:
    print("Вычисление прошло успешно.")
finally:
    print("Программа завершена")
    
 # Задание 3
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("Привет\n")
    f.write("Как дела?\n")
    f.write("Пока\n")
 
with open("hello.txt", "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
 
print(lines)             
real_lines = [x for x in lines if x != ""]
print("Строк в файле:", len(real_lines))

# Задание 4

name = "hello.txt"
secondline = "Ещё одна строка"
with open(name, "a", encoding="utf-8") as f:
    f.write(secondline + "\n")
with open(name, "r", encoding="utf-8") as f:
    b = f.read()
    print(b)

# Задание 5

class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades   

    def to_line(self):
        grades_str = ",".join(str(g) for g in self.grades)
        return f"{self.name};{self.group};{grades_str}"

def student_from_line(line):
    name, group, grades_str = line.strip().split(";")
    if grades_str == "":
        grades = []
    else:
        grades = [int(g) for g in grades_str.split(",")]
    return Student(name, group, grades)

def save_students(students, filename="students.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for s in students:
            f.write(s.to_line() + "\n")


def load_students(filename="students.txt"):
    students = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():     
                students.append(student_from_line(line))
    return students

if __name__ == "__main__":
    students = [Student("Анна Петрова", "ИТ-21", [5, 4, 5, 3]), Student("Игорь Смирнов", "ИТ-22", []), Student("Мария Козлова", "ИТ-21", [4, 4, 4])]
    save_students(students)
    loaded = load_students()
    for s in loaded:
        print(s.name, s.group, s.grades)
        
# Задание 6

class Student:
    def __init__(self, name, group, grades):
        self.name = name
        self.group = group
        self.grades = grades

    def to_line(self):
        grades_str = ",".join(str(g) for g in self.grades)
        return f"{self.name};{self.group};{grades_str}"

def student_from_line(line):
    name, group, grades_str = line.strip().split(";")
    if grades_str == "":
        grades = []
    else:
        grades = [int(g) for g in grades_str.split(",")]
    return Student(name, group, grades)
object_from_line = student_from_line

def save_to_file(objects, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for obj in objects:
            f.write(obj.to_line() + "\n")
            
def load_from_file(filename):
    objects = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    objects.append(object_from_line(line))
    except FileNotFoundError:
        print("Файл не найден, начинаем с пустого списка.")
    except ValueError:
        print("Ошибка в формате данных.")
    return objects
        
        
# Задание 7

class Streamer:
    def __init__(self, name="", subscribers=0, donats=None):
        self.name = name
        self.subscribers = subscribers
        self.donats = donats if donats is not None else []

    def total_donations(self):
        return sum(self.donats)

    def average_donation(self):
        return self.total_donations / len(self.donats) if self.donats else 0.0

    def print_card(self):
        print(f"Стример: {self.name}")
        print(f"Подписчики: {self.subscribers}")
        print(f"Всего донатов: {self.total_donations}")
        print(f"Средний донат: {self.average_donation}")

    def save_to_file(self, filename="data.txt"):
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{self.name};{self.subscribers};{';'.join(map(str, self.donats))}\n")

    def load_from_file(cls, filename="data.txt"):
        heroes = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split(";")
                    heroes.append(cls(parts[0], int(parts[1]), list(map(int, parts[2:]))))
        except FileNotFoundError:
            print("Файл не найден, начинаем с пустого списка")
        return heroes
    
def main():
    heroes = [Streamer("GolubKin", 1200, [350, 300]), Streamer("FrostMiron", 8500, [1000, 500, 200]), Streamer("NeonTaxi", 430, [77, 13]),]
    for s in heroes:
        s.save_to_file()
    heroes = []
    heroes = Streamer.load_from_file()
    for s in heroes:
        s.print_card()
        print()
        
# Задание 8
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
    
# Задание 9

    a = input("Имя файла?")
    try:
        with open(a, 'r', encoding='utf-8') as file:
            n = file.read()
            print("Файл успешно прочитан. Содержимое:")
            print(n)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{a}' не найден.")
    except PermissionError:
        print(f"Файл '{a}' найден, но у программы нет прав на его чтение.")
    except UnicodeDecodeError:
        print(f"Ошибка: Не удалось прочитать файл '{a}'.")
        
# Задание 10

def save(filename, name, hp, level):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"{name}|{hp}|{level}")

def load(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read().split("|")
        
    name = data[0]
    hp = int(data[1])
    level = int(data[2])
    
    return name, hp, level

save("data.txt", "Arina", 100, 5)
print(load("data.txt"))

