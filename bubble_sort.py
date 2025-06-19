import pygame

from sorting_utils import draw_new_bars2, draw_array, draw_stats2, draw_complexity, font1, font2, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Bubble Sort Visualization")

running = True 
comparaisons = 0
swaps = 0

def bubble_sort(arr):
    global  comparaisons, swaps

    for n in range(len(arr) - 1, 0, -1):
       
        swapped = False  

        for i in range(n):
            comparaisons += 1
            draw_new_bars2(arr, screen, comparaisons=comparaisons, swaps=swaps, indices=[i, i + 1])
            if arr[i] > arr[i + 1]:
              
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                swaps += 1
                draw_new_bars2(arr, screen, comparaisons=comparaisons, swaps=swaps, indices=[i, i + 1])

        if not swapped:
            break

draw_array(array, screen, "Bubble Sort Visualization")
pygame.time.delay(500)

bubble_sort(array)
draw_array(array, screen, "Bubble Sort Visualization")
draw_stats2(screen, comparaisons, swaps)

draw_complexity("O(n²)",screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 

pygame.quit()