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
        self.vert = False

    def update(self):
        if not pygame.sprite.spritecollideany(self,
                                              horizontal_rectangle_sprite) and not pygame.sprite.spritecollideany(
            self, vertical_rectangle_sprite):
            self.rect = self.rect.move(0, 1)
            self.vert = False
        if pygame.sprite.spritecollideany(self, vertical_rectangle_sprite):
            self.vert = True

    def moving(self, side):
        if side == 'L':
            self.rect.x -= 10
        elif side == 'R':
            self.rect.x += 10
        if self.vert:
            if side == 'U':
                self.rect.y -= 10
            elif side == 'D':
                self.rect.y += 10


class Horizontal_Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(horizontal_rectangle_sprite)
        self.image = pygame.Surface((50, 10))
        self.image.fill(pygame.Color('grey'))
        self.rect = self.image.get_rect()
        self.rect.x = x - 25
        self.rect.y = y - 5


class Vertical_Rectangle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(vertical_rectangle_sprite)
        self.image = pygame.Surface((10, 50))
        self.image.fill(pygame.Color('red'))
        self.rect = self.image.get_rect()
        self.rect.x = x - 5
        self.rect.y = y - 25


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('Платформы')
    size = 500, 500
    hero_sprite = pygame.sprite.Group()
    screen = pygame.display.set_mode(size)
    horizontal_rectangle_sprite = pygame.sprite.Group()
    vertical_rectangle_sprite = pygame.sprite.Group()
    running = True
    hero = None
    fps = 50
    clock = pygame.time.Clock()
    clicking = False
    keying = False
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
                    clicking = True
                    x, y = event.pos
            if event.type == pygame.KEYDOWN:
                if hero is not None:
                    if event.key == pygame.K_LEFT:
                        hero.moving('L')
                    if event.key == pygame.K_RIGHT:
                        hero.moving('R')
                    if event.key == pygame.K_UP:
                        hero.moving('U')
                    if event.key == pygame.K_DOWN:
                        hero.moving('D')
                if event.mod & pygame.KMOD_CTRL:
                    print('test')
                    keying = True
            if event.type == pygame.KEYUP:
                if event.key == 1073742048:
                    keying = False
        if clicking:
            if keying:
                Vertical_Rectangle(x, y)
            else:
                Horizontal_Rectangle(x, y)
            clicking = False
            keying = False
        screen.fill(pygame.Color('black'))
        hero_sprite.draw(screen)
        hero_sprite.update()
        horizontal_rectangle_sprite.draw(screen)
        vertical_rectangle_sprite.draw(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()
