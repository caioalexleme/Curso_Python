'''import pygame
pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''
from pygame import mixer
mixer.init()
mixer.music.load('musica.mp3')
mixer.music.play()
import time
time.sleep(360)
