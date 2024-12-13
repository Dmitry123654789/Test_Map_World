import pygame
from pytmx import load_pygame, TiledTileLayer

SIZE = (1000, 650)
CELL_SIZE = 50


def main():
    pygame.init()
    pygame.display.set_caption('Castle')
    screen = pygame.display.set_mode(SIZE)

    screen.fill(pygame.Color('black'))
    pygame.display.flip()

    world = pygame.sprite.Group()
    tmx_map = load_pygame('world.tmx')
    title_img = tmx_map.get_tile_image_by_gid
    for layer in tmx_map.visible_layers:
        if isinstance(layer, TiledTileLayer):
            for x, y, serf in layer:
                title = title_img(serf)

                if title:
                    title = pygame.transform.scale(title, (CELL_SIZE, CELL_SIZE))
                    screen.blit(title, (x * CELL_SIZE, y * CELL_SIZE))

    running = True
    fps = 100
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        world.draw(screen)
        pygame.display.flip()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
