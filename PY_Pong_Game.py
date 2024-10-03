import pygame
pygame.init()


WIDTH, HEIGHT, = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw(win):
    win.fill()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()