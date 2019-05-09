import pygame
from utils import cycle_sprite, update, place_items

pygame.init()

#VALUES
MAX_HEIGHT = 500
MAX_WIDTH = 500
BACKGROUND_COLOR = (255, 100, 255)

SPRITE_WIDTH = 40
SPRITE_HEIGHT = 60

x = (MAX_WIDTH / 2) - (SPRITE_WIDTH / 2)
y = (MAX_HEIGHT / 2) - (SPRITE_HEIGHT / 2)

PLAYER = pygame.image.load("maria.png")
PLAYER_RECT = PLAYER.get_rect()

SPEED = 10

SCORE = 0

#make the window, set bg color
win = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
win.fill(BACKGROUND_COLOR)

run = True

player_cycle = 0

#put the prizes and enemies on the screen

enemy_list = []
enemy_token_list = []

prize_list = []
prize_token_list = []

while run:
  pygame.time.delay(50)
  
  pygame.display.set_caption("SCORE: " + str(SCORE))

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT] and (x-SPEED >= 0):
    x -= SPEED
    player_cycle = update(player_cycle)
  if keys[pygame.K_RIGHT] and (x+SPEED <= MAX_WIDTH-SPRITE_WIDTH):
    x += SPEED
    player_cycle = update(player_cycle)
  if keys[pygame.K_UP] and (y-SPEED >= 0):
    y -= SPEED
    player_cycle = update(player_cycle)
  if keys[pygame.K_DOWN] and (y+SPEED <= MAX_HEIGHT-SPRITE_HEIGHT):
    y += SPEED
    player_cycle = update(player_cycle)
  
  win.fill(BACKGROUND_COLOR)

  pygame.display.update()

pygame.quit()

