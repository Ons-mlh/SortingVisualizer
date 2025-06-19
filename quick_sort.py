import pygame

from sorting_utils import draw_new_bars, draw_array, draw_stats, draw_complexity, array

pygame.init() 
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Quick Sort Visualization")

running = True

comparaisons = 0
swaps = 0
operations = 0

parameters = {
    "comparaisons": comparaisons,
    "swaps": swaps,
    "operations": operations
}

def partition(arr, low, high):
    global parameters
    i = (low - 1)
    pivot = arr[high]
    
    for j in range(low, high):
        parameters["comparaisons"] += 1
        draw_new_bars(arr, screen, parameters, [j,high])

        if arr[j] <= pivot:
            i += 1
            parameters["swaps"] += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_new_bars(arr, screen, parameters, [i,j])
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    parameters["swaps"] += 1
    draw_new_bars(arr, screen, parameters, [i + 1, high]) 
    return i + 1

def quick_sort (arr, low, high):
    global parameters
    if low < high:
        parameters["operations"] += 1

        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

draw_array(array, screen, "Quick Sort Visualization")
pygame.time.delay(500)

quick_sort(array, 0, len(array) - 1)

draw_array(array, screen, "Quick Sort Visualization")
draw_stats(screen, parameters)

draw_complexity("O(n log n)",screen)

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
pygame.quit()