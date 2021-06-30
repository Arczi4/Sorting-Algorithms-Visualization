import sys
import pygame
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

screen_width = 860
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Sorting visualization')

font = pygame.font.SysFont('Constantia', 30)

#define colours
bg = (0, 0, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

#define global variable
clicked = False

class Button():
    #colours for button and text
    hover_col = (75, 225, 255)
    click_col = (50, 150, 255)
    text_col = black
    width = 180
    height = 70


    def __init__(self, x, y, color, text):
        self.x = x
        self.y = y
        self.text = text
        self.color = color

    def draw_button(self):

        global clicked
        action = False

        #get mouse position
        pos = pygame.mouse.get_pos()

        #create pygame Rect object for the button
        button_rect = Rect(self.x, self.y, self.width, self.height)

        #check mouseover and clicked conditions
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.color, button_rect)

        #add text to button
        text_img = font.render(self.text, True, self.text_col)
        text_len = text_img.get_width()
        screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 25))
        return action

class Rectangle:
    pass

def bubble_sort():
    running = True
    while running:
        screen.fill((255,255,255))
        start = Button(650, 550, (0, 125, 255), 'Start BS')
        back = Button(20, 550, (255,140,0), 'Back')

        if start.draw_button():
            print('Started bubble sort')
            
        if back.draw_button():
            running = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        pygame.display.update()
        mainClock.tick(60)

def quicksort():
    running = True
    while running:
        screen.fill((255,255,255))
        start = Button(650, 550, (0, 125, 255), 'Start QS')
        back = Button(20, 550, (255,140,0), 'Back')
        
        if start.draw_button():
            print('Started quicksort')
            
        if back.draw_button():
            running = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    

        pygame.display.update()
        mainClock.tick(60)


btn_bubble_sort = Button(320, 100, (0, 125, 255), 'Bubble sort')
btn_quicksort = Button(320, 200, (0, 125, 255), 'Quicksort')
btn_quit = Button(320, 500, (255, 0, 0), 'Quit')

run = True
while run:
    screen.fill(bg)

    if btn_bubble_sort.draw_button():
        print('Bubble')
        bubble_sort()

    if btn_quicksort.draw_button():
        print('Quicksort')
        quicksort()

    if btn_quit.draw_button():
        print('Quit')
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()