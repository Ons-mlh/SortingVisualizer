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

def selection_sort(array, size):
    global parameters
   
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            parameters["comparaisons"] += 1
            if array[j] < array[min_index]:
                min_index = j
                draw_new_bars(array, screen, parameters, indices=[ind, j, min_index])
                pygame.time.delay(50)
                
        if min_index != ind:
            (array[ind], array[min_index]) = (array[min_index], array[ind])
            parameters["swaps"] += 1
            draw_new_bars(array, screen, parameters, indices=[ind, min_index])
            pygame.time.delay(50)

draw_array(array, screen, "Selection Sort Visualization")
pygame.time.delay(500)  

selection_sort(array, len(array))

draw_array(array, screen, "Selection Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n²)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()