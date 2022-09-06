import subprocess
import sys
from time import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pygame']) 
import pygame
sleep(0.01)
subprocess.check_call(['clear'])
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('.wav')
pygame.mixer.music.play(-1)
def yshda():
   pgf = pygame.font.Font(None, 25)
   yshda = pgf.render(":) you shouldn't have done that.", True, 'black')
   screen = pygame.display.set_mode((300,125))
   cl = pygame.time.Clock()
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
      screen.fill('red')
      screen.blit(yshda,(25,50))
      cl.tick(15)
      pygame.display.update()
def joj423():
 for i in range(10):
   subprocess.check_call(['echo', 'you shouldnt have done that.']) 
   subprocess.check_call(['sleep', '0.1'])
 for i in range(20):
   subprocess.check_call(['xdg-open', 'https://www.google.com/search?q=you+shouldn%27t+have+done+that&rlz=1CABBMB_enUS1014&oq=you+shouldn%27t+have+done+that&aqs=chrome..69i57j46i512j0i512l5j69i60.7235j0j7&sourceid=chrome&ie=UTF-8'])
def pyHandler():
   exec.__class__()