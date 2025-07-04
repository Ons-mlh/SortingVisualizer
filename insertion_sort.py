import pygame

from sorting_utils import draw_new_bars, draw_array, draw_stats, draw_complexity, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Insertion Sort Visualization")

running = True
comparaisons = 0
shifts = 0

parameters = {
    "comparaisons": comparaisons,
    "shifts": shifts,
}

def insertion_sort(arr):
    n = len(arr)  
    global parameters
    if n <= 1:
        return 

    for i in range(1, n): 
        key = arr[i]  
        j = i-1
        while j >= 0:
            draw_new_bars(arr, screen, parameters, indices=[j, j + 1])
            parameters["comparaisons"] += 1 
            if key < arr[j]:  
                arr[j + 1] = arr[j]  
                parameters["shifts"] += 1 
                draw_new_bars(arr, screen, parameters, indices=[j, j + 1])         
                j -= 1
            else:
                break
        arr[j+1] = key
        parameters["shifts"] += 1
        draw_new_bars(arr, screen, parameters, indices=[j + 1])
        

draw_array(array, screen, "Insertion Sort Visualization")
pygame.time.delay(500)  

insertion_sort(array)

draw_array(array, screen, "Insertion Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n²)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()