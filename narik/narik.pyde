character_x = 256
character_y = 462 
character_width = 50
character_height = 50
speed = 5 
gravity = 0.5
jump_strength = -15  
velocity_y = jump_strength
platforms = [] 
bullets = []

left_pressed = False
right_pressed = False
class Bullet:
    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction  # 'up', 'left', 'right'
        self.width = 5
        self.height = 10

    def update(self):
        if self.direction == 'up':
            self.y += self.speed
        elif self.direction == 'left':
            self.x += self.speed
        elif self.direction == 'right':
            self.x += self.speed

    def display(self):
        fill(0)
        rect(self.x, self.y, self.width, self.height)

def setup():
    global img
    size(512, 512)  
    img = loadImage('narKOT.png')  
    noStroke() 
    generate_platforms()
    print("Setup complete") 
def draw():
    global character_x, character_y, velocity_y, left_pressed, right_pressed

    background(200) 

    velocity_y += gravity
    character_y += velocity_y

    if left_pressed:
        character_x -= speed
    if right_pressed:
        character_x += speed

    on_platform = False
    for platform in platforms:
        if platform['is_moving']:
            platform['x'] += platform['velocity_x']
            if platform['x'] <= 0 or platform['x'] + platform['width'] >= width:
                platform['velocity_x'] *= -1
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
    if character_y < height / 2:
        scroll_y = height / 2 - character_y
        character_y = height / 2
        for platform in platforms:
            platform['y'] += scroll_y
    generate_new_platforms()
    if character_y > height:
        noLoop() 
        print("Game Over")

    image(img, character_x, character_y, character_width, character_height)  

    display_platforms() 

    update_and_display_bullets()


def keyPressed():
    global left_pressed, right_pressed
    if key == CODED:
        if keyCode == LEFT:
            left_pressed = True
        elif keyCode == RIGHT:
            right_pressed = True
    if key == ' ':
        bullets.append(Bullet(character_x + character_width / 2, character_y, -10, 'up'))
    elif key == 'a':
        bullets.append(Bullet(character_x, character_y + character_height / 2, -10, 'left'))
    elif key == 'd':
        bullets.append(Bullet(character_x + character_width, character_y + character_height / 2, 10, 'right'))

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
        velocity_x = 2  
        if random(1) < 0.5:  
            velocity_x *= -1 
        is_moving = random(1) < 0.5 
        platform = {
            'x': x,
            'y': y,
            'width': 50,
            'height': 10,
            'velocity_x': velocity_x,
            'is_moving': is_moving,
            'color': color(random(50, 255), random(50, 255), random(50, 255))  
        }
        platforms.append(platform)
    print("Platforms generated:", platforms)
def generate_new_platforms():
    global platforms
    while len(platforms) < 8:
        x = random(0, width - 50)
        y = -10 
        velocity_x = 2
        if random(1) < 0.5:
            velocity_x *= -1 
        is_moving = random(1) < 0.5
        platform = {
            'x': x,
            'y': y,
            'width': 50,
            'height': 10,
            'velocity_x': velocity_x,
            'is_moving': is_moving,
            'color': color(random(50, 255), random(50, 255), random(50, 255))  
        }
        platforms.append(platform)
   
    platforms[:] = [platform for platform in platforms if platform['y'] < height]
    print("New platforms generated:", platforms)
def display_platforms():
    for platform in platforms:
        fill(platform['color'])  
        rect(platform['x'], platform['y'], platform['width'], platform['height'])
    print("Platforms displayed")

def update_and_display_bullets():
    for bullet in bullets[:]:
        bullet.update()
        bullet.display()
        if bullet.y < 0 or bullet.x < 0 or bullet.x > width:
            bullets.remove(bullet)
