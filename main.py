import pygame

#Set display surface
pygame.init()

#Set display surface
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 400
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed The Dragon")

#Set FPS and clock
FPS = 60
clock = pygame.time.Clock()

#Set game values
''' create a constant that stores player starting lives ang give it a starting value of 5 ''' # PLAYER_STARTING_lIVES
''' create a constant that stores player velocity and give it a starting value of 10 '''
''' create a constant that stores coin starting velocity and give it a starting value of 10 '''
''' create a constant that stores coin velocity and give it a starting value of 10 '''
''' create a constant that stores coin acceleration and give it a staring value of 0.5 '''

'''create a variable that tracks and score and give it a staring value of 0 '''
''' create a variable that tracks the player lives and set it equal to the constant that stores player starting lives '''
''' create a variable that tracks the coin velocity and set it equal to the constant that coin starting velocity '''

#Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
''' create a varable called font and give it a value from the following: pygame.font.Font('AttackGraffiti.ttf', 32) '''

#Set text
#Sets the text for the sorce
''' create a variable that tracks score text and give it a value from the following: font.render("Score: " + str(score),True, GREEN, WHITE '''
'''
''' create a variable that tracks score rect and give it a value from the following: score_text.get_rect() '''
''' score_rect.topleft = (10, 10)'''

#Sets the text for lives
''' Same deal, variable name lives_text, "Lives: str(plater_lives), True, GREEN, DARKGREEN '''
''' Same deal, variable name lives_rect, get from lives_text '''
''' Same deal, topright = (WINDOW_WIDTH - 10, 10)'''

#Sets the text for game over
'''
Variable: game_over_text
Rect: game_over_rect
PHRASE: "GAMEOVER" ,
Antialias: True
Color: GREEN,
Background: BARKGREEN,
Position: center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
'''

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
