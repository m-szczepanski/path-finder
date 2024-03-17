import pygame
import heapq
import random
import time

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# A* algorithm
def a_star(start, goal, obstacles):
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:
        current = heapq.heappop(frontier)[1]

        if current == goal:
            break

        for next in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next = (current[0] + next[0], current[1] + next[1])
            if 0 <= next[0] < board_size and 0 <= next[1] < board_size and next not in obstacles:
                new_cost = cost_so_far[current] + 1
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost + heuristic(goal, next)
                    heapq.heappush(frontier, (priority, next))
                    came_from[next] = current

    return came_from, cost_so_far

pygame.init()

# board settings
board_size = 100
win_size = (1000, 1000)
win = pygame.display.set_mode(win_size)

# player position
player_pos = [0, 0]
coin_pos = [random.randint(0, board_size-1), random.randint(0, board_size-1)]

# obstacle position
obstacles = [(random.randint(0, board_size-1), random.randint(0, board_size-1)) for _ in
             range(int(board_size*board_size*0.3))]

