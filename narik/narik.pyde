character_x = 256
character_y = 462 
character_width = 50
character_height = 50
speed = 5 
gravity = 0.5
jump_strength = -15  
velocity_y = jump_strength
platforms = [] 

left_pressed = False
right_pressed = False

def setup():
    global img
    size(512, 512)  
    img = loadImage('narKOT.png')  
    noStroke() 
    generate_platforms()

def draw():
    global character_x, character_y, velocity_y, left_pressed, right_pressed

    background(0) 

    velocity_y += gravity
    character_y += velocity_y

    if left_pressed:
        character_x -= speed
    if right_pressed:
        character_x += speed

    on_platform = False
    for platform in platforms:
        if (character_x + character_width > platform['x'] and
            character_x < platform['x'] + platform['width'] and
            character_y + character_height >= platform['y'] and
            character_y + character_height - velocity_y <= platform['y']):
            character_y = platform['y'] - character_height
            velocity_y = jump_strength
            on_platform = True
            break

    if character_y + character_height >= height and velocity_y > 0:
        character_y = height - character_height
        velocity_y = jump_strength
        on_platform = True

    if not on_platform and character_y + character_height < height:
        velocity_y += gravity

    character_x = constrain(character_x, 0, width - character_width)

    image(img, character_x, character_y, character_width, character_height)  

    display_platforms() 

def keyPressed():
    global left_pressed, right_pressed
    if key == CODED:
        if keyCode == LEFT:
            left_pressed = True
        elif keyCode == RIGHT:
            right_pressed = True

def keyReleased():
    global left_pressed, right_pressed
    if key == CODED:
        if keyCode == LEFT:
            left_pressed = False
        elif keyCode == RIGHT:
            right_pressed = False


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
