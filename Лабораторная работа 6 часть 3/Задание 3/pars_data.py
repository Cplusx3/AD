with open("Задание 3/data.txt", "r") as file:
    data = {}
    text = [tuple(map(float, i.split())) for i in file.readlines()]
    for i in text: 
        data[i[0]] = i[1:]
    
    
    