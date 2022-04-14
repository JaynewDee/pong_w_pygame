import pygame, sys

print(sys.path)
def animate_ball():
   global speed_x, speed_y

   ball.x += speed_x
   ball.y += speed_y

   if ball.top <= 0 or ball.bottom >= screenHeight:
      speed_y *= -1
   if ball.left <=0 or ball.right >= screenWidth:
      speed_x *= -1

   if ball.colliderect(player) or ball.colliderect(opponent):
      speed_x *= -1

def set_difficulty(setting, speedx, speedy):
   if setting == 1:
      speedx = 3
      speedy = 2
   if setting == 2:
      speedx = 6
      speedy = 4


def animate_player():
   player.y += player_speed
   if player.top <= 0:
      player.top = 0
   if player.bottom >= screenHeight:
      player.bottom = screenHeight

def animate_opponent():
   if opponent.top < ball.y:
      opponent.top += 7
   if opponent.bottom > ball.y:
      opponent.bottom -= 7
   if opponent.top <= 0:
      opponent.top = 0
   if opponent.bottom >= screenHeight:
      opponent.bottom = screenHeight

pygame.init()
clock = pygame.time.Clock()

screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Classic pong!')

# Rectangles
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth - 20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2 - 70, 10, 140)

backgroundColor = pygame.Color(255,255,255)
grey = (50,50,100)

speed_x = 3
speed_y = 2
player_speed = 0
opponent_speed = 0
paused = True

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_SPACE:
            paused = not paused
         if event.key == pygame.K_DOWN:
            player_speed +=7
         if event.key == pygame.K_UP:
            player_speed -=7
      if event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            player_speed -=7
         if event.key == pygame.K_UP:
            player_speed +=7
      
   if paused == False:
      animate_ball()
      animate_player()
      animate_opponent()
   screen.fill(backgroundColor)
   pygame.draw.aaline(screen, grey, (screenWidth/2,0), (screenWidth/2, screenHeight))

   pygame.draw.rect(screen, grey, player)
   pygame.draw.rect(screen, grey, opponent)
   pygame.draw.ellipse(screen, (255,50,50), ball)


   pygame.display.flip()
   clock.tick(120)