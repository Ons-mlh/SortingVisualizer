import pygame

from sorting_utils import draw_new_bars, highlight_bar, draw_array, draw_stats, draw_complexity, draw_counting_updates, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Counting Sort Visualization")

running = True
count_updates = 0
writes = 0
iterations= 0

parameters = {
    "count_updates": count_updates,
    "writes": writes,
    "iterations": iterations
}

def counting_sort(arr):
    global parameters
    if not arr:
        return []

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for i, num in enumerate(arr):
        parameters["iterations"] += 1
        count[num] += 1
        parameters["count_updates"] += 1
        highlight_bar(arr, i, screen)
        draw_counting_updates(parameters["count_updates"],screen)

    pygame.draw.rect(screen, (0, 0, 0), (600, 100, 400, 20))

    index = 0
    for value, freq in enumerate(count):
        parameters["iterations"] += 1
        if freq > 0:
            for _ in range(freq):
                arr[index] = value
                parameters["writes"] += 1
                draw_new_bars(arr, screen, parameters, indices=[index])
                pygame.time.delay(100)
                index += 1

    return arr

draw_array(array, screen, "Counting Sort Visualization")
pygame.time.delay(500)  

sorted_arr = counting_sort(array)

draw_array(sorted_arr, screen, "Counting Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n + k)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()