with open("Задание 1/data.txt", "r") as file:
    data = dict(zip(map(float, file.readline().split()), map(float, file.readline().split())))