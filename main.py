import pgzrun

WIDTH = 800
HEIGHT = 800

itachi = Actor("itachi.png")
keys = pygame.key.get_press()
if keys[pygame.K_w]:
    y-=1
if keys [pygame.K_s]:
    y+=1
if keys[pygame.K_d]:
    x+=1
if keys[pygame.K_a]:
    x-=1
screen.blit(itachi, (x,y))
pygame.display.flip()
def draw():
  screen.fill("white")
  screen.blit("itachi", (300,145))
  
  pgzrun.go()