import pygame
import colorsys
import random

pygame.init()

font1 = pygame.font.Font(None, 28)
font2 = pygame.font.Font(None, 45)

array = [random.randint(1, 500) for _ in range(100)]
bar_height = 6

def draw_bar (arr, index, array, screen, y=20):
    value = arr[index]
    if max(array) == min(array):
        norm = 0.5  
    else:
        norm = (value - min(array)) /( (max(array)) - min(array))
    hue = norm 
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
   
    color = (int(r * 255), int(g * 255), int(b * 255))
        
    pygame.draw.rect(screen, (0, 0, 0), (0, y + index * bar_height, 500, bar_height))
    pygame.draw.rect(screen, color, (0, y + index * bar_height, value, bar_height))

def draw_new_bars(array, screen, parameters, indices=[],):

    for i in indices:
        draw_bar(array, i, array, screen, 20 )

    draw_stats(screen, parameters)
    pygame.display.update()
    pygame.time.delay(20)

def draw_array(array,screen, title):
    screen.fill((0, 0, 0))
    title = font2.render(f"{title}", True, (239, 71, 111))
    screen.blit(title, (550, 50))
    for i in range(len(array)):
        draw_bar(array, i, array, screen, 20)
    pygame.display.update()

def draw_stats(screen, parameters):
    pygame.draw.rect(screen, (0, 0, 0), (600, 230, 220, 400))
    x = 0
    for i, param in parameters.items():
        text = font1.render(i + " : " + str(param), True, (255, 255, 255))
        screen.blit(text, (600, 250 + x * 50))
        x += 1
    pygame.display.update()

def draw_complexity(complexity,screen):
    complexity_text = font2.render(f"Time Complexity: {complexity}", True, (239, 71, 111))
    screen.blit(complexity_text, (550, 500))
    pygame.display.update()

def highlight_bar (array, index, screen):
    pygame.draw.rect(screen, (255, 255, 255), (0, 20 + index * bar_height, array[index], bar_height))
    pygame.display.update()
    pygame.time.delay(100) 
    draw_bar(array, index, array, screen, 20)

def draw_counting_updates(count_updates, screen):
    pygame.draw.rect(screen, (0, 0, 0), (600, 100, 400, 20))
    text = font1.render("Counting...", True, (255, 255, 255)) 
    screen.blit(text, (600, 100))
    pygame.draw.rect(screen, (0, 0, 0), (600, 200, 400, 20))
    text = font1.render(f"Counting updates : {count_updates}", True, (255, 255, 255))
    screen.blit(text, (600, 200 ))