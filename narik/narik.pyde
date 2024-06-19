character_x = 256
character_y = 462  # Положение персонажа на нижней границе экрана
character_width = 50
character_height = 50
speed = 6  # Скорость перемещения по горизонтали
platforms = []  # Массив для хранения досок

def setup():
    global img
    size(512, 512)  # Размер окна
    img = loadImage('narKOT.png')  # Изображение персонажа
    noStroke()  # Отключение обводки

    # Создание досок
    generate_platforms()

def draw():
    global character_x, character_y

    background(0)  # Чёрный фон

    # Ограничение горизонтального положения персонажа
    character_x = constrain(character_x, 0, width - character_width)

    # Отображение изображения персонажа
    image(img, character_x, character_y, character_width, character_height)  

    # Отображение досок
    display_platforms()

def generate_platforms():
    global platforms

    # Создание досок с интервалом по вертикали
    for i in range(8):
        x = random(0, width - 50)
        y = i * 60 + 80  # Интервалы по вертикали
        platform = {
            'x': x,
            'y': y,
            'width': 50,
            'height': 10,
            'color': color(random(50, 255), random(50, 255), random(50, 255))  
        }
        platforms.append(platform)

def display_platforms():
    # Отображение каждой доски
    for platform in platforms:
        fill(platform['color'])  
        rect(platform['x'], platform['y'], platform['width'], platform['height'])
