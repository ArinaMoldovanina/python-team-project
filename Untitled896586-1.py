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