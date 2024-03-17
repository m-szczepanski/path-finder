import pygame
import heapq
import random
import time

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

