import pygame


class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(hero_sprite)
        self.move = False
        self.image = pygame.Surface((20, 20))
        self.image.fill(pygame.Color('blue'))
        self.rect = self.image.get_rect()
        self.rect.x = x - 10
        self.rect.y = y - 10

    def update(self):
        self.move = False
        if not pygame.sprite.spritecollideany(self, rectangle_sprite):
            self.rect = self.rect.move(0, 1)
        else:
            self.move = True

    def moving(self, side):
        if self.move:
            if side == 'L':
                self.rect.x -= 10
            else:
                self.rect.x += 10


class Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(rectangle_sprite)
        self.image = pygame.Surface((50, 10))
        self.image.fill(pygame.Color('grey'))
        self.rect = self.image.get_rect()
        self.rect.x = x - 25
        self.rect.y = y - 5


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Платформы')
    size = 500, 500
    hero_sprite = pygame.sprite.Group()
    screen = pygame.display.set_mode(size)
    rectangle_sprite = pygame.sprite.Group()
    running = True
    hero = None
    fps = 50
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if hero is not None:
                        hero_sprite.remove(hero)
                    x, y = event.pos
                    hero = Hero(x, y)
                if event.button == 1:
                    x, y = event.pos
                    Rectangle(x, y)
            if event.type == pygame.KEYDOWN:
                if hero is not None:
                    if event.key == pygame.K_LEFT:
                        hero.moving('L')
                    if event.key == pygame.K_RIGHT:
                        hero.moving('R')
        screen.fill(pygame.Color('black'))
        hero_sprite.draw(screen)
        hero_sprite.update()
        rectangle_sprite.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
