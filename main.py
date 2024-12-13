import pygame
from pytmx import load_pygame, TiledTileLayer

SIZE = (1000, 650)
CELL_SIZE = 50


class Game:
    def __init__(self):
        pygame.init()
        self.running = True
        self.fps = 100
        self.clock = pygame.time.Clock()
        self.create_screen()
        self.create_world()

    def create_screen(self):
        pygame.display.set_caption('Castle')
        self.screen = pygame.display.set_mode(SIZE)
        self.screen.fill(pygame.Color('black'))

    def create_world(self):
        self.world = pygame.sprite.Group()
        self.tmx_map = load_pygame('world.tmx')
        title_img = self.tmx_map.get_tile_image_by_gid
        for layer in self.tmx_map.visible_layers:
            if isinstance(layer, TiledTileLayer):
                for x, y, serf in layer:
                    title = title_img(serf)

                    if title:
                        title = pygame.transform.scale(title, (CELL_SIZE, CELL_SIZE))
                        self.screen.blit(title, (x * CELL_SIZE, y * CELL_SIZE))

    def set_darkness(self):
        """Затемнение"""
        darkness = pygame.Surface(SIZE)
        darkness.fill(pygame.Color('black'))
        darkness.set_alpha(100)
        self.screen.blit(darkness, (0, 0))

    def run(self):
        self.set_darkness()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.world.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.fps)

        pygame.quit()

    def main(self):
        self.run()


if __name__ == '__main__':
    game = Game()
    game.main()
