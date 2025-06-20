import pygame

from sorting_utils import draw_new_bars, highlight_bar, draw_array, draw_stats, draw_complexity, draw_counting_updates, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Tim Sort Visualization")

running = True
merges = 0
iterations= 0
min_run_size = 32
current_run = 0

parameters = {
    "merges": merges,
    "min_run_size": min_run_size,
    "iterations": iterations,
    "current_run": current_run,
}

def insertion_sort(arr, left=0, right=None):
    global parameters
    if right is None:
        right = len(arr) - 1

    for i in range(left + 1, right + 1):
        parameters["iterations"] += 1

        key = arr[i]  
        j = i-1
        while j >= left:
            draw_new_bars(arr, screen, parameters, indices=[j, j + 1])
         
            if key < arr[j]:  
                arr[j + 1] = arr[j]  

                draw_new_bars(arr, screen, parameters, indices=[j, j + 1])         
                j -= 1
            else:
                break
        arr[j+1] = key
     
        draw_new_bars(arr, screen, parameters, indices=[j + 1])
    
    if screen and parameters and "current_run" in parameters:
        run_start = parameters["current_run"] * (right - left + 1)
        for i in range(left, right + 1):
            draw_new_bars(arr, screen, parameters, indices=[i])
        pygame.time.delay(50)

    return arr


def merge(left, right, arr=None, start_index=0):
    global parameters
    parameters["merges"] += 1

    i = j = 0
    merged = []

    while i < len(left) and j < len(right):
        parameters["iterations"] += 1

        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
        parameters["iterations"] += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
        parameters["iterations"] += 1

    if arr is not None and screen is not None:
        for k, val in enumerate(merged):
            arr[start_index + k] = val
            draw_new_bars(arr, screen, parameters, indices=[start_index + k])

    return merged

def tim_sort(arr):
    global parameters
    min_run = 32
    parameters["min_run_size"] = min_run
    n = len(arr)

    for i in range(0, n, min_run):
        parameters["current_run"] += 1
        insertion_sort(arr, i, min(i + min_run - 1, (n - 1)))
        parameters["iterations"] += 1

    size = min_run
    while size < n:

        for start in range(0, n, size * 2):
            parameters["iterations"] += 1

            midpoint = start + size
            end = min(start + size * 2 - 1, n - 1)

            left = arr[start:midpoint]
            right = arr[midpoint:end + 1]

            merged_array = merge(left, right, arr, start)

        size *= 2
    return arr


draw_array(array, screen, "Tim Sort Visualization")
pygame.time.delay(500)  

sorted_arr = tim_sort(array)

draw_array(sorted_arr, screen, "Tim Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n * log n)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()