import pygame

from sorting_utils import draw_new_bars, highlight_bar, draw_array, draw_stats, draw_complexity, draw_counting_updates, array

pygame.init()
screen = pygame.display.set_mode((1000, 650))
pygame.display.set_caption("Radix Sort Visualization")

running = True
passes = 0
moves = 0
iterations= 0
counting_sort_updates = 0

parameters = {
    "passes": passes,
    "moves": moves,
    "iterations": iterations,
}

def counting_sort(arr, exp1): 
    global counting_sort_updates
    n = len(arr) 

    output = [0] * (n) 

    count = [0] * (10) 
  
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        count[int((index)%10)] += 1
        parameters["iterations"] += 1

    for i in range(1,10): 
        count[i] += count[i-1] 
        parameters["iterations"] += 1
        counting_sort_updates += 1
        highlight_bar(arr, i, screen)
        draw_counting_updates(counting_sort_updates, screen)
    
    pygame.draw.rect(screen, (0, 0, 0), (600, 100, 400, 20))

    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10) ] - 1] = arr[i] 
        count[int((index)%10)] -= 1
        highlight_bar(arr, i, screen)
        i -= 1
        parameters["iterations"] += 1
        parameters["moves"] += 1

    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i]
        parameters["iterations"] += 1
        draw_new_bars(arr, screen, parameters, indices=[i]) 

def radix_sort(arr):

    max1 = max(arr)

    exp = 1
    while max1 // exp > 0:
        counting_sort(arr,exp)
        exp *= 10
        draw_new_bars(arr, screen, parameters)
        parameters["iterations"] += 1
        parameters["passes"] += 1

draw_array(array, screen, "Radix Sort Visualization")
pygame.time.delay(500)  

radix_sort(array)

draw_array(array, screen, "Radix Sort Visualization")
draw_stats(screen, parameters)
draw_complexity("O(d * (n + k))", screen)
pygame.display.update()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()