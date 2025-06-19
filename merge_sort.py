import pygame 

from sorting_utils import draw_bar, draw_stats, draw_array, draw_complexity, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Merge Sort Visualization")

comparaisons = 0
swaps = 0
operations = 0

running = True

def draw_new_bars(indices=[]):
   
    for i in range(len(array)):
        if i in indices:
            draw_bar(array, i, array, screen ,20)
        else:
            draw_bar(array, i, array, screen ,20)


    draw_stats(screen, operations, comparaisons, swaps)
    pygame.display.update()
    pygame.time.delay(20)



def merge(arr, l, m, r):
    global comparaisons, swaps
    
    n1 = m - l + 1
    n2 = r - m

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = 0     
    j = 0     
    k = l     

    while i < n1 and j < n2:
        comparaisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        swaps += 1
        draw_new_bars([k])
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        swaps += 1
        draw_new_bars([k])

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        swaps += 1
        draw_new_bars([k])


def merge_sort(arr, l, r):
    global operations
    if l < r:
        operations += 1
        m = l+(r-l)//2

        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)

draw_array(array, screen, "Merge Sort Visualization")
pygame.time.delay(500)

merge_sort(array,0,99)
draw_array(array, screen, "Merge Sort Visualization")
draw_stats(screen, operations, comparaisons, swaps)

draw_complexity("O(n log n)",screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()