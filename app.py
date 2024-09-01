import sys
import pygame as pg
from random import random
import time
#import numpy as np

W: int = 320
H: int = 180

FPS = 500

CELL_SIZE = 20

WIDTH = W * CELL_SIZE
HEIGHT = H * CELL_SIZE

BG_COLOR = (15, 15, 15)
CELL_COLOR = (236, 128, 39)
CIRCLE = False


class GameOfLife:
	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height

		self.world: list[list[bool]] = [
			[False for c in range(self.width)]
			for r in range(self.height)
		]

		self.num_alives: list[list[int]] = [[0 for c in range(self.width)] for r in range(self.height)]
		

	def randomize(self, alive_prob: float = 0.5) -> None:
		"""
		This method will randomize self.world, with the alive probabilty of alive_prob: float [0 - 1]
		"""
		self.world = [
			[(random() < alive_prob) for c in range(self.width)]
			for r in range(self.height)
		]


	def compute_num_alives(self) -> None:
		# loop through each cell in the world
		for r in range(self.height):
			for c in range(self.width):
				num_alives: int = 0
				# loop through the 8 neighbors of this current cell and count the alive cells
				for r_n in range(r-1, r+1+1):
					for c_n in range(c-1, c+1+1):
						# skip over the current cell
						if (r_n, c_n) == (r, c): continue

						if self.world[r_n%self.height][c_n%self.width]:
							num_alives += 1
				# now we counted all the alive cells in the neighborhood of the current cell
				self.num_alives[r][c] = num_alives


	def evolve(self) -> None:
		# compute alive nearby cells for every cell in the current state of the world
		self.compute_num_alives()

		# loop through each cell in the world, and the num_alives list
		for r in range(self.height):
			for c in range(self.width):
				cell = self.world[r][c]
				num_alives = self.num_alives[r][c]
				# it's time to check for the main rules of the game
				if cell:
					if num_alives in (2, 3):
						self.world[r][c] = True
					else:
						self.world[r][c] = False
				else:
					if num_alives == 3:
						self.world[r][c] = True



class GOL_GAME:
	def __init__(self) -> None:
		pg.init()
		pg.display.set_caption('Game of Life')

		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		self.fps = FPS
		self.gol: GameOfLife = GameOfLife(width=W, height=H)
		self.gol.randomize()

		self.screen.fill(color=BG_COLOR)
		pg.display.update()

	def draw_world(self) -> None:
		for r in range(self.gol.height):
			for c in range(self.gol.width):
				cell: bool = self.gol.world[r][c]

				top = r * CELL_SIZE
				left = c * CELL_SIZE
				rect = (left, top, CELL_SIZE, CELL_SIZE)

				color = CELL_COLOR if cell else BG_COLOR
				radius = CELL_SIZE if CIRCLE and cell else 0
				pg.draw.rect(self.screen, rect=rect, color=color, border_radius=radius)


	def	step(self) -> None:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

		self.gol.evolve()
		
		self.draw_world()

		pg.display.update()
		self.clock.tick(self.fps)


if __name__ == '__main__':
	game = GOL_GAME()

	while True:
		start = time.time()
		game.step()
		steptime = time.time() - start
		print(steptime)