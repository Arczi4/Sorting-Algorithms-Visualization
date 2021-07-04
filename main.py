import sys
import pygame
import random
from pygame.locals import *
import time

pygame.init()
mainClock = pygame.time.Clock()

WIDTH = 860
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

def generate_height():
    return [random.randint(1, 400) for _ in range(70)]

def display_rect(height_list):
    initial_x = 20
    initial_y = 30
    
    for height in height_list:
        pygame.draw.rect(screen, (0,0,255), (initial_x + 20, initial_y, 10, height))
        initial_x += 11
        
def partition(height_list, low, high):
    i = (low - 1)
    pivot = height_list[high]
    
    for j in range(low, high):
        if height_list[j] <= pivot:
            i += 1
            height_list[i], height_list[j] = height_list[j], height_list[i]
            screen.fill((255,255,255))
            display_rect(height_list)
            pygame.time.delay(30)
            pygame.display.update()
    
    height_list[i + 1], height_list[high] = height_list[high], height_list[i + 1]
    screen.fill((255,255,255))
    display_rect(height_list)
    pygame.time.delay(30)
    pygame.display.update()
    return (i + 1)

def quick_sort(height_list, low, high):
    if len(height_list) == 1:
        return height_list
    
    if low < high:
        pi = partition(height_list, low, high)

        quick_sort(height_list, low, pi - 1)
          
        quick_sort(height_list, pi + 1, high)
        

def bubble_sort_screen():
    
    running = True
    rect_height = generate_height()
    while running:
        mainClock.tick(60)
        screen.fill((255,255,255))
        start = Button(650, 550, (0, 125, 255), 'Start BS')
        back = Button(20, 550, (255,140,0), 'Back')
        display_rect(rect_height)
        
        if start.draw_button():
            print("Bubble sort stated")
            
            for i in range(len(rect_height) - 1):
                for j in range(len(rect_height) - i -1):
                    if rect_height[j] > rect_height[j+1]:
                        rect_height[j], rect_height[j+1] = rect_height[j+1], rect_height[j]
                    
                    screen.fill((255,255,255))
                    display_rect(rect_height)
                    pygame.time.delay(30)
                    pygame.display.update()
            
            print("Bubble sort finised")

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


def quicksort_screen():
    running = True
    rect_height = generate_height()
    while running:
        mainClock.tick(60)
        screen.fill((255,255,255))
        start = Button(650, 550, (0, 125, 255), 'Start QS')
        back = Button(20, 550, (255,140,0), 'Back')
        display_rect(rect_height)
        
        if start.draw_button():
            print("Quick sort stated")
            
            quick_sort(rect_height, 0, len(rect_height) - 1)
            
            print("Quick sort  finised")

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

btn_bubble_sort = Button(320, 100, (0, 125, 255), 'Bubble sort')
btn_quicksort = Button(320, 200, (0, 125, 255), 'Quicksort')
btn_quit = Button(320, 500, (255, 0, 0), 'Quit')

run = True
while run:
    screen.fill(bg)

    if btn_bubble_sort.draw_button():
        print('Bubble')
        bubble_sort_screen()

    if btn_quicksort.draw_button():
        print('Quicksort')
        quicksort_screen()

    if btn_quit.draw_button():
        print('Quit')
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()