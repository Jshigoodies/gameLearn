import pygame

run = True

#run the game so the exit code isn't 0 until i close it
while run:
    pygame.init()
    #window
    window = pygame.display.set_mode((852, 480))
    #title
    pygame.display.set_caption("FirstGAME")

    #time
    clock = pygame.time.Clock()

    #animations
    walkRight = [pygame.image.load("R1.png"), pygame.image.load("R2.png"), pygame.image.load("R3.png")]
    walkLeft = [pygame.image.load("L1.png"), pygame.image.load("L2.png"), pygame.image.load("L3.png")]
    background = pygame.image.load("bg.jpg")
    idle = pygame.image.load("Standing.png")


    #variables
    x = 50 #position
    y = 416

    width = 64 #the size of the image is 64x64 pixels
    height = 64
    velocity = 5

    isJump = False
    jumpVelocity = 10

    left = False
    right = False
    walkCount = 0


    #methods
    def reDrawGameWindow(): #redraws the whole window

        global walkCount

        window.blit(background, (0, 0))

        #i don't want the rectangles to exist permanently
        # window.fill((0, 0, 0))

        #player, literally a rectangle
        # pygame.draw.rect(window, (255, 0, 0), (x, y, width, height)) #rect( on what display, what color, (position, position, size, size))

        if walkCount + 1 >= 9: # i could just use 3, but i did //3 so it slows the animation a little bit
            walkCount = 0

        if left:
            window.blit(walkLeft[walkCount//3], (x, y))
            walkCount = walkCount + 1
        elif right:
            window.blit(walkRight[walkCount//3], (x, y))
            walkCount = walkCount + 1
        else:
            window.blit(idle, (x, y))

        pygame.display.update()

    #the game running now
    while run:
        # pygame.time.delay(50)

        clock.tick(27)

        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        #movment
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and x > 0:
            x = x - velocity #position minus number
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 852 - width:
            x = x + velocity # position add number
            right = True
            left = False
        else:
            right = False
            left = False
            walkCount = 0

        if not(isJump): #so it doesn't infinently jump in the air
            # if keys[pygame.K_UP] and y > 0:
            #     y = y - velocity # position subtract because the top right of the screen is point (0, 0)
            # if keys[pygame.K_DOWN] and y < 480 - height:
            #     y = y + velocity # you get the point
            if keys[pygame.K_SPACE]:
                isJump = True
                # right = False #i don't really need these
                # left = False
                walkCount = 0
        else: #jump
            # if jumpVelocity >= -10: #just like physics, it would have the same magnitude, but in the negative direction
            #     y = y - jumpVelocity
            #     jumpVelocity = jumpVelocity - 1

            if jumpVelocity >= -10: #i like this one, gives it a hang time and more fluent
                y = y - (jumpVelocity * abs(jumpVelocity)) * 0.5
                jumpVelocity = jumpVelocity - 1

            else:
                isJump = False
                jumpVelocity = 10

        reDrawGameWindow()
pygame.quit()