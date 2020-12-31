import pygame
import win32gui

pygame.init()
screen = pygame.display.set_mode((200,200), pygame.NOFRAME) # For borderless, use pygame.NOFRAME
pygame.display.set_caption("Bar")

hwnd = pygame.display.get_wm_info()['window']

win32gui.MoveWindow(hwnd, 0, 0, 200, 200, 1)

#You can render some text
white=(255,255,255)
blue=(0,0,255)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.fill(white)  # Transparent background
    pygame.display.flip()