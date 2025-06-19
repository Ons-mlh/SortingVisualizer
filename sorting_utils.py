import pygame
import colorsys
import random

pygame.init()

font1 = pygame.font.Font(None, 28)
font2 = pygame.font.Font(None, 45)

array = [random.randint(1, 500) for _ in range(100)]
bar_height = 6

def draw_bar (arr, index,array,screen, y=20):
    value = arr[index]
    norm = (value - min(array)) / (max(array) - min(array))
    hue = norm 
    r, g, b = colorsys.hsv_to_rgb(hue, 1, 1)
   
    color = (int(r * 255), int(g * 255), int(b * 255))
        
    pygame.draw.rect(screen, (0, 0, 0), (0, y + index * bar_height, 500, bar_height))
    pygame.draw.rect(screen,color,(0, y + index * bar_height, value, bar_height))

def draw_new_bars(array, screen, operations, comparaisons, swaps,  indices=[],):

    for i in indices:
        draw_bar(array, i, array, screen, 20 )

    draw_stats(screen, operations, comparaisons, swaps)
    pygame.time.delay(20)

def draw_new_bars2(array, screen, comparaisons, swaps,  indices=[],):

    for i in indices:
        draw_bar(array, i, array, screen, 20 )

    draw_stats2(screen, comparaisons, swaps)
    pygame.time.delay(20)

def draw_array(array,screen, title):
    screen.fill((0, 0, 0))
    title = font2.render(f"{title}", True, (239, 71, 111))
    screen.blit(title, (550, 50))
    for i in range(len(array)):
        draw_bar(array, i, array, screen, 20)
    pygame.display.update()

def draw_stats (screen, operations, comparaisons, swaps):
    pygame.draw.rect(screen, (0, 0, 0), (600, 180, 220, 400))
    text1 = font1.render(f"Recursive splits: {operations}", True, (255, 255, 255))
    text2 = font1.render(f"Comparaisons: {comparaisons}", True, (255, 255, 255))
    text3 = font1.render(f"Swaps: {swaps}", True, (255, 255, 255))
    screen.blit(text1, (600, 200))
    screen.blit(text2, (600, 300))
    screen.blit(text3, (600, 400))
    pygame.display.update()

def draw_stats2 (screen, comparaisons, swaps):
    pygame.draw.rect(screen, (0, 0, 0), (600, 180, 220, 400))
    text1 = font1.render(f"Comparaisons: {comparaisons}", True, (255, 255, 255))
    text2 = font1.render(f"Swaps: {swaps}", True, (255, 255, 255))
    screen.blit(text1, (600, 200))
    screen.blit(text2, (600, 300))
    pygame.display.update()

def draw_complexity(complexity,screen):
    complexity_text = font2.render(f"Time Complexity: {complexity}", True, (239, 71, 111))
    screen.blit(complexity_text, (550, 500))
    pygame.display.update()