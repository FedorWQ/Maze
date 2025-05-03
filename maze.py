from pygame import *
mixer.init()
font.init()
font1 = font.SysFont('Arial', 70)
mixer.music.load('jungles.ogg')
money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
mixer.music.play()
window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'), (700,500))
game = True
clock = time.Clock()
FPS = 30
win = font1.render('You Win!', True, (255,215,0))
Lose = font1.render('You Lose!', True, (255,215,0))
class GameSprite(sprite.Sprite):
    def __init__(self, filename, w, h, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w,h)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys_pressed[K_s] and self.rect.y < 440:
            self.rect.y += 10
        if keys_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= 10
        if keys_pressed[K_d] and self.rect.x < 640:
            self.rect.x += 10
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= 700 - 65:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed    
class Wall(sprite.Sprite):
    def __init__(self, w, h, color,x,y):
        super().__init__()
        self.image = Surface((w, h))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def drow_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    
wall1 = Wall(20, 210, (0, 100, 0), 180, 340)
wall2 = Wall(20, 220, (0, 100, 0), 180, 1)
wall3 = Wall(110, 20, (0, 100, 0), 190, 201)
wall4 = Wall(20, 110, (0, 100, 0), 298, 201)
wall5 = Wall(20, 4300, (0, 100, 0), 430, 90)
wall6 = Wall(150, 20, (0, 100, 0), 300, 90)
walls = sprite.Group()
walls.add(wall1, wall2, wall3, wall4, wall5, wall6)
player = Player('hero.png', 65, 65, 50, 400, 1)
cyborg = Enemy('cyborg.png', 65, 65, 600, 280, 3)
treasure = GameSprite('treasure.png', 65, 65, 530, 400, 0)
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    clock.tick(FPS)
    display.update()
    if finish == False:
        window.blit(background, (0,0))
        if len(sprite.spritecollide(player, walls, False)) > 0:
            player.rect.x = 50
            player.rect.y = 450
        wall1.drow_wall()
        wall2.drow_wall()
        wall3.drow_wall()
        wall4.drow_wall()
        wall5.drow_wall()
        wall6.drow_wall()
        if sprite.collide_rect(player, cyborg):
            window.blit(Lose, (200, 200))
            finish = True
            kick.play()
        if sprite.collide_rect(player, treasure):
            window.blit(win, (200, 200))
            finish = True
            money.play()
        player.update()
        cyborg.update()
        player.reset()
        cyborg.reset()
        treasure.reset()
    





    