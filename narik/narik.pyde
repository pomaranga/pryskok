character_x = 256
character_y = 462 
character_width = 50
character_height = 50
speed = 6 
platforms = [] 

def setup():
    global img
    size(512, 512)  
    img = loadImage('narKOT.png')  
    noStroke() 
   
    generate_platforms()

def draw():
    global character_x, character_y

    background(0) 

    character_x = constrain(character_x, 0, width - character_width)

    image(img, character_x, character_y, character_width, character_height)  

    display_platforms()

def generate_platforms():
    global platforms

    for i in range(8):
        x = random(0, width - 50)
        y = i * 60 + 80 
        platform = {
            'x': x,
            'y': y,
            'width': 50,
            'height': 10,
            'color': color(random(50, 255), random(50, 255), random(50, 255))  
        }
        platforms.append(platform)

def display_platforms():
  
    for platform in platforms:
        fill(platform['color'])  
        rect(platform['x'], platform['y'], platform['width'], platform['height'])
