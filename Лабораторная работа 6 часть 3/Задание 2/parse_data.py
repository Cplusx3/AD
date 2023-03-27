with open("Задание 2/data.txt", "r") as file:
    data = dict(zip(map(float, file.readline().split()), map(float, file.readline().split())))