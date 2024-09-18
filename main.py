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

#Set game value:  CONSTANT_NAME, value
''' 5 CONSTANTS
PLAYER_STARTING_LIVES, 5
PLAYER_VELOCITY, 10
COIN_STARTING_VELOCITY, 10
COIN_ACCELERATION, 0.5
BUFFER_DISTANCE, 100
'''
PLAYER_STARTING_LIVES = 5


PLAYER_STARTING_LIVES = 5
'''create a variable that tracks and score and give it a staring value of 0 '''
''' create a variable that tracks the player lives and set it equal to the constant that stores player starting lives '''
''' create a variable that tracks the coin velocity and set it equal to the constant that coin starting velocity '''

#Set colors
GREEN = (0, 255, 0)
DARK_GREEN = (10, 50, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Set fonts
font = pygame.font.Font('AttackGraffiti.ttf', 32)

#Sets the text for the sorce
'''
variable names:  score_text, score_rect
render text: "Score: " + str(score)
antialias: True
color: GREEN
background: DARKGREEN
rect location: topleft = (10, 10)  
'''
score_text = font.render("Score: " + str(10), True, GREEN, DARK_GREEN)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

#Sets the text for lives
'''
variable names: lives_text, lives_rect
render text: "Lives: " + str(player_lives)
True
color: GREEN
background: DARKGREEN
rect location: y = 10
'''

#Sets the text for game over
'''
Variable: game_over_text
Rect: game_over_rect
PHRASE: "GAMEOVER" ,
Antialias: True
Color: GREEN,
Background: DARKGREEN,
Position: center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
'''
#Set Text for Continue (Similar to Score)
'''
variable names: continue_text, continue_rect
render text: "Press any key to play again"
True
color: GREEN
background: DARKGREEN
rect location: center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 32)
'''

#The main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#Fill the display
display_surface.fill(BLACK)

display_surface.blit(score_text, score_rect)


pygame.quit()
