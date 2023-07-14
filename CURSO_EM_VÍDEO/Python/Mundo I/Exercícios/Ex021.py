import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input() #'''aqui tive que colocar essa input pois a atualização do python 'obriga' a escrever isso para poder reproduzir'''
pygame.event.wait()
