import sys
import pygame as pg
from random import random
from copy import deepcopy

W: int = 20
H: int = 20

FPS = 10

CELL_SIZE = 35

WIDTH = W * CELL_SIZE
HEIGHT = H * CELL_SIZE

BG_COLOR = (15, 15, 15)
CELL_COLOR = (236, 128, 39)
CIRCLE = True

class Cell:
	"""
	Cell class that holds the information of each cell, including the position
	"""
	def __init__(self, x: int, y: int, state: bool = False) -> None:
		self.x = x
		self.y = y
		self.state: bool = state

	def __eq__(self, other: tuple | object) -> bool:
		if isinstance(other, tuple):
			return self.astuple == other

		elif isinstance(other, Cell):
			return ((self.x == other.x) and (self.y == other.y))


	def __ne__(self, other: tuple | object) -> bool:
		if isinstance(other, tuple):
			return self.astuple != other

		elif isinstance(other, Cell):
			return ((self.x != other.x) or (self.y != other.y))


	@property
	def astuple(self):
		return (self.x, self.y)


	def __repr__(self) -> str:
		return str(self.astuple)



class GameOfLife:
	def __init__(self, width: int, height: int) -> None:
		self.width = width
		self.height = height

		self.world: list[list[Cell]] = [
			[Cell(x=x, y=y) for x in range(width)]
			for y in range(height)
		]

		self.num_alives: list[list[int]] = [[0 for c in range(self.width)] for r in range(self.height)]
		self.compute_num_alives()


	def randomize(self, alive_prob: float = 0.5) -> None:
		"""
		This method will randomize self.world, with the alive probabilty of alive_prob: float [0 - 1]
		"""
		self.world = [
			[Cell(x=x, y=y, state=bool(random() < alive_prob)) for x in range(self.width)]
			for y in range(self.height)
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

						if self.world[r_n%self.height][c_n%self.width].state:
							num_alives += 1
				# now we counted all the alive cells in the neighborhood of the current cell
				self.num_alives[r][c] = num_alives



	def evolve(self) -> None:
		self.compute_num_alives()

		for r in range(self.height):
			for c in range(self.width):
				pass




class GOL_GAME:
	def __init__(self) -> None:
		pg.init()
		pg.display.set_caption('Game of Life')

		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		self.fps = FPS
		self.gol: GameOfLife = GameOfLife(width=WIDTH, height=HEIGHT)
		self.gol.randomize()

		self.screen.fill(color=BG_COLOR)


	def draw_world(self) -> None:
		for r in range(self.gol.height):
			for c in range(self.gol.width):
				cell: Cell = self.gol.world[r][c]

				top = r * CELL_SIZE
				left = c * CELL_SIZE
				rect = (left, top, CELL_SIZE, CELL_SIZE)

				color = CELL_COLOR if cell.state else BG_COLOR
				radius = CELL_SIZE if CIRCLE and cell.state else 0
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
		game.step()