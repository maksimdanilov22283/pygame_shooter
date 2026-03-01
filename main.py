from pygame import *
from random import randint

init()
screen_w = 1080
screen_h = 720
screen = display.set_mode((screen_w,screen_h)) 
screen.fill((255,255,255))
clock = time.Clock()

class Sprite (sprite.Sprite):
    def __init__(self, x, y, w, h, img):
        super().__init__()
        self.image = image.load(img)
        self.image = transform.scale(self.image, (w,h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class Enemy (Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class Player (Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.speed = speed
        self.rect.h = h

    def update(self):
        pressed_keys = key.get_pressed()
        if pressed_keys[K_a] and self.rect.x >= 0:
            self.rect.x -= self.speed
        if pressed_keys[K_d] and self.rect.x <= screen_w - self.rect.width:
            self.rect.x += self.speed
    
    def shoot(self):
        bullet = Bullet(1, self.rect.x, self.rect.y, 10, 15, 'bullet.png')
        bullets.add(bullet)
     
class Bullet (Sprite):
    def __init__(self, speed, x, y, w, h, img):
        super().__init__(x, y, w, h, img)
        self.speed = speed
    
    def update(self):
        self.rect.y += self.speed

class TextArea (sprite.Sprite):
    def __init__(self, x, y, w, h, color):
        super().__init__()
        self.rect = Rect(x, y, w, h)
        self.color = color
        
    def set_text(self, text, color, size_text):
        self.text = text
        self.image = font.Font(None, size_text).render(text, True, color)

    def draw_text(self, x, y):
        draw.rect(screen, self.color, self.rect)
        screen.blit(self.image, (self.rect.x + x, self.rect.y + y))

player = Player(8, 0, 660 , 60, 60, 'player.png') 
group = sprite.Group()
bullets = sprite.Group()

counter = 0
while True:
    for bullet in range(100):
        pass
    player.update()
    if counter > 60:
        enemy_w = 40
        x = randint(0, screen_w - enemy_w)
        enemy = Enemy(1, x, 0, enemy_w, 40, 'enemy.png')
        group.add(enemy)
        counter = 0
    else:
        counter += 1
    screen.fill((255,255,255)) 
    group.update()
    group.draw(screen)
    player.draw()
    bullets.draw(screen)
    pressed_keys = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            exit()
    clock.tick(60)
    display.update()