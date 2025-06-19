import pygame

from sorting_utils import draw_new_bars, draw_array, draw_stats, draw_complexity, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Bubble Sort Visualization")

running = True 
comparaisons = 0
swaps = 0

parameters = {
    "comparaisons": comparaisons,
    "swaps": swaps,
}

def bubble_sort(arr):
    global  parameters

    for n in range(len(arr) - 1, 0, -1):
       
        swapped = False  

        for i in range(n):
            parameters["comparaisons"] += 1
            draw_new_bars(arr, screen, parameters, indices=[i, i + 1])
            if arr[i] > arr[i + 1]:
              
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                parameters["swaps"] += 1
                draw_new_bars(arr, screen, parameters, indices=[i, i + 1])

        if not swapped:
            break

draw_array(array, screen, "Bubble Sort Visualization")
pygame.time.delay(500)

bubble_sort(array)
draw_array(array, screen, "Bubble Sort Visualization")
draw_stats(screen, parameters)

draw_complexity("O(n²)",screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

pygame.quit()