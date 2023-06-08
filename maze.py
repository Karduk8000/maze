#создай игру "Лабиринт"!
from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, image_file, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image_file), (65, 65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if (keys[K_w] or keys[K_UP]) and self.rect.y > 5:
            self.rect.y -= self.speed
        if (keys[K_s]or keys[K_DOWN]) and self.rect.y < height - 70:
            self.rect.y += self.speed
        
        if (keys[K_a]or keys[K_LEFT]) and self.rect.x > 5:
            self.rect.x -= self.speed
        if (keys[K_d]or keys[K_RIGHT]) and self.rect.x < width - 70:
            self.rect.x += self.speed
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= width - 70:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

#класс для стен
class Wall(sprite.Sprite):
    def __init__(self, r, g, b, x, y, width, height):
        super().__init__()
        self.r = r
        self.g = g
        self.b = b
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((r, g, b))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

#размеры окна игры
width = 700
height = 500

#создание окна с названием
window = display.set_mode((width, height))
display.set_caption('Лабиринт')

# создание фона сцены
background = transform.scale(image.load("background.jpg"), (width, height))

game = True
finish = False

clock = time.Clock()
FPS = 60

#музыка
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

#надписи
font.init()
my_font = font.SysFont("Arial", 70)
win = my_font. render('ПОБЕЖДА!', True, (255, 215, 0))
lose = my_font. render('ПОТРАЧЕНО...', True, (180, 0, 0))

#создвние обьектов
player = Player('hero.png', 5, height - 80, 4)
monster = Enemy('cyborg.png', width - 80, 280, 2)
final = GameSprite('treasure.png ', width - 120, height - 80, 0)

# создание стен
w1 = Wall(114, 0, 255, 100, 20 , 450, 10)
w2 = Wall(114, 0, 255, 100, 480, 350, 10)
w3 = Wall(114, 0, 255, 100, 20 , 10, 380)
w4 = Wall(114, 0, 255, 200, 130, 10, 350)
w5 = Wall(114, 0, 255, 450, 130, 10, 360)
w6 = Wall(114, 0, 255, 300, 20, 10, 350)
w7 = Wall(114, 0, 255, 390, 120, 130, 10)
# ctrl + f2 выделить одинаковые обьекты

while game:
    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish != True:
        player.update()
        monster.update()

        window.blit(background, (0, 0))# создание фона
        player.reset()#добавление на кадр игрока
        monster.reset()##добавление на кадр врага
        final.reset()##добавление на кадр золото

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()
        w7.draw_wall()

        if sprite.collide_rect(player, w1) or sprite.collide_rect(player, w2) or sprite.collide_rect(player, w3) or sprite.collide_rect(player, w4) or sprite.collide_rect(player, w5) or sprite.collide_rect(player, w6) or sprite.collide_rect(player, w7) or sprite.collide_rect(player, monster):
            finish = True
            window.blit(lose, (160,200))
            kick.play()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit(win, (160,200))
            money.play()
            
    
    display.update()#отрисовка всего кадров
    clock.tick(FPS)


