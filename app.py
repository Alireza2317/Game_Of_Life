import sys
import pygame as pg
from random import randint
from copy import deepcopy

W: int = 20
H: int = 20

FPS = 10

CELL_SIZE = 10

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
	
	def randomize(self) -> None:
		self.world = [
			[Cell(x=x, y=y, state=bool(randint(0, 1))) for x in range(self.width)]
			for y in range(self.height)
		]
	

	def evolve(self) -> None:
		pass



class GOL_GAME:
	def __init__(self) -> None:
		pg.init()
		self.screen = pg.display.set_mode((WIDTH, HEIGHT))
		self.clock = pg.time.Clock()
		self.fps = FPS
		self.gol: GameOfLife = GameOfLife(width=WIDTH, height=HEIGHT)
		self.gol.randomize()


	def draw_world(self) -> None:
		for r in self.gol.world:
			for c in self.gol.world:
				top = r * CELL_SIZE
				left = c * CELL_SIZE
				rect = (left, top, CELL_SIZE, CELL_SIZE)
				radius = CELL_SIZE if CIRCLE else 0
				pg.draw.rect(self.screen, color=CELL_COLOR, rect=rect, border_radius=radius)


	def	step(self) -> None:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()


		self.gol.evolve()
		self.draw_world()
		self.screen.fill(color=BG_COLOR)
		pg.display.update()
		self.clock.tick(self.fps)


if __name__ == '__main__':
	game = GOL_GAME()

	while True:
		game.step()