import pygame

run = True

while run:
    pygame.init()
    #window
    window = pygame.display.set_mode((500, 500))
    #title
    pygame.display.set_caption("FirstGAME")

    x = 50
    y = 50

    width = 40
    height = 60
    velocity = 5

    while run:
        pygame.time.delay(100)

        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        #movment
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x = x - velocity #position minus number
        if keys[pygame.K_RIGHT]:
            x = x + velocity # position add number
        if keys[pygame.K_UP]:
            y = y - velocity # position subtract because the top right of the screen is point (0, 0)
        if keys[pygame.K_DOWN]:
            y = y + velocity # you get the point

        #i don't want the rectangles to exist permanently
        window.fill((0, 0, 0))

        #player, literally a rectangle
        pygame.draw.rect(window, (255, 0, 0), (x, y, width, height)) #rect( on what display, what color, (position, position, size, size))
        pygame.display.update()

pygame.quit()