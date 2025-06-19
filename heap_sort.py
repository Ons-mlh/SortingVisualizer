import pygame

from sorting_utils import draw_new_bars, draw_array, draw_stats, draw_complexity, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Heap Sort Visualization")

running = True
comparaisons = 0
swaps = 0
heapify_calls = 0

parameters = {
    "comparaisons": comparaisons,
    "swaps": swaps,
    "heapify_calls": heapify_calls
}

def heapify(arr, n, i):
    global parameters
    parameters["heapify_calls"] += 1
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2 

    if l < n and arr[i] < arr[l]:
        largest = l
        parameters["comparaisons"] += 1

    if r < n and arr[largest] < arr[r]:
        largest = r
        parameters["comparaisons"] += 1

    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i]) 
        parameters["swaps"] += 1
        draw_new_bars(arr, screen, parameters, indices=[i, largest])
        heapify(arr, n, largest)

def heap_sort(arr):
    global parameters
    n = len(arr)

    for i in range(n // 2 -1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        parameters["swaps"] += 1
        draw_new_bars(arr, screen, parameters, indices=[0, i])
        heapify(arr, i, 0)
        
draw_array(array, screen, "Heap Sort Visualization")
pygame.time.delay(500)  

heap_sort(array)

draw_array(array, screen, "Heap Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n log n)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()