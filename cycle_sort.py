import pygame

from sorting_utils import draw_new_bars, draw_array, draw_stats, draw_complexity, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Cycle Sort Visualization")

running = True
comparaisons = 0
writes = 0
cycles = 0

parameters = {
    "comparaisons": comparaisons,
    "writes": writes,
    "cycles": cycles
}

def cycle_sort(array):
    global parameters

    for cycleStart in range(0, len(array) - 1):
        parameters["cycles"] += 1
        item = array[cycleStart]

        pos = cycleStart
        for i in range(cycleStart + 1, len(array)):
            parameters["comparaisons"] += 1
            if array[i] < item:
                pos += 1

        if pos == cycleStart:
            continue

        while pos < len(array) and item == array[pos]:
            pos += 1
        array[pos], item = item, array[pos]
        parameters["writes"] += 1
        draw_new_bars(array, screen, parameters, indices=[cycleStart, pos])
        pygame.time.delay(100)

        while pos != cycleStart:

            pos = cycleStart
            for i in range(cycleStart + 1, len(array)):
                parameters["comparaisons"] += 1
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1
            array[pos], item = item, array[pos]
            parameters["writes"] += 1
            draw_new_bars(array, screen, parameters, indices=[cycleStart, pos])
            pygame.time.delay(100)
        
draw_array(array, screen, "Cycle Sort Visualization")
pygame.time.delay(500)  

cycle_sort(array)

draw_array(array, screen, "Cycle Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(n²)", screen)

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()