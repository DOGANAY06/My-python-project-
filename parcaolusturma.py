
import pygame, sys

pygame.init()
width=1000
height=800
boyut = (1000, 800)
car = pygame.image.load("10126765883442.jpg")
x = 0
y = 0
pencere = pygame.display.set_mode(boyut)
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()  # group içinde sprite sprite parcacıklara denir 2D oyunlardaki


class parca(pygame.sprite.Sprite):  # nesne tabanlı programlama
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 100))  # 100 e 100 lük bir image oluşsturuyoruz muhakkak surface olmak zorunda
        self.image.fill((0, 255, 0))
        self.rect==self.image.get_rect()   #rectengıl boş dikdörtgen döndürüyor bize muhakkak rectengıl olması gerekiyor
        self.rect.center=(width/2,height/2)   #tam ortayı bulup carpa  için kullandık
parca1=Parca
all_sprites.add(parca1)

while True:
    clock.tick(60)
    for event in pygame.event.get():  # her türlü eventi çağırmamızı sağlar
        if event.type == pygame.QUİT: sys.exit()
